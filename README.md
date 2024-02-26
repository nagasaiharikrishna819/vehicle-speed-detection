# Traffic Speed Tracker

## Overview

This project implements a simple traffic speed tracking system using OpenCV. It utilizes the Gaussian Mixture-based Background/Foreground Segmentation Algorithm (MOG2) for background subtraction, Euclidean Distance Tracking for object tracking and Display speed of the Vehicles.

## Prerequisites

- Python 3.x
- OpenCV
- NumPy

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/nagasaiharikrishna819/vehicle-speed-detection
   ```

2. Navigate to the project directory:

   ```bash
   cd path/to/folder
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script to start the traffic speed tracker:

   ```bash
   python Vehicle_Tracking.py
   ```

   Ensure that you have a compatible video file (`clip5.mp4` in this example) located at `C:\Users\My world\Downloads\clip5.mp4` or replace the video file path in the script accordingly.

2. Press the 'Esc' key to exit the application.



## Additional Notes

- The `Speed_Detection_Algorithm.py` module contains the `Speed_Detection` class used for object tracking.

Feel free to customize this README file based on your project specifics and additional information you may want to include.
