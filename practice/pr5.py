
import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation

cap=cv2.VideoCapture('data/vtest.avi')
if cap is None:
    print('no')

fig=plt.figure(figsize=(10,6))
fig.canvas.manager.set_window_title('videoCapture')
plt.axis('off')

def init():
    global im
    ret,frame=cap.read()
    im=plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    return im

def updateFrame(k):
    ret,frame=cap.read()
    if ret:
        im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        
ani=animation.FuncAnimation(fig,updateFrame,init_func=init,
                            interval=50)
plt.show()
