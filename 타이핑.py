
from typing import List

# 타입 힌트를 추가한 함수
def sum_of_elements(numbers: List[int]) -> int:
    return sum(numbers)

# 타입 오류 예시
# sum_of_elements(["1", "2", "3"])  # TypeError: can only concatenate str (not "int") to str



##
from typing import List, Tuple, Dict

# 리스트 안에 튜플을 포함한 타입
def process_data(data: List[Tuple[int, str]]) -> Dict[str, int]:
    result = {}
    for num, text in data:
        result[text] = num
    return result

# 예시 데이터
data = [(1, "apple"), (2, "banana")]
print(process_data(data))  # {'apple': 1, 'banana': 2}



##
from typing import Union

# Union을 사용해 여러 타입을 허용
def add(x: Union[int, float], y: Union[int, float]) -> float:
    return x + y

# 잘못된 호출 예시
# add("hello", 5)  # TypeError: can only concatenate str (not "int") to str

print(add(3, 4.5))  # 7.5



## Callable
from typing import Callable

# 함수 타입을 명시
def apply_function(fn: Callable[[int], int], value: int) -> int:
    return fn(value)

# 예시: 값을 두 배로 만드는 함수
def double(x: int) -> int:
    return x * 2

print(apply_function(double, 5))  # 10



# 재할당할 수 없는 변수에는 Final을 사용한다.
from typing import Final
PORT: Final[int] = 8080