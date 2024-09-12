import multiprocessing
import time

# 프로세스에서 실행할 함수 정의
def calculate_sum(start, end, queue):
    temp_sum = 0
    for i in range(start, end):
        temp_sum += i
    queue.put(temp_sum)  # 계산 결과를 큐에 저장

if __name__ == "__main__":
    start_time = time.time()

    # 멀티프로세싱 큐 생성
    queue = multiprocessing.Queue()

    # 프로세스 생성 및 실행
    process1 = multiprocessing.Process(target=calculate_sum, args=(1, 50000001, queue))
    process2 = multiprocessing.Process(target=calculate_sum, args=(50000001, 100000001, queue))
    process1.start()
    process2.start()

    # 프로세스 종료 대기
    process1.join()
    process2.join()

    # 큐에서 결과 가져오기
    sum1 = queue.get()
    sum2 = queue.get()
    total_sum = sum1 + sum2

    end_time = time.time()

    print(f"1부터 1억까지의 합: {total_sum}")
    print(f"실행 시간: {end_time - start_time:.2f}초")