import cv2
import face_recognition
import pandas as pd
from datetime import datetime, timedelta
import os


# Directory containing known face images
known_faces_dir = 'images'


# Load known faces
known_faces = []
known_names = []
for filename in os.listdir(known_faces_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image = face_recognition.load_image_file(f"{known_faces_dir}/{filename}")
        encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(filename.split('.')[0])



# Function to recognize face
def recognize_face(captured_image):
    face_encodings = face_recognition.face_encodings(captured_image)
    if len(face_encodings) == 0:
        return None
    captured_encoding = face_encodings[0]
    matches = face_recognition.compare_faces(known_faces, captured_encoding)
    if True in matches:
        first_match_index = matches.index(True)
        return known_names[first_match_index]
    return None



# Function to mark attendance with the total time spent
def mark_attendance(student_name, total_time, file='attendance.xlsx'):
    total_seconds = total_time.total_seconds()
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    duration = f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")

    try:
        df = pd.read_excel(file)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Name", "Date", "Total Time"])

    new_record_df = pd.DataFrame({
        "Name": [student_name], 
        "Date": [current_date], 
        "Total Time": [duration]
    })

    df = pd.concat([df, new_record_df], ignore_index=True)
    df.to_excel(file, index=False)



# Main execution
def main():
    # Define the time window (e.g., 1 hour)
    time_window = timedelta(hours=1)
    start_window_time = datetime.now()
    end_window_time = start_window_time + time_window

    reappearance_threshold = timedelta(seconds=5)  # Set reappearance threshold (e.g., 5 seconds)
    cam = cv2.VideoCapture(0)
    recognized_name = None
    session_start_time = None
    total_time_spent = timedelta()
    lost_time = None

    while datetime.now() < end_window_time:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Recognize face in the frame
        name = recognize_face(frame)
        if name:
            if recognized_name is None:
                recognized_name = name
                session_start_time = datetime.now()
                print(f"{recognized_name} detected. Session started.")
            elif lost_time:
                if datetime.now() - lost_time <= reappearance_threshold:
                    print(f"{recognized_name} reappeared within threshold. Continuing session.")
                    lost_time = None
                else:
                    session_end_time = datetime.now()
                    session_duration = session_end_time - session_start_time
                    total_time_spent += session_duration
                    print(f"{recognized_name} reappeared but exceeded threshold. New session started.")
                    session_start_time = session_end_time
                    lost_time = None
            else:
                print(f"{recognized_name} is still in front of the camera.")
        else:
            if recognized_name and lost_time is None:
                lost_time = datetime.now()
                print(f"{recognized_name} lost. Waiting for reappearance.")
            elif recognized_name and lost_time and datetime.now() - lost_time > reappearance_threshold:
                session_end_time = datetime.now()
                session_duration = session_end_time - session_start_time
                total_time_spent += session_duration
                print(f"{recognized_name} did not reappear within threshold. Session ended.")
                recognized_name = None
                session_start_time = None
                lost_time = None

        cv2.imshow('Real-time Monitoring', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            break

    if recognized_name:
        session_end_time = datetime.now()
        session_duration = session_end_time - session_start_time
        total_time_spent += session_duration
        print(f"Final session time added for {recognized_name}: {session_duration}")

    if total_time_spent > timedelta(0):
        mark_attendance(recognized_name, total_time_spent)
        print(f"Total time {recognized_name} was in front of the camera: {total_time_spent}")
    else:
        print("No time recorded for any person.")

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

