import numpy as np
import cv2

img=np.full((400,400,3),255, np.uint8)
pt1=(50,100)
pt2=(img.shape[0]-100, 100)
pt3=(img.shape[0]-100, 300)
pt4=(200,250)
linecolor=(0,50,255)
linecolor2=(255,50,0)
thick=10
lineType=cv2.LINE_AA
 #(x1,y1),(x2,y2)
#cv2.rectangle(img,pt1,pt4,linecolor,thick)
 #x,y,w,h
cv2.rectangle(img,(200,200,200,100),linecolor2,thick,lineType)
cv2.circle(img,(int(img.shape[0]/2),int(img.shape[1]/2)),100,(0,255,0),2,cv2.LINE_AA)
# cv2.line(img,pt1,pt2,linecolor,thick,lineType)
# cv2.line(img,pt1,pt3,linecolor,thick,cv2.LINE_AA)
# text="Hello opencv"
# font=cv2.FONT_HERSHEY_SIMPLEX
# fontsize=1.5
# Bluecolor=(100,150,5)
# thick=1
# lineType=cv2.LINE_AA
# cv2.putText(img,text,(50,35),font,fontsize,Bluecolor,thick,lineType)
cv2.imshow('zzz',img)
cv2.waitKey()
cv2.destroyAllWindows()
