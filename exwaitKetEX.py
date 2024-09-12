import cv2,sys
import numpy as np

#화살표를 누르면 원이 이동되는 어플
width,height=512,512
#초기에 원의 좌표
x,y,R = 256,256,50

direction=0

#main
while True:
    #기본 waitKey+Extention키 입력까지 받아들임
    key = cv2.waitKeyEx(30) #timeout=30ms
    
    
    #종료 조건
    if key == 27:#ESC
        break
    elif key ==0x270000:
        x+=10
    # down key
    elif key==0x280000:
        direction=1
        y+=10
    #left key
    elif key==0x250000:
        direction =2
        x-=10
    elif key==0x260000:
        direction=3
        y-=10   
    
    #경계확인
    if x<R:
        X=R
        direction=0
    if x>width-R:
        X=width-R
        direction=2
    if y<R:
        y=R
        direction=1
    if y>height-R:
        y=height-R
        direction=3
    
    #빈 캠버스 생성
    img=np.zeros((width,height,3),np.uint8)+255
    #원을 그린다. img에 (x,y)좌표에, 반지름R로, 빨간색으로 안을 채워서-1
    cv2.circle(img,(x,y),R,(0,0,255),-1)
    cv2.imshow('img',img)
cv2.destroyAllWindows()