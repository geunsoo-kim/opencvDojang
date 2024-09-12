import cv2,sys
import numpy as np
import matplotlib.pyplot as plt



src=cv2.imread("data2/Hawkes.jpg",cv2.IMREAD_GRAYSCALE)

if src is None:
    sys.exit('no')
#equalize전 히스토그램   
hist1=cv2.calcHist([src],[0],None,[256],[0,256])   
#equalize후 히스토그램
dst=cv2.equalizeHist(src)
hist2=cv2.calcHist([dst],[0],None,[256],[0,256])
#normalize후 히스토그램
dst2=cv2.normalize(src,None,0,255,cv2.NORM_MINMAX)
hist3=cv2.calcHist([dst2],[0],None,[256],[0,256])

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)
plt.plot(hist1)
plt.plot(hist2)
plt.plot(hist3)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()


#equalize는 선부분이 강조되는 느낌
#normalize는 전체적으로 선명했다.