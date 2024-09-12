import cv2
import numpy as np
import sys

red="data2/red.jpg"
yello="data2/yello.jpg"
red="data2/red.jpg"

def on_trackbar(pos):
    hmin=cv2.getTrackbarPos('H_min','Trackbar')
    hmax=cv2.getTrackbarPos('H_max','Trackbar')
    dst = cv2.inRange(src_hsv,(hmin,150,0),(hmax,255,255))
src = cv2.imread('data2/red.jpg')

if src is None:
    sys.exit("image Load failed")

#색상의 범위를 잘 지정하려면 bgr->hsv
src_hsv =cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

#창에 트랙바를 넣기 위해서는  창을 먼저 생성
cv2.namedWindow('Trackbar')
cv2.imshow('Trackbar', src)

#트랙바 생성:'H_min' 트랙바의 이름, 범위 0~255,
#on_trackbar :트랙바를 움직일때 호출되는 함수(콜백함수)
cv2.createTrackbar('H_min','Trackbar',0,255, on_trackbar)
cv2.createTrackbar('H_max','Trackbar',0,255, on_trackbar)
on_trackbar(0)

cv2.waitKey()
cv2.destroyAllWindows()