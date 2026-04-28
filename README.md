# AI Virtual Air Canvas using Hand Gesture Recognition

## 📌 Project Overview

AI Virtual Air Canvas is a computer vision-based project that allows users to draw in the air using hand gestures without touching the screen. Using a webcam, the system detects hand landmarks in real time, tracks the index finger, and uses it as a virtual pen for drawing on screen.

This project demonstrates practical applications of Computer Vision, Hand Tracking, and Human-Computer Interaction using Python.

---

## 🚀 Features

* Real-time hand detection using webcam
* Index fingertip tracking for virtual drawing
* Gesture-based draw / stop control
* Multiple color selection (Red, Green, Blue)
* Eraser functionality
* Clear screen option
* Smooth real-time drawing interface
* Professional mini-project for academic and portfolio use

---

## 🛠 Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy
* Git
* GitHub

---

## ⚙️ System Workflow

1. Webcam captures live video feed
2. MediaPipe detects hand landmarks
3. Index fingertip (Landmark 8) is tracked
4. Finger movement is converted into drawing strokes
5. Gesture recognition controls draw / stop mode
6. Top selection bar allows color selection and eraser mode
7. Final output is displayed as a virtual air canvas

---

## 📂 Project Structure

* `main.py` → Basic hand detection
* `main2.py` → Improved hand tracking
* `draw.py` → Finger drawing implementation
* `gesture_draw.py` → Gesture-based draw / stop control
* `final_air_canvas.py` → Final complete project with colors + eraser

---

## ▶️ Installation & Setup

### Step 1: Clone Repository

```bash
git clone https://github.com/mohitgavhane/air-canvas-project.git
cd air-canvas-project
```

### Step 2: Install Required Libraries

```bash
pip install opencv-python mediapipe numpy
```

### Step 3: Run Final Project

```bash
py -3.10 final_air_canvas.py
```

---

## 🎯 Applications

* Academic mini project
* Computer vision demonstration
* Touchless drawing systems
* Smart classroom interaction
* Internship portfolio project
* AI-based user interaction systems

---

## 🔮 Future Enhancements

* Save drawing as image
* Shape recognition using AI
* 3D Air Canvas support
* Voice-controlled commands
* Mobile application version
* Advanced gesture classification

---

## 👨‍💻 Author

### Mohit Gavhane

Computer Science Engineering Student
Passionate about Python, Artificial Intelligence, and Computer Vision Projects.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps improve visibility and supports future development.
