import cv2
video_file="data/video2.avi"

cap=cv2.VideoCapture(video_file)
if cap.isOpened():
    fps=cap.get(cv2.CAP_PROP_FPS)
    delay=int(1000/fps)
    print("FPS:%f,Delay: %dms")