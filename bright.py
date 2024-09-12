#add함수 밝기 제한
import cv2
import numpy as np
import matplotlib.pyplot as plt
isColor=False

if not isColor:
 #grayscale
 src=cv2.imread('data2/candies.png',cv2.IMREAD_GRAYSCALE)
 
 #밝기 변화
 dst1=cv2.add(src,100)
 hist1=cv2.calcHist([src],[0],None,[256],[0,256])
 hist2=cv2.calcHist([dst1],[0],None,[256],[0,100])
 #dst1=src+100
 #범위를 0~255로 지정하고 덧셈연산을 수행
 #dst1=np.clip(src+100,0,255)

if isColor:
    src=cv2.imread("data2/candies.jpg")
    #채널별로 100씩 더한다. 채널의 순서는 BGR
    dst1=cv2.add(src,(100,100,100))
   
    
cv2.imshow('img',src)
cv2.imshow('dst1',dst1)
plt.plot(hist1)
plt.plot(hist2)
plt.show()
# cv2.imshow('dst2',dst2)
cv2.waitKey()
cv2.destroyAllWindows()