import cv2

cap = cv2.VideoCapture('data/vtest.avi')
frame_size=(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(frame_size)

fourcc=cv2.VideoWriter_fourcc(*'xvid')

out1=cv2.VideoWriter('practice/record0.avi',
                     fourcc,20.0,frame_size,isColor=True)
out2=cv2.VideoWriter('practice/record1.avi',
                     fourcc,20.0,frame_size,isColor=False)

while True:
    ret,frame=cap.read()
    if not ret:
        break
    
    out1.write(frame)
    
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    out2.write(gray)
    
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    
    key=cv2.waitKey(25)
    if key==27:
        break
cap.release()
out1.release()
out2.release()
cv2.destroyAllWindows()
