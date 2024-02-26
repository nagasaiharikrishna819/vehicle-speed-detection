import numpy as np
import time
import math


class Speed_Detection:
    def __init__(self):

        # Dictionary to store center points of detected vehicles
        self.center_points = {}

        # Dictionaries to store timing information for each vehicle
        self.Timer = np.zeros((1,1000))
        self.Start_Timer = np.zeros((1,1000))
        self.End_Timer = np.zeros((1,1000))

        # Dictionary to store flags for each vehicle
        self.Flag = np.ones(1000)
        
        # Variable To give Unique Id For Cars
        self.Vehicle_id = 0

        self.capture = np.ones(1000)
        self.exceed = 0
        self.count = 0
    
    def limit(self):

        # Return a Reference Speed for Speed Limit
        return 30 
    
    def tracking (self, Vehicle_detection):

        # List to store detected vehicles
        car_detection = []

        for rect in Vehicle_detection:
            
            x, y, w, h = rect 

            #cx and cy gives Centroid of Rectangle 
            cx = x + w // 2 
            cy = y + h // 2

            same_object_detected = False

            for id, pt in self.center_points.items():

                # Calculate distance between current and previous center points
                dis = math.hypot(cx - pt[0], cy - pt[1])

                # If distance is below a threshold, consider it the same object
                if dis < 70:
                    self.center_points[id] = (cx, cy)
                    car_detection.append([x, y, w, h, id])
                    same_object_detected = True

                    # Start timer when vehicle passes specific y-coordinates
                    if (y >= 410 and y <= 430):
                        self.Start_Timer[0,id] = time.time()

                    # End timer when vehicle passes specific y-coordinates
                    if (y >= 235 and y <= 255):
                        self.End_Timer[0, id] = time.time()
                        self.Timer[0,id] = self.End_Timer[0, id] - self.Start_Timer[0, id]
                        
                    # Set flag for the vehicle
                    if y > 235 :
                        self.Flag[id] = 1

            # If no similar object is detected, add a new object
            if same_object_detected is False :
                self.center_points[self.Vehicle_id] = (cx, cy)
                car_detection.append([x, y, w, h, self.Vehicle_id])
                self.Vehicle_id+= 1
        
        return car_detection
    
    # Calculate speed based on elapsed time between specific y-coordinates
    def SpeedCalculation(self, id):
        Time = self.Timer[0, id]
        if Time!= 0:
            speed = 15.15 / Time
        else:
            speed = 0
        return int(speed)

