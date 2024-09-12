import cv2,sys
import matplotlib.pyplot as plt
import mylib

src=cv2.imread('data/srcThreshold.png',cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('no')

mylib.hist_gray(src)
    
#threshhold 함수를 이용해서 흑과 백을 나눈다.
src_th=cv2.adaptiveThreshold(src,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,51,5)

cv2.imshow('src',src)
cv2.imshow('src_th',src_th)
cv2.waitKey()
cv2.destroyAllWindows()