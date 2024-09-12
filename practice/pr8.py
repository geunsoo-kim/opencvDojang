#뭐지 ㅋㅋㅋㅋ안되네
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Video(animation.FuncAnimation):
    def __init__(self, device=0, fig=None, frames=None,
               interval=80, repeat_delay=50,blit=False,
               **kwargs):
        self.im1.set_array(cv2.merge((gray,gray,gray)))
        
    if fig is None:
        self.fig, self.ax =plt.subplots(1,2, figsize=(10,5))
        self.fig.canvas.manager.set_window_title('Video Capture')
        self.ax[0].set_position([0,0,0.5,1])
        self.ax[0].axis('off')
        
        self.ax[1].set_position([0.5,0,0.5,1])
        self.ax[1].axis('off')
        plt.subplots_adjust(left=0,bottom=0,tright=1,op=1,wspace=0.05,hspace=0.05)
        super(video,self).__init__(self.fig, self.updateFrame,init_func=self.init,
                                   frames=frames,interval=interval,blit=blit,repeat_delay=repeat_delay,**kwargs)
        self.cap=cv2.VideoCapture(device)
        print('start capture')
        
    def init(self):
        ret,self.frame=self.cap.read()
        if ret:
            self.im0=self.ax[0].imshow(cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGB),aspect='auto')
            self.im1=self.ax[1].imshow(np.zeros(self.frmae.shape,self.frame.dtype),aspect='auto')
            
    def updateFrame(self,k):
        ret,self.frame=self.cap.read()
        if ret:
            self.im0.set_array(cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGB))
            gray=cv2.cvtColor(self.frame,cv2.COLOR_BGR2GRAY)
            self.im1.set_array(cv2.merge((gray,gray,gray)))
            
        def close(self):
            if self.cap.isOpened():
                self.cap.release()
            print('finish capture')
            
camera=Video()
plt.show()
camera.close()