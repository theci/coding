import threading
import time

# CPU 집약적인 작업 예시
def cpu_bound_task(n):
    result = 0
    for i in range(n):
        result += i * i
    return result

def main():
    start_time = time.time()

    threads = []
    for _ in range(4):  # 4개의 스레드로 CPU 집약적 작업 수행하기를 기대
        thread = threading.Thread(target=cpu_bound_task, args=(10000000,))
        threads.append(thread)
        thread.start()

    # 모든 스레드가 종료될 때까지 기다리기
    for thread in threads:
        thread.join()

    print(f"Total time: {time.time() - start_time} seconds") # 하지만 실제로는 1개의 cpu로 돌기 때문에 시간이 오래걸린다. 

if __name__ == "__main__":
    main()



import time
import multiprocessing

# CPU 집약적인 작업 예시
def cpu_bound_task(start, end):
    result = 0
    for i in range(start, end):
        result += i * i
    return result

def main():
    start_time = time.time()

    # 각 프로세스에 할당할 범위
    ranges = [(0, 2500000), (2500000, 5000000), (5000000, 7500000), (7500000, 10000000)]

    # 멀티프로세싱을 사용하여 작업을 병렬로 처리
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.starmap(cpu_bound_task, ranges)

    total_result = sum(results)

    print(f"Total result: {total_result}")
    print(f"Total time: {time.time() - start_time} seconds")

if __name__ == "__main__":
    main()




# 실제 예시

import os
import time
from PIL import Image
import multiprocessing

# 이미지 크기 조정 함수
def resize_image(image_path, output_path, size=(800, 800)):
    try:
        with Image.open(image_path) as img:
            img = img.resize(size)  # 이미지 크기 조정
            img.save(output_path)  # 수정된 이미지 저장
        print(f"Processed {image_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

# 이미지 폴더에서 이미지를 읽고 멀티프로세스로 처리하는 함수
def process_images_in_folder(input_folder, output_folder):
    # 이미지 파일 리스트 얻기
    images = [f for f in os.listdir(input_folder) if f.endswith('.jpg') or f.endswith('.png')]
    
    # 프로세스 풀을 생성하여 병렬 처리
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # 각 이미지 파일에 대해 resize_image 함수 호출
        tasks = [(os.path.join(input_folder, image), os.path.join(output_folder, image)) for image in images]
        pool.starmap(resize_image, tasks)  # 병렬로 처리

# 예시 실행
if __name__ == "__main__":
    input_folder = "input_images"  # 입력 이미지 폴더
    output_folder = "output_images"  # 출력 이미지 폴더

    # 출력 폴더가 없으면 생성
    os.makedirs(output_folder, exist_ok=True)

    start_time = time.time()

    process_images_in_folder(input_folder, output_folder)

    print(f"Processing completed in {time.time() - start_time:.2f} seconds")


### 실제 예시 2
# 웹 크롤링은 I/O 바운드 작업이지만, 여러 페이지를 동시에 크롤링할 때 멀티프로세싱을 사용하여 성능을 개선할 수 있습니다. 
# 각 프로세스가 독립적으로 웹 요청을 보내고 데이터를 처리하므로 멀티코어를 효율적으로 사용할 수 있습니다.
import requests
from bs4 import BeautifulSoup
import multiprocessing
import time

# 웹 페이지에서 제목을 추출하는 함수
def crawl_page(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else 'No Title'
        print(f"Page title for {url}: {title}")
    except Exception as e:
        print(f"Error crawling {url}: {e}")

# 여러 페이지를 병렬로 크롤링하는 함수
def crawl_pages(urls):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(crawl_page, urls)

if __name__ == "__main__":
    # 크롤링할 URL 리스트
    urls = [
        "https://www.example.com",
        "https://www.wikipedia.org",
        "https://www.python.org",
        "https://www.github.com"
    ]

    start_time = time.time()

    crawl_pages(urls)  # 멀티프로세싱으로 여러 URL을 크롤링

    print(f"Total time: {time.time() - start_time:.2f} seconds")



### 실제 예시 3
# 대규모 시스템에서는 로그 파일을 분석해야 하는 경우가 많습니다. 로그 파일은 보통 매우 크고, 여러 파일을 동시에 분석할 필요가 있습니다. 
# 멀티프로세싱을 사용하여 여러 로그 파일을 병렬로 처리하는 방법을 보여드립니다.
import os
import multiprocessing
import time

# 로그 파일에서 특정 키워드를 검색하는 함수
def search_log_file(file_path, keyword):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            matches = [line for line in lines if keyword in line]
            return matches
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []

# 여러 로그 파일을 병렬로 분석하는 함수
def analyze_logs(log_files, keyword):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.starmap(search_log_file, [(file, keyword) for file in log_files])
        # 결과를 합침
        all_matches = sum(results, [])
        print(f"Total matches for '{keyword}': {len(all_matches)}")
        return all_matches

if __name__ == "__main__":
    # 로그 파일 리스트 (여기서는 예시로 파일 이름을 사용)
    log_files = [
        "log1.txt", "log2.txt", "log3.txt", "log4.txt"
    ]
    
    # 로그 파일에서 검색할 키워드
    keyword = "ERROR"
    
    start_time = time.time()

    analyze_logs(log_files, keyword)

    print(f"Total time: {time.time() - start_time:.2f} seconds")
