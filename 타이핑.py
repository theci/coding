from typing import List


def sum_list(numbers: List[int]) -> int: # numbers의 모든 요소도 int형 인지를 체크
    return sum(n for n in numbers)


result = sum_list([1, 2, '3', 4])
print(result)


# 여러 개의 타입이 허용될 수 있는 상황이라면 Union을 사용한다. Union[int, float]는 int형과 float형 모두를 허용한다는 뜻이다.

from typing import Union

def add(a: int, b: Union[int, float]) -> str:
    return str(a+b)


# 재할당할 수 없는 변수에는 Final을 사용한다.
from typing import Final
PORT: Final[int] = 8080