import cv2
import numpy as np

# unprocessed = r"C:\Users\TarFa\code\climbingBuddy\fastAPI\processing\climbing1.jpeg"
unprocessed = r"C:\Users\TarFa\code\3climbingLog\fastAPI\testingPhotos\threeColoursTest.png"

image = cv2.imread(unprocessed)


# Crop Image
def cropImage(img):
    img = image[0:950, 100:800]
    img = cv2.resize(img, (500,500), interpolation=cv2.INTER_LINEAR)
    return img

image = cropImage(image)

# Blurring + Canny

blurColor = cv2.blur(image, (3,3))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray, (3,3))

edged = cv2.Canny(blur, 30, 200)

# ======== Contours =========
contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

avgColor = []
contourMasks = []
for contour in contours:
    mask = np.zeros(image.shape[:2], np.uint8) # [:2] bc mask must be grayscaled, not coloured like image
    cv2.drawContours(mask, contour, -1, 255, cv2.FILLED)
    contourMasks.append(mask)
    avgColor.append(cv2.mean(image, mask))

# ========= K Mean Clustering ===========


avgColor = np.array(avgColor, dtype=np.float32)
avgColor = avgColor.reshape(-1,3)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0) 

noMeans = 3
ret, label, center = cv2.kmeans(avgColor, noMeans, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
# need to use elbow / silloet method to decide no. means
# center - all the different colours it's found
# label - list of which center (by index) each colour falls into

center = np.uint8(center)
labelsAssigned = center[label.flatten()] # this is some beautiful notation... though it does obscure
# colours have now been quantized.

masksFiltered = []
for index, oneLabel in enumerate(labelsAssigned[:190]):
    # print(index)
    if np.all(oneLabel == center[0]):
        masksFiltered.append(contourMasks[index])

def showColours(center):
    height, width = (20,20)
    showColours = np.full((height,width,3), (255,255,255), dtype=np.uint8)
    for index, color in enumerate(center):
        showColours = np.concatenate((np.full((height,width, 3), color, dtype=np.uint8), showColours), axis=1)

    return showColours

showColours = showColours(center)

allMasksImage = sum(masksFiltered)

cv2.imshow("colours", showColours)
cv2.imshow("blurred", allMasksImage)
cv2.imshow("image", image)
cv2.waitKey(0)



cv2.destroyAllWindows()


