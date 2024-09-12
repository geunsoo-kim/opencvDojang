import threading
import time

# 공유 변수 설정
sum_of_numbers = 0
lock = threading.Lock()

# 스레드 함수 정의
def calculate_sum(start, end):
    global sum_of_numbers
    temp_sum = 0
    for i in range(start, end):
        temp_sum += i

    # 공유 변수 업데이트 시 race condition 방지 위해 lock 사용
    with lock:
        sum_of_numbers += temp_sum

# 시작 시간 기록
start_time = time.time()

# 스레드 생성 및 실행
thread1 = threading.Thread(target=calculate_sum, args=(1, 50000001))
thread2 = threading.Thread(target=calculate_sum, args=(50000001, 100000001))
thread1.start()
thread2.start()

# 스레드 종료 대기
thread1.join()
thread2.join()

# 종료 시간 기록
end_time = time.time()

print(f"1부터 1억까지의 합: {sum_of_numbers}")
print(f"실행 시간: {end_time - start_time:.2f}초")