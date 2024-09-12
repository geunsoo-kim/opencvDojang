import cv2
cap=cv2.VideoCapture('data/vtest.avi')

frame_size=(cap.get(cv2.CAP_PROP_FRAME_WIDTH),
            cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(frame_size)

while True:
    ret,frame=cap.read()
    if ret is False:
        break
    
    cv2.imshow('video',frame)
    
    key=cv2.waitKey(100)
    if key==27:
        break
    
cv2.destroyAllWindows()