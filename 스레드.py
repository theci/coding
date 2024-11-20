# 스레드를 사용하면, CPU 집약적인 작업에서 멀티코어를 활용하지는 못하더라도 I/O 바운드 작업에서 병렬성을 활용할 수 있습니다. 
# 예를 들어, 여러 파일을 동시에 다운로드하거나, 여러 네트워크 요청을 동시에 처리하는 등의 작업에서는 스레드를 사용하여 성능을 개선할 수 있습니다.

### 문제점
import time

def download_file(file_id):
    print(f"Downloading file {file_id}...")
    time.sleep(2)  # 다운로드 시뮬레이션 (2초)
    print(f"File {file_id} downloaded.")

def main():
    start_time = time.time()
    
    # 순차적으로 파일 다운로드
    download_file(1)
    download_file(2)
    download_file(3)
    
    print(f"Total time: {time.time() - start_time} seconds")

if __name__ == "__main__":
    main()
"""
Downloading file 1...
File 1 downloaded.
Downloading file 2...
File 2 downloaded.
Downloading file 3...
File 3 downloaded.
Total time: 6.0 seconds
"""

### 해결법

import time
import threading

def download_file(file_id):
    print(f"Downloading file {file_id}...")
    time.sleep(2)  # 다운로드 시뮬레이션 (2초)
    print(f"File {file_id} downloaded.")

def main():
    start_time = time.time()
    
    # 스레드를 이용한 파일 다운로드
    threads = []
    for i in range(1, 4):
        thread = threading.Thread(target=download_file, args=(i,))
        threads.append(thread)
        thread.start()

    # 모든 스레드가 종료될 때까지 기다리기
    for thread in threads:
        thread.join()
    
    print(f"Total time: {time.time() - start_time} seconds")

if __name__ == "__main__":
    main()

"""
Downloading file 1...
Downloading file 2...
Downloading file 3...
File 1 downloaded.
File 2 downloaded.
File 3 downloaded.
Total time: 2.0 seconds
"""