import cv2,sys
import numpy as np

src=cv2.imread("data2/rose.bmp",cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('no')

    
#blur 처리
#필터의 크기가 (3x3)
dst=cv2.GaussianBlur(src,(0,0),3 )
dst2=cv2.GaussianBlur(src,(5,5),3 )


cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)
cv2.waitKey()
cv2.destroyAllWindows()