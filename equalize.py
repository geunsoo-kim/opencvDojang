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


cv2.imshow('src',src)
cv2.imshow('dst',dst)

plt.plot(hist1)
plt.plot(hist2)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()