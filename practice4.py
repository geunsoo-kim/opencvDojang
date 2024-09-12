import cv2
from matplotlib import pyplot as plt

imagefile="data2/images1.png"
plt.axis('off')
imgBGR=cv2.imread(imagefile)

#imgrgb=cv2.cvtColor(imgBGR,cv2.COLOR_BGR2RGB)
plt.imshow(imgBGR)
plt.show()