import cv2,sys
import numpy as np
import matplotlib.pyplot as plt
# 이미지 불러오기
src = cv2.imread("misson/misson_image01.png")



# 2. 노이즈 제거 (Non-local Means Denoising 적용)
dst = cv2.fastNlMeansDenoisingColored(src, None, 10, 10, 7, 21)

# 3. 선명도 향상 (Unsharp Masking 적용)
blurred = cv2.GaussianBlur(dst, (0, 0), 2)
sharpened = cv2.addWeighted(dst, 1.5, blurred, -0.5, 0)




#dst=cv2.bilateralFilter(src, -1,10,5)#약간 부드러워진 느낌 딱히
#dst=cv2.Canny(src,64,128 )선만 살아있음
#dst=cv2.equalizeHist(src)///
hist2=cv2.calcHist([dst],[0],None,[256],[0,256])

#dst2=cv2.normalize(src,None,0,255,cv2.NORM_MINMAX)
#hist3=cv2.calcHist([dst2],[0],None,[256],[0,256])
#plt.imshow(selected_frame, cmap='gray')
#plt.plot(src)#이미지와 에러 메시지를 종합해 보니, 아마도 Matplotlib을 사용하여 450 프레임의 영상 데이터를 한 번에 그래프로 표현하려는 것으로 보입니다. 각 프레임은 1040x해상도에 3개의 색상 채널(RGB)을 가지고 있고요.
               #이 경우, (450,) 모양의 x 데이터는 프레임 번호를 나타내고, (450, 1040, 3) 모양의 y 데이터는 각 프레임의 픽셀 값을 나타내는 것 같습니다. 하지만 Matplotlib은 이런 형태의 데이터를 한 번에 처리하여 그래프로 그릴 수 없습니다.
plt.plot(hist2)

plt.show()

cv2.imshow('img',src)
cv2.imshow('dst',dst)

cv2.waitKey()
cv2.destroyAllWindows()


