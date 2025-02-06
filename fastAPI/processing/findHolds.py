import cv2
import numpy as np

unprocessed = r"C:\Users\TarFa\code\climbingBuddy\fastAPI\processing\climbing1.jpeg"
destination = r"C:\Users\TarFa\code\climbingBuddy\fastAPI\processing\processed_images\test.jpeg"

image = cv2.imread(unprocessed)
image = image[0:950, 100:800]
image = cv2.resize(image, (500,500), interpolation=cv2.INTER_LINEAR)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([95, 0, 0])   # Lower bound for red
upper_red1 = np.array([130, 255, 255]) # Upper bound for red

    # lower_red2 = np.array([170, 120, 70]) # Second range for red
    # upper_red2 = np.array([180, 255, 255]) 

    # # Create masks for red regions
red_mask = cv2.inRange(hsv_image, lower_red1, upper_red1)


cv2.imshow("red mask", red_mask)

contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
        
        if cv2.contourArea(contour) > 100:  # Adjust area threshold as needed
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green box

    
cv2.imshow("climbing wall",image)
cv2.waitKey(0)
cv2.destroyAllWindows()