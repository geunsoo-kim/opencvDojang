import cv2, sys

#이미지 불러오기

img = cv2.imread('data2/opencv-logo-white.png',cv2.IMREAD_UNCHANGED)
dst=cv2.imread('data2/cat.bmp')
#모든 행,모든열, 0~2번 채널
src=img[:,:,0:3]
#알파채널만 슬라이싱
mask=img[:,:,3]
#print(mask.shape)

#mask의 영역
h,w=mask.shape[:2]
crop=src[10:10+h, 10:10+w]

#마스크 연산
cv2.copyTo(logo,mask,dst)
cv2.imshow('src',src)
cv2.imshow('logo',logo)
cv2.imshow('mask',mask)
cv2.imshow('img', dst)
cv2.waitKey()
cv2.destroyAllWindows()
