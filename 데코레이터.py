# 문제점
import time


def elapsed(original_func):   # 기존 함수를 인수로 받는다.
    def wrapper():
        start = time.time()
        result = original_func()    # 기존 함수를 수행한다.
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))  # 기존 함수의 수행시간을 출력한다.
        return result  # 기존 함수의 수행 결과를 리턴한다.
    return wrapper

@elapsed
def myfunc():
    print("함수가 실행됩니다.")

myfunc()  # 함수가 실행됩니다.
myfunc("You need python")  # 에러가 난다. 인수없는 wrapper함수로 구현했기 때문



### 모든 입력 인수를 받는 파라미터 구현
import time


def elapsed(original_func):   # 기존 합수를 인수로 받는다.
    def wrapper(*args, **kwargs):   # *args, **kwargs 파라미터 추가
        start = time.time()
        result = original_func(*args, **kwargs)  # 전달받은 *args, **kwargs를 입력파라미터로 기존함수 수행
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))  # 수행시간을 출력한다.
        return result  # 함수의 결과를 리턴한다.
    return wrapper

@elapsed
def myfunc(msg):
    """ 데코레이터 확인 함수 """
    print("'%s'을 출력합니다." % msg)

myfunc("You need python")