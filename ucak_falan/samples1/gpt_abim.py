import cv2
import numpy as np

# Read image from file
img = cv2.imread("/Users/yigitcaneroglu/cuaqcu/ai_falan/ucak_falan/samples1/lil_circle.jpeg")

# Convert image to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define range of red color in HSV
lower_red = np.array([0,100,100])
upper_red = np.array([10,255,255])

# Threshold the HSV image to get only red colors
mask = cv2.inRange(hsv, lower_red, upper_red)

# Find circles in the image
circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

# Check if any circles were found
if circles is not None:
    # Convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")

    # Loop over the circles
    for (x, y, r) in circles:
        # Draw the circle in the output image
        cv2.circle(img, (x, y), r, (0, 255, 0), 4)

        # Calculate the distance from the center of the image to the center of the circle
        distance = np.sqrt((x - img.shape[1] / 2)**2 + (y - img.shape[0] / 2)**2)

        # Print the distance
        print("Distance: {:.2f}".format(distance))

# Show the output image
cv2.imshow("Output", img)
cv2.waitKey(0)
