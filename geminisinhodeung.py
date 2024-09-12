import cv2
import numpy as np

def detect_traffic_light_color(image_path):
    """
    이미지에서 신호등 색깔을 검출하는 함수

    Args:
        image_path (str): 이미지 파일 경로

    Returns:
        str: 검출된 신호등 색깔 ('red', 'yellow', 'green' 또는 'unknown')
    """
    image = cv2.imread('data2/red.jpg')

    # BGR -> HSV 변환
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 각 색상 범위 설정 (HSV)
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([179, 255, 255])
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([80, 255, 255])

    # 각 색상 마스크 생성
    red_mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
    red_mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)
    yellow_mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)

    # 각 색상 영역의 픽셀 수 계산
    red_pixels = cv2.countNonZero(red_mask)
    yellow_pixels = cv2.countNonZero(yellow_mask)
    green_pixels = cv2.countNonZero(green_mask)

    # 가장 많은 픽셀을 가진 색상 검출
    if red_pixels > yellow_pixels and red_pixels > green_pixels:
        return 'red'
    elif yellow_pixels > red_pixels and yellow_pixels > green_pixels:
        return 'yellow'
    elif green_pixels > red_pixels and green_pixels > yellow_pixels:
        return 'green'
    else:
        return 'unknown'


# 이미지 파일 경로
image_path = 'traffic_light.png'  # 이미지 파일 경로를 적절히 변경해주세요

# 신호등 색깔 검출
detected_color = detect_traffic_light_color(image_path)

# 결과 출력
print(f"Detected traffic light color: {detected_color}")