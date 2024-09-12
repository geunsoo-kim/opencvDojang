import cv2
import numpy as np

# 마우스 클릭 좌표를 저장할 리스트
points = []

# 이미지 생성
img = np.zeros((512, 512, 3), np.uint8) + 255  # 흰색 배경

def mouse_callback(event, x, y, flags, param):
    global points, img
    if event == cv2.EVENT_LBUTTONDOWN: #선 그리기
        points.append((x, y))
        cv2.polylines(img, [np.array(points, np.int32)], False, (0, 255, 0), 1)
        cv2.imshow("shape", img)
        if flags & cv2.EVENT_FLAG_SHIFTKEY and len(points) >2: #다각형 완성
            cv2.polylines(img, [np.array(points, np.int32)], True, (0, 255, 0), 1)
            cv2.imshow("shape", img)
            points = []
       
    elif event == cv2.EVENT_RBUTTONDOWN:  # 오른쪽 클릭으로 원 완성
        cv2.circle(img,(x,y),50,(0,0,255),1)
        cv2.imshow("shape",img)

cv2.namedWindow("shape")
cv2.setMouseCallback("shape", mouse_callback)

cv2.imshow("shape",img)

cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite("data2/shape.jpg",img)
