import cv2,sys
import numpy as np
src=cv2.imread('data2/rose.bmp',cv2.IMREAD_GRAYSCALE)

if src is  None:
    sys.exit('no')

#사용자 커널(=필터)을 생성
kernel=np.ones((3,3),dtype=np.float32)/9
dst=cv2.filter2D(src,-1,kernel)
mask=np.array([[-2,-1,0],
              [0,5,1],
              [-1,0,0]])
dst2=cv2.filter2D(src,-1,mask)
#blur kernel을 사용한거랑 비슷하다.
# =>dst2=cv2.blur(src,(3,3))
cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)
cv2.waitKey()
cv2.destroyAllWindows()