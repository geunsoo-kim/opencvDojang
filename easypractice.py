import cv2
img_file="data/fkyou.gif"
img=cv2.imread(img_file)

if img is not None:
    cv2.imshow('img',img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('븅신 이것도 못하냐?')