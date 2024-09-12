import cv2,sys
import numpy as np
import matplotlib.pyplot as plt

#이미지 불러오기
src=cv2.imread('misson/misson_image01.png')

if src is None:
    sys.exit('image load failed')
    
#컬러 채널 분리
colors = ['b','g','r']
bgr_planes = cv2.split(src)
  
for (p, c) in zip(bgr_planes, colors):
    hist = cv2.calcHist([p],[0],None,[256],[0,256])
    print(hist.shape)
    plt.plot(hist, color=c)
    
# plt.show()

#YCBCr 채널을 활용
#BGR ->Ycbcr로 컬러스페이스 변경
src_Ycbcr=cv2.cvtColor(src,cv2.COLOR_BGR2YCrCb)
hist1=cv2.calcHist([src_Ycbcr],[0],None,[256],[0,256])

# plt.plot(hist1)
# plt.show()


Y,Cb,Cr=cv2.split(src_Ycbcr)
#src_Ycbcr에 normalize 적요
# Y_equalize=cv2.equalizeHist(Y)
#Y_norm=cv2.normalize(Y,None,0,255,cv2.NORM_MINMAX)
Y_add=cv2.add(Y,50)
hist2=cv2.calcHist([Y_add],[0],None,[256],[0,256])
plt.plot(hist2)
plt.show()

#Y_equalize,cb,cr채널 합치기
src_Ycbcr_add = np.zeros_like(src_Ycbcr)  # 빈 이미지 배열 생성
src_Ycbcr_add[:,:,0] = Y_add  # Y 채널 추가
src_Ycbcr_add[:,:,1] = Cb     # Cb 채널 추가
src_Ycbcr_add[:,:,2] = Cr     # Cr 채널 추가

# 나머지 코드는 동일하게 유지
src_add = cv2.cvtColor(src_Ycbcr_add, cv2.COLOR_YCrCb2BGR)
cv2.imshow('src_add', src_add)
cv2.waitKey()
cv2.destroyAllWindows()