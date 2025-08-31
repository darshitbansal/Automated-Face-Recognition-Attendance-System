# Automated Real-Time Face Recognition and Attendance Tracking System

## 📌 Overview  
🚀 An AI-powered **real-time face recognition and attendance tracking system** that uses computer vision to automatically identify individuals, track their presence, and log attendance efficiently.

This project is an **Automated Attendance System** that uses **Face Recognition** to identify individuals and mark their attendance. It eliminates the need for manual attendance systems, making the process faster, more secure, and error-free.  

The system captures live video feed, detects faces, matches them with stored images of registered individuals, and updates the attendance file automatically. 

## ✨ Features  
- 📷 **Real-time Face Detection & Recognition** using `face_recognition` and `OpenCV`.  
- 🧾 **Automatic Attendance Marking** in an Excel (`.xlsx`) file.  
- 📂 **Stores attendance with Name, Date, and Total Time spent**.  
- 🖼️ **Easily add new faces** by placing images in the `images/` folder.  
- ⚡ **Robust Accuracy** which uses threshold-based reappearance handling to reduce false positives.
- ⚡ **Time Spent Tracking** makes it records the total duration each person was in front of the camera.

## 📂 Project Structure
Automated-Face-Recognition-Attendance/
│── images/ # Known face images
│── src/ # Source code files
│ └── main.py # Final code
│── data/ # Attendance file
│ └── attendance.xlsx
│── requirements.txt # Dependencies
│── README.md
│── .gitignore

## 🛠️ Technologies Used  
- **Python 3.8+**  
- **OpenCV** → for image/video processing  
- **face_recognition** → for face detection & recognition  
- **NumPy** → for matrix operations  
- **Pandas / openpyxl** → for handling attendance Excel file  

## 🚀 Future Enhancements

-- Add GUI Dashboard for attendance visualization.
-- Send email/SMS notifications for absentees.
-- Store attendance in Database (MySQL/PostgreSQL).
-- Integrate with web-based portal for teachers/admins.

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 👨‍💻 Author

Developed by Darshit Bansal
