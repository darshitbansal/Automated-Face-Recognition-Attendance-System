# Automated Real-Time Face Recognition and Attendance Tracking System

🚀 An AI-powered **real-time face recognition and attendance tracking system** that uses computer vision to automatically identify individuals, track their presence, and log attendance efficiently.

## 📌 Features
- **Face Recognition & Tracking**: Uses deep learning-based face encodings to recognize individuals in real time.
- **Automated Attendance**: Marks attendance in an Excel file (`data/attendance.xlsx`).
- **Session Management**: Tracks presence within a defined time window (e.g., 1 hour).
- **Robust Accuracy**: Uses threshold-based reappearance handling to reduce false positives.
- **Time Spent Tracking**: Records the total duration each person was in front of the camera.

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