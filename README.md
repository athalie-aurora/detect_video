# Security System with OpenCV

This Python script implements a motion detection system using OpenCV. It captures video from the default camera, detects faces and bodies using Haarcascades, and records video when motion is detected. The recording stops after a specified period of no motion detected and saves recorded videos with the date and time.

## Documentation

This Python Script implements a motion detection system using OpenCV. It captures video from the default camera, detects faces and bodies using Haarcascades, and records video when motion is detected. The recording stops after a specified period of no motion detected.

**Key Functionalities:**

- Accesses the default webcam.
- Employs Haarcascades for face and body detection.
- Initiates video recording upon detection and continues for a specified duration after the last detection.
- Displays a live feed with bounding boxes around detected faces.
- Allows for termination using the 'q' key.

**Limitations:**

- Relies on pre-trained Haarcascades, which might have limitations in accuracy and robustness.
- Records continuously upon detection, which could lead to large video files. More sophisticated motion detection could be implemented for efficiency.
- Lacks features like email or cloud storage integration for recordings.

**Usage:**

- Ensure you have OpenCV installed (`pip3 install opencv-python`).
- Run the script. The live feed will display on your screen.
- Press 'q' to quit the application.
