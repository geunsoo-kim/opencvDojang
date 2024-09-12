import cv2,sys
import numpy as np
import math
def translate(src, x_move=0,y_move=0):
    #이미지의 이동 변환 x->200, y->100만큼ㅁ 이동
    #이동변환 행렬
    h,w=src.shape[:2]
    aff=np.array([[1,0,x_move],[0,1,y_move]],dtype=np.float32)
    #aff=np.array([[1,0,x_move],[0,1,y_move]],dtype=np.float32)
    dst=cv2.warpAffine(src,aff,(h+y_move,w+x_move))
    #return dst

src=cv2.imread('data2/rose.bmp')

def shear(src, x_shear=0,y_shear=0):
    if x_shear>0 and y_shear==0:
        aff = np.array([[1, x_shear,0],[0,1,0]],dtype=np.float32)
    elif y_shear>0 and x_shear==0:
        aff =np.array([[1,0,0],[y_shear,1,0]],dtype=np.float32)
    
    h,w=src.shape[:2]
    dst=cv2.warpAffine(src,aff,w,(h+int(h*y_shear)))
    return dst 

def scale(src,x_scale,y_scale):
    h,w=src.shape[:2]
    aff=np.array([[x_scale,0,0],[0,y_scale,0]],dtype=np.float32)
    dst=cv2.warpAffine(src,aff,(w,h))
    return dst
def rotate(src,rad):
    aff=np.array([[np.cos(rad),np.sin(rad),0],\
        [-np.sin(rad),np.cos(rad),0]],dtype=np.float32)
    dst=cv2.warpAffine(src,aff,(0,0))
    return dst
def rotate2(src,angle):
    h,w=src.shape[:2]
    #튜플로 centerPt를 저장
    centerPt=(w/2,h/2)
    aff=cv2.getRotationMatrix2D(centerPt,angle,1)
    dst=cv2.warpAffine(src,aff,(0,0))
    return dst
    
#각도를 radian으로 변환하는 공식
angle=20
rad=angle*math.pi/180
dst=rotate2(src,angle)
if src is None:
    sys.exit('no')
#dst=shear(src,0,0.5)  
#dst=scale(src,1.5,1.5)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()