import numpy as np
import cv2 as cv
from SpeedDetection import *

# Path to the video file
Path_to_videofile = r"C:\Users\My world\Documents\roadradar-main\clip3.mp4"

# Open the video file
Raw_video = cv.VideoCapture(Path_to_videofile)

# Background subtractor
Background_subtractor = cv.createBackgroundSubtractorMOG2(detectShadows=True)

# Kernels for morphological operations
kernalopen = np.ones((5, 5), np.uint8)
kernalClose = np.ones((11, 11), np.uint8)
kernalerode = np.ones((5, 5), np.uint8)

# Tracker for vehicle detection and speed calculation
Tracker = Speed_Detection()

while True:
    # Read a frame from the video
    ret, frame = Raw_video.read()

    # Check if the frame is successfully read
    if not ret:
        break

    # Resize the frame
    frame = cv.resize(frame, None, fx=0.5, fy=0.5)

    # Region of interest (ROI)
    roi = frame[20:1720, 0:1980]

    # Background subtraction
    iframe = Background_subtractor.apply(roi)
    _, testframe = cv.threshold(iframe, 200, 255, cv.THRESH_BINARY)
    mask1 = cv.morphologyEx(testframe, cv.MORPH_OPEN, kernalopen)
    mask2 = cv.morphologyEx(mask1, cv.MORPH_CLOSE, kernalClose)
    e_image = cv.erode(mask2, kernalerode)

    # Find contours in the processed image
    contours, _ = cv.findContours(e_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # List to store detected vehicles
    vehicle_detection = []

    for cont in contours:
        area = cv.contourArea(cont)
        if area > 1000:
            x, y, w, h = cv.boundingRect(cont)
            cv.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
            vehicle_detection.append((x, y, w, h))

    # Track vehicles and get their IDs
    cars_ids = Tracker.tracking(vehicle_detection)

    for car_id in cars_ids:
        x, y, w, h, id = car_id

        # Calculate and display the speed
        Car_Speed = Tracker.SpeedCalculation(id)
        if Car_Speed < Tracker.limit():
            cv.putText(roi, str(Car_Speed), (x, y - 15), cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            cv.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 3)
        else:
            cv.putText(roi, str(Car_Speed), (x, y - 15), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
            cv.rectangle(roi, (x, y), (x + w, y + h), (0, 0, 255), 3)

    # Display the result
    cv.imshow("result", roi)

    # Check for key press to exit the loop
    Kill_Loop = cv.waitKey(1)
    if Kill_Loop != -1:
        break

# Release resources
cv.destroyAllWindows()
Raw_video.release()
