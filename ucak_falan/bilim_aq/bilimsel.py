import cv2
import numpy as np

im_path = "/Users/yigitcaneroglu/cuaqcu/ai_falan/ucak_falan/bilim_aq/bruhullah106.jpeg"
### kullanilan foto 960p

#blurring and smoothin
img1=cv2.imread(im_path,)
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
duble_blured = cv2.blur(img3,(5,5))




### smoothed 2 aslinda blurlu ve sadece kirmizi bolgeleri filtreliyor

cv2.imwrite("/Users/yigitcaneroglu/cuaqcu/ai_falan/ucak_falan/bilim_aq/1bruhullah106.jpeg", duble_blured)

