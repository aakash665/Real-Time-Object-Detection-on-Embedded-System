# Real-Time Object Detection on Embedded Systems

This project implements a real-time object detection system using a MobileNet SSD model optimized with TensorFlow Lite. Designed for resource-constrained environments, the project runs on a Raspberry Pi, leveraging OpenCV for image processing and enabling seamless performance with a connected camera module.

---

## Features

- **Object Detection:** Real-time detection of objects in video streams using a MobileNet SSD model.
- **Optimized for Embedded Systems:** Efficient use of TensorFlow Lite for reduced memory usage and power consumption.
- **Integrated Image Processing:** OpenCV handles preprocessing (image frames) and post-processing (detection results).
- **Continuous Operation:** Designed for long-term usage in low-power hardware environments.

---

## Hardware Requirements

- **Raspberry Pi (Model 3B+ or newer)** with Raspbian OS
- **Camera Module** (e.g., Raspberry Pi Camera Module v2 or USB Webcam)
- **MicroSD Card (16GB or higher)**
- **Power Supply for Raspberry Pi**

---

## Software Requirements

- Python 3.7 or newer
- TensorFlow Lite
- OpenCV (Version 4.x)
- NumPy
- Required Python libraries:
  - `tflite-runtime`
  - `opencv-python`
  - `numpy`

---

## Project Architecture

1. **Video Input:** The camera module streams video frames to the Raspberry Pi.
2. **Preprocessing:** OpenCV resizes and normalizes image frames for compatibility with the MobileNet SSD model.
3. **Inference:** TensorFlow Lite processes the frames to detect objects in real-time.
4. **Post-Processing:** Detected objects are highlighted with bounding boxes and labels, displayed on the output video.

---

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/aakash665/Real-Time-Object-Detection-on-Embedded-System.git
cd Real-Time-Object-Detection-on-Embedded-System
