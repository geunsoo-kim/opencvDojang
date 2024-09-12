import cv2,sys
import numpy as np

def translate(src, x_move,y_move):
    #이미지의 이동 변환 x->200, y->100만큼ㅁ 이동
    #이동변환 행렬
    aff=np.array([[1,0,x_move],[0,1,y_move]],dtype=np.float32)
    dst=cv2.warpAffine(src,aff,(0,0))
    return dst

src=cv2.imread('data2/lenna.bmp')

def scale(src,x_scale,y_scale):
    h,w=src.shape[:2]
    aff=np.array([[x_scale,0,0],[0,y_scale,0]],dtype=np.float32)
    dst=cv2.warpAffine(src,aff,(w,h))
    return dst

if src is None:
    sys.exit('no')
#dst=shear(src,0,0.5)  
dst=translate(src,1.5,1.5)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()