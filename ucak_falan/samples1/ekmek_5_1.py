import cv2
import numpy as np

def filter_red(frame):
    img1 = cv2.imread(frame)

    hsv = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)

    lower_red2 = np.array([170,50,50])
    upper_red2 = np.array([180,255,255])

    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    res2 = cv2.bitwise_and(img1,img1, mask= mask2)

    kernel2 = np.ones((5, 5), np.float32) / 25
    im = cv2.filter2D(src=res2, ddepth=-1, kernel=kernel2)

    return im


