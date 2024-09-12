#좀더 매끈
import cv2,sys
import numpy as np

#cartoon filter

src=cv2.imread("data2/lenna.bmp")

if src is None:
    sys.exit('no')

    
#blur 처리
#필터의 크기가 (3x3)
dst=cv2.bilateralFilter(src, -1,10,5)


cv2.imshow('src',src)
cv2.imshow('dst',dst)

cv2.waitKey()
cv2.destroyAllWindows()