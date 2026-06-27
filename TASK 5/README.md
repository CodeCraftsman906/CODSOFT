# AI-Powered Face Recognition System

## Overview

This project is a real-time Face Recognition System developed using Python, OpenCV, DeepFace, and ArcFace. The application detects faces from a live webcam feed and verifies the identity of a user by comparing facial embeddings generated from a registered reference image.

The project demonstrates the complete face recognition pipeline, including face detection, feature extraction, embedding generation, similarity comparison, and identity verification.

---

## Features

* Real-time webcam integration
* Face detection using Haar Cascade Classifier
* Face verification using DeepFace
* ArcFace-based facial embeddings
* Live identity recognition and display
* Real-time bounding box visualization
* Threshold-based verification system

---

## Technologies Used

* Python
* OpenCV
* DeepFace
* ArcFace
* TensorFlow
* NumPy

---

## Project Structure

Face-Recognition-System/

│
├── known_faces/
│   └── raghav.jpg
│
├── face_detection.py
│
├── face_recognition.py
│
├── requirements.txt
│
├── README.md
│

---

## Working

### Phase 1: Face Detection

The system uses OpenCV's Haar Cascade Classifier to detect human faces in real time from a webcam feed. Detected faces are highlighted using bounding boxes.

### Phase 2: Face Recognition

A reference image of the registered user is stored in the system. DeepFace with ArcFace generates facial embeddings from both the stored image and the live webcam frame. These embeddings are compared using cosine similarity to determine whether the detected face belongs to the registered user.

---

## Results

* Successfully detects faces in real time.
* Performs live face verification using ArcFace.
* Displays the recognized user's name on the webcam feed.
* Identifies unknown faces when verification conditions are not satisfied.

---

## Future Enhancements

* Multi-person face recognition database
* Attendance management system
* Face registration module
* Advanced face detectors such as RetinaFace
* Cloud and web deployment
* Face tracking for improved performance
* Real-time multi-face recognition

---

## Learning Outcomes

Through this project, the following concepts were explored:

* Computer Vision Fundamentals
* Face Detection
* Face Recognition
* Face Verification
* Facial Embeddings
* ArcFace Architecture
* Deep Learning-Based Recognition Systems
* Real-Time Webcam Processing

---

