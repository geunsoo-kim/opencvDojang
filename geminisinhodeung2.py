import cv2
import numpy as np

def on_trackbar(val):
    global h_min, h_max, s_min, s_max, v_min, v_max

    h_min = cv2.getTrackbarPos('H_min', 'Traffic Light')
    h_max = cv2.getTrackbarPos('H_max', 'Traffic Light')
    s_min = cv2.getTrackbarPos('S_min', 'Traffic Light')
    s_max = cv2.getTrackbarPos('S_max', 'Traffic Light')
    v_min = cv2.getTrackbarPos('V_min', 'Traffic Light')
    v_max = cv2.getTrackbarPos('V_max', 'Traffic Light')

    lower_range = np.array([h_min, s_min, v_min])
    upper_range = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv_image, lower_range, upper_range)

    masked_image = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow('Traffic Light', masked_image)


# 이미지 파일 경로 (실제 파일 경로로 변경 필요)
image_paths = [
    "data2/red.jpg", 
    "data2/yellow.jpg", 
    "data2/green.jpg"
]

# 각 신호등 이미지 처리
for image_path in image_paths:
    # 이미지 로드
    image = cv2.imread(image_path)
    # BGR -> HSV 변환
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 트랙바 초기값 설정
    h_min, h_max, s_min, s_max, v_min, v_max = 0, 179, 0, 255, 0, 255

    # 윈도우 생성 및 트랙바 추가
    cv2.namedWindow('Traffic Light')
    cv2.createTrackbar('H_min', 'Traffic Light', h_min, 179, on_trackbar)
    cv2.createTrackbar('H_max', 'Traffic Light', h_max, 179, on_trackbar)
    cv2.createTrackbar('S_min', 'Traffic Light', s_min, 255, on_trackbar)
    cv2.createTrackbar('S_max', 'Traffic Light', s_max, 255, on_trackbar)
    cv2.createTrackbar('V_min', 'Traffic Light', v_min, 255, on_trackbar)
    cv2.createTrackbar('V_max', 'Traffic Light', v_max, 255, on_trackbar)

    # 초기 마스크 및 결과 이미지 표시
    on_trackbar(0)

    # 키 입력 대기
    cv2.waitKey(0)
    cv2.destroyAllWindows()