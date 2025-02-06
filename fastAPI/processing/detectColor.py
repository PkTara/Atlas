import cv2
import numpy as np

# Load the image
# image = cv2.imread('climbing1.jpeg')

def detectColor(image):
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image_colored = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)  # Convert grayscale back to BGR for masking

    # Convert to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the color range for the mask (e.g., red color)
    # lower_bound = np.array([0, 120, 70])  # Lower bound of the color in HSV
    # upper_bound = np.array([10, 255, 255])  # Upper bound of the color in HSV

    lower_bound = np.array([95, 0, 0])   # Lower bound for red
    upper_bound = np.array([130, 255, 255])

    # Create a mask for the specific color
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

    # Invert the mask
    mask_inv = cv2.bitwise_not(mask)
    purple_background = np.full_like(image, (150, 100, 200))


    # Extract the color part
    colored_part = cv2.bitwise_and(image, image, mask=mask)
    # gray_part = cv2.bitwise_and(purple_background, purple_background, mask=mask_inv)

    

    # Extract the grayscale part
    gray_part = cv2.bitwise_and(gray_image_colored, gray_image_colored, mask=mask_inv)

    # Combine both parts
    final_image = cv2.add(colored_part, gray_part)

    # Display the result
    final_image = final_image[0:950, :]
    final_image = cv2.resize(final_image, None, fx=0.7, fy=0.7, interpolation=cv2.INTER_AREA)
    
    return(final_image)

if __name__ == "__main__":
    final_image = detectColor()
    cv2.imwrite('highlighted_climbing_holds.jpg', final_image)
    cv2.imshow('Highlighted Color', final_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
