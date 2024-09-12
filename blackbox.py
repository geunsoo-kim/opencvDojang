import cv2
import numpy as np
import threading
import time
import os
import shutil
import datetime

# 설정
VIDEO_DURATION = 60  # 동영상 길이 (초)
DISK_SPACE_THRESHOLD = 10  # 디스크 공간 부족 임계값 (%)

# 전역 변수
recording = False  # 녹화 중 여부

def create_video_folder():
    """현재 날짜_시간으로 폴더를 생성하는 함수"""
    now = datetime.datetime.now()
    folder_name = now.strftime("%Y%m%d_%H")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name

def check_disk_space():
    """남은 디스크 공간을 확인하고 부족하면 오래된 폴더 삭제"""
    total, used, free = shutil.disk_usage("/")
    free_percentage = (free / total) * 100

    if free_percentage < DISK_SPACE_THRESHOLD:
        print("디스크 공간 부족! 오래된 녹화 파일을 삭제합니다.")
        folders = sorted([
            f for f in os.listdir() if os.path.isdir(f) and f.startswith("20")
        ])
        while free_percentage < DISK_SPACE_THRESHOLD and folders:
            oldest_folder = folders.pop(0)
            shutil.rmtree(oldest_folder)
            print(f"폴더 삭제: {oldest_folder}")
            total, used, free = shutil.disk_usage("/")
            free_percentage = (free / total) * 100
        print(f"디스크 공간 확보: {free_percentage:.2f}%")

def record_video(folder_name):
    """동영상을 녹화하고 저장하는 함수"""
    global recording
    recording = True

    now = datetime.datetime.now()
    file_name = now.strftime("%Y%m%d-%H%M%S") + ".mp4"
    file_path = os.path.join(folder_name, file_name)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(file_path, fourcc, 20.0, (640, 480))

    cap = cv2.VideoCapture(0)  # 0번 카메라 사용
    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
        return

    start_time = time.time()
    while time.time() - start_time < VIDEO_DURATION and recording:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)

    cap.release()
    out.release()
    print(f"녹화 완료: {file_path}")
    recording = False

def main():
    while True:
        folder_name = create_video_folder()
        check_disk_space()

        video_thread = threading.Thread(target=record_video, args=(folder_name,))
        video_thread.start()

        time.sleep(VIDEO_DURATION)  # 60초 대기

if __name__ == "__main__":
    main()