import cv2,sys
import numpy as np

src=cv2.imread("data2/shape.jpg")
if src is None:
    sys.exit('no')

def scale(src,x_scale,y_scale):
    h,w=src.shape[:2]
    aff=np.array([[x_scale,0,0],[0,y_scale,0]],dtype=np.float32)
    dst=cv2.warpAffine(src,aff,(w,h))
    return dst
print(src.shape)
dst1=cv2.resize(src,(0,0),fx=1/4,fy=1/4,interpolation=cv2.INTER_CUBIC)
dst2=cv2.resize(src,(0,0),fx=1/4,fy=1/4,interpolation=cv2.INTER_AREA)   



cv2.imshow('src',src)
cv2.imshow('INTER_CUBIC',dst1)

cv2.imshow('INTER_AREA',dst2)
cv2.waitKey()
cv2.destroyAllWindows()