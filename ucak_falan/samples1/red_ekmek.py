import cv2
import numpy as np


#blurring and smoothin
ph_path = '/Users/yigitcaneroglu/cuaqcu/ai_falan/ucak_falan/samples1/1080p_izle.jpeg'
img1=cv2.imread('/Users/yigitcaneroglu/cuaqcu/ai_falan/ucak_falan/samples1/1080p_izle.jpeg',1)

img_copy = img1.copy()

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

#cv2.imshow('res2',res2)
#### aga burdan yukarisi calisiyor dokunma artik
#cv2.imwrite('/Users/yigitcaneroglu/cuaqcu/ai_falan/ucak_falan/samples1/red_filtered_img.jpg', res2)

gray = cv2.cvtColor(res2,cv2.COLOR_BGR2GRAY)
### burasi da checkpoint ab bonfire gibi dusun
"""
cv2.waitKey(0)
cv2.destroyAllWindows()
"""