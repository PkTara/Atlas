import cv2
import numpy as np

def process(unprocessed, destination):

    # Load the image
    # image = cv2.imread('climbing1.jpeg')
    image = cv2.imread(unprocessed)

    # print(unprocessed)
    # cv2.imshow("climbingImage" , image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    image = image[0:950, :800]

    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the color range for red in HSV
    # Red in HSV can wrap around 0° and 360°, so you may need two ranges

    lower_red1 = np.array([95, 0, 0])   # Lower bound for red
    upper_red1 = np.array([130, 255, 255]) # Upper bound for red

    # lower_red2 = np.array([170, 120, 70]) # Second range for red
    # upper_red2 = np.array([180, 255, 255]) 

    # # Create masks for red regions
    red_mask = cv2.inRange(hsv_image, lower_red1, upper_red1)
    # mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)

    # # Combine masks
    # red_mask = cv2.bitwise_or(mask1, mask2)

    # Find contours of the red regions
    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes around each hold
    max_x = 0
    min_x = 10000
    max_y = 0
    min_y = 10000
    for contour in contours:
        # Optional: Filter small contours by area

        
        if cv2.contourArea(contour) > 100:  # Adjust area threshold as needed
            x, y, w, h = cv2.boundingRect(contour)

            max_x = x if x > max_x else max_x
            min_x = x if x < min_x else min_x
            max_y = y if y > max_y else max_y
            min_y = y if y < min_y else min_y

            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green box


    # print("FOR CROPPING" , min_x, min_y, max_x, max_y)
    # Show the result
    padding = 50
    width_y = max_y - min_y
    width_x = max_x - min_x
    x_padding = int(((width_y * 9/16) - width_x + 100) /2)
    print("XPADDING", x_padding)
    image = image[min_y-padding:max_y+padding, min_x-x_padding:max_x+x_padding]

    from detectColor import detectColor
    image = detectColor(image)

    # image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    # cv2.imshow('Climbing Holds', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # # Optionally save the result
    # cv2.imwrite('./processed_images/1.jpg', image)
    print(destination)
    cv2.imwrite(destination, image)

if __name__ == "__main__":
    process(r"C:\Users\TarFa\code\climbingBuddy\fastAPI\processing\climbing1.jpeg", r"C:\Users\TarFa\code\climbingBuddy\fastAPI\processing\processed_images\test.jpeg")


    # import sys
    # if len(sys.argv) != 3:
    #     print("ERROR: Must include file input and destination")
    # else:
        # process(*sys.argv[1:2])