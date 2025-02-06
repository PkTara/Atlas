import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('climbing1.jpeg')

# Convert to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Extract the Hue channel
hue_channel = hsv_image[:, :, 0]

# Calculate the histogram for the Hue channel
# The hue range is 0 to 180 in OpenCV (HSV uses 180 bins instead of 360)
hue_hist = cv2.calcHist([hue_channel], [0], None, [180], [0, 180])

# Normalize the histogram (optional, for better comparison)
hue_hist = cv2.normalize(hue_hist, hue_hist).flatten()

threshold = 0.2
high_frequency_hues = [hue for hue, freq in enumerate(hue_hist) if freq > threshold]

# Print the hues
print("Hues with frequency > 0.2:", high_frequency_hues)

# Plot the histogram as a bar chart
plt.figure(figsize=(10, 6))
plt.bar(range(180), hue_hist, color='orange', edgecolor='black', width=1)
plt.title('Hue Frequency Distribution')
plt.xlabel('Hue Value (0-179)')
plt.ylabel('Frequency')
plt.xlim([0, 180])
plt.show()
