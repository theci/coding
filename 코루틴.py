import asyncio
import aiohttp
from aiohttp import ClientSession
import time

# 비동기적으로 웹 페이지에서 제목을 추출하는 함수
async def fetch_page(session: ClientSession, url: str):
    try:
        async with session.get(url) as response:
            html = await response.text()
            title = html.split('<title>')[1].split('</title>')[0] if '<title>' in html else 'No Title'
            print(f"Page title for {url}: {title}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")

# 여러 웹 페이지를 비동기적으로 크롤링하는 함수
async def crawl_pages(urls: list):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = fetch_page(session, url)
            tasks.append(task)
        
        # 모든 비동기 작업을 동시에 실행
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    urls = [
        "https://www.example.com",
        "https://www.wikipedia.org",
        "https://www.python.org",
        "https://www.github.com"
    ]
    
    start_time = time.time()

    # 비동기 웹 크롤링 시작
    asyncio.run(crawl_pages(urls))

    print(f"Total time: {time.time() - start_time:.2f} seconds")


