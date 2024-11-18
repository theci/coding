import logging

logging.basicConfig(level=logging.INFO) # 로깅 모듈의 기본 레벨은 WARNING으로 설정됩니다. INFO는 설정 레벨인 WARNING 보다 높으므로 해당 메세지가 출력되지 않는 겁니다. 
# logging.basicConfig(filename="mylog.txt", level=logging.INFO)  filename인자를 주면 로그가 파일로 출력

def hap(a, b):
    ret = a + b
    logging.info(f"input: {a} {b}, output={ret}")
    return ret

result = hap(3, 4) # INFO:root:input: 3 4, output=7




### 위 함수를 클래스로 만든 코드
class Logger:
    def __init__(self):
        # 로깅 설정
        logging.basicConfig(level=logging.INFO)
    
    def hap(self, a, b):
        ret = a + b
        logging.info(f"input: {a} {b}, output={ret}")
        return ret

# 클래스 사용 예시
logger = Logger()
result = logger.hap(3, 4)  # INFO:root:input: 3 4, output=7