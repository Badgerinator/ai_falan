import numpy as np
import cv2


cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, captured_frame = cap.read()
    output_frame = captured_frame.copy()

### ekmek51.py
    """
    hsv = cv2.cvtColor(captured_frame,cv2.COLOR_BGR2HSV)

    lower_red2 = np.array([170,0,0])
    upper_red2 = np.array([180,255,255])

    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    res2 = cv2.bitwise_and(captured_frame,captured_frame, mask= mask2)

    kernel2 = np.ones((5, 5), np.float32) / 25
    im = cv2.filter2D(src=res2, ddepth=-1, kernel=kernel2)
    """

    img1=captured_frame
    hsv = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
    #lower red
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    #upper red
    lower_red2 = np.array([170,50,50])
    upper_red2 = np.array([180,255,255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(img1,img1, mask= mask)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    res2 = cv2.bitwise_and(img1,img1, mask= mask2)
    img3 = res+res2
    kernel = np.ones((15,15),np.float32)/225
    im = cv2.filter2D(img3,-1,kernel)


### uygar.py


    # read image

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # do adaptive threshold on gray image
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 101, 3)


    
    """
    # apply morphology open then close
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    blob = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,9))
    blob = cv2.morphologyEx(blob, cv2.MORPH_CLOSE, kernel)

    # invert blob
    blob = (255 - blob)

    # Get contours
    cnts = cv2.findContours(blob, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    big_contour = max(cnts, key=cv2.contourArea)

    # test blob size
    blob_area_thresh = 1000
    blob_area = cv2.contourArea(big_contour)
    if blob_area < blob_area_thresh:
        print("Blob Is Too Small")

    # draw contour
    uygar = im.copy()
    cv2.drawContours(uygar, [big_contour], -1, (0,0,255), 1)
    """
    
    cv2.imshow('frame', thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()