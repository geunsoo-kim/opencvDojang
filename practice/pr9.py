#색깔-하늘or정면or사이드-등받이유무-팔걸이 유무
#1.배경:흰색 책상,우드 테이블
#2.데이터 증식 조건
#   2-0.스마트폰으로 사진 촬영후 이미지 크기를 줄여주자. (이미지 크기 224x224)
#       대상물 촬영을 어떻게 해야할지 확인        

#   2-1.rotate:회전(10~30도)법위 안에서 어느 정도 각도를 넣어야 인식이 잘 되는가?
#   2-2.hflip,vflip:도움이 되는가? 넣을 것인가?
#   2-3.resize,crop:가능하면 적용해보자.
#   2-4.파일명을 다르게 저장 cf)jelly_woodfreen_sky_no_na.jpg,jelly_whitefreen_sky_no_na.jpg
#       jelly_wood_rot_15freen_sky_no_na.jpg,jelly_wood_hflipfreen_sky_no_na.jpg,jelly_wood_resizefreen_sky_no_na.jpg
#   2-5.클래스 별로 폴더를 생성
#   2-6.데이터를 어떻게 넣느냐에 따라 어떻게 동작되는지 1~2줄로 요약   

#구성 순서
#1.촬영한다.
#2.이미지를 컴퓨터로 복사, resize한다.
#3.육안으로 확인, 이렇게 사용해도 되는가?
#4.함수들을 만든다.resize,rotate,hflip,vflip,crop
#  원본 파일명을 읽어서 파일명을 생성하는 기능은 모든 함수에 있어야한다.
#5.단일 함수를 검증
#6.함수를 활용해서 기능 구현
#7.테스트(경우의 수)
#8.데이터셋을 teachable machine사이트에 올려서 테스트
#9.인식이 잘 안되는 케이스를 분석하고 케이스 추가 1~8에서 구현된 기능을 이용

import cv2,sys
import numpy as np
import os

RESIZE_EN = True
ROTATE_EN = True

dataPath=os.path.join(os.getcwd(),'DataAug')
dataorg=os.path.join(dataPath,'org')
fileName=os.path.join(dataorg,'blue_sky_y_na.jpg')
print(fileName)
img=cv2.imread(fileName)

dsize=(224,224)
#스마트폰으로 촬영된 이미지를 224x224
# resize시에는 interpolation을 무엇으로 할 지도 중요
img_resize=cv2.resize(img,dsize,interpolation=cv2.INTER_AREA)  
for angle in range(0,360,15):
    center = (img_resize.shape[1] // 2, img_resize.shape[0] // 2)   
    rotation_matrix =cv2.getRotationMatrix2D(center, angle, 1)
    rotated_image = cv2.warpAffine(img_resize, rotation_matrix, (img_resize.shape[1], img_resize.shape[0]))

    
    
    output_folder = "C:\\Users\\SBA\\opencvDojang\\surplus_image\\blue_y" # 원하는 폴더 경로를 지정
    os.makedirs(output_folder, exist_ok=True)  # 폴더가 없으면 생성
    output_filename = os.path.join(output_folder, f"rotated_{angle}_blue_sky_y_na.jpg")# 파일 이름 설정
    cv2.imwrite(output_filename, rotated_image)
    cv2.imshow('rotated_image',rotated_image)
    cv2.waitKey(50)
#flipped_image=cv2.flip(img_resize,1)
#output_folder = "C:\\Users\\SBA\\opencvDojang\\surplus_image\\blue_y" # 원하는 폴더 경로를 지정
#os.makedirs(output_folder, exist_ok=True)  # 폴더가 없으면 생성
#output_filename = os.path.join(output_folder, "rotate_blue_sky_y_na.jpg")
#cv2.imwrite(output_filename,flipped_image)
#cv2.imshow('rotated_image',flipped_image)

cv2.destroyAllWindows()  
    