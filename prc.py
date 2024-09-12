import cv2

cap=cv2.VideoCapture('data/vtest.avi')

frame_size=(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(frame_size)

while True:
    
    ret,frame=cap.read()
    
    if not ret:
        break
    cv2.imshow('frame',frame)
    
    key=cv2.waitKey(100)
    if key==27:
        break
    
if cap.isOpened():
    cap.release()
    
cv2.destroyAllWindows()