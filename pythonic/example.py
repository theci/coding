### 1. 리스트 생성 - 리스트 컴프리헨션을 사용하여 코드가 간결하고 효율적으로 작성됨.
# # #안좋은 예:
numbers = []
for i in range(10):
    numbers.append(i)

# # #좋은 예:
numbers = [i for i in range(10)]



### 2. 조건문 (간단한 if-else) - 삼항 연산자를 사용하여 간결하게 작성.
# # #안좋은 예:
if x > 10:
    result = "large"
else:
    result = "small"

# # #좋은 예:
result = "large" if x > 10 else "small"


### 3. 문자열 연결
# # #안좋은 예:
s = ""
for word in words:
    s += word + " "

# # #좋은 예:
s = " ".join(words)


### 4. 파일 열기 후 자동 닫기 - 컨텍스트 관리자(with)를 사용하여 파일을 자동으로 닫도록 작성.
# # #안좋은 예:
f = open('file.txt', 'r')
data = f.read()
f.close()

# # #좋은 예:
with open('file.txt', 'r') as f:
    data = f.read()


### 5. 딕셔너리 키 검사 - get() 메서드를 사용하여 코드가 더 간결해짐.
# # #안좋은 예:
if 'key' in my_dict:
    value = my_dict['key']
else:
    value = None

# # #좋은 예:
value = my_dict.get('key', None)



### 6. 다중 조건문 - 삼항 연산자를 중첩하여 더 간결하게 작성.
# # #안좋은 예:
if x > 10:
    result = "large"
elif x > 5:
    result = "medium"
else:
    result = "small"

# # #좋은 예:
result = "large" if x > 10 else "medium" if x > 5 else "small"


### 7. 빈 리스트 체크 - 빈 리스트 체크 시, len() 함수 대신 리스트 자체를 조건식에 사용할 수 있음.
# # #안좋은 예:
if len(my_list) > 0:
    print("List is not empty")

# # #좋은 예:
if my_list:
    print("List is not empty")


### 8. 함수 인자 기본값 설정 - 기본값 인자를 설정하여 코드가 더 직관적이고 깔끔해짐.
# # #안좋은 예:
def add(x, y):
    if y is None:
        y = 0
    return x + y

# # #좋은 예:
def add(x, y=0):
    return x + y


### 9. 중복 코드 제거 - 중복된 반복문을 하나로 합쳐서 코드 중복을 제거.
# # #안좋은 예:
def process_data(data):
    for i in data:
        print(i)
    for i in data:
        if i > 0:
            print(i)

# # #좋은 예:
def process_data(data):
    for i in data:
        print(i)
        if i > 0:
            print(i)



### 10. 반복문에서의 else 사용 - else 문이 반복문과 함께 사용될 때 유용하지만, 경우에 따라 직관적이지 않게 느껴질 수 있습니다.
# #안좋은 예:
for item in items:
    if item == target:
        found = True
        break
else:
    found = False
# #좋은 예:
for item in items:
    if item == target:
        found = True
        break
else:
    found = False



### 11. 정수 나누기 - 정수 나누기는 //를 사용하여 더 직관적으로 작성.
# #안좋은 예:
result = int(a / b)
# #좋은 예:
result = a // b

### 12. 불필요한 else 문 - else 없이 if 문만 사용해도 충분한 경우가 많음.
# #안좋은 예:
if x > 10:
    print("greater")
else:
    print("smaller or equal")
# #좋은 예:
if x > 10:
    print("greater")



### 13. 리스트 컴프리헨션에서 조건문 - 리스트 컴프리헨션을 사용하여 더 간결하고 ic하게 작성.
# #안좋은 예:
numbers = []
for i in range(10):
    if i % 2 == 0:
        numbers.append(i)
# #좋은 예:
numbers = [i for i in range(10) if i % 2 == 0]


### 14. 람다 함수 사용 - 람다 함수를 사용하여 간결하게 표현.
# #안좋은 예:



def square(x):
    return x * x
# #좋은 예:



square = lambda x: x * x




### 15. 튜플 언팩킹 - 튜플을 바로 언팩킹하여 더 간결한 코드 작성.
# #안좋은 예:



a = pair[0]
b = pair[1]
# #좋은 예:



a, b = pair




### 17. 정규 표현식 사용 - 정규 표현식을 사용하여 문자열 검색을 효율적으로 처리.
# #안좋은 예:
import re
if "abc" in string:
    print("found")
# #좋은 예:
import re
if re.search("abc", string):
    print("found")




### 19. map과 filter 사용 - map() 함수를 사용하여 간결하게 작성.
# #안좋은 예:
result = []
for x in data:
    result.append(x * 2)
# #좋은 예:
result = list(map(lambda x: x * 2, data))




### 20. 일반적인 에러 핸들링 - 구체적인 예외를 잡고 예외 메시지를 제공하여 문제를 더 쉽게 추적.
# #안좋은 예:
try:
    # some code
except Exception:
    print("An error occurred")
# #좋은 예:



try:
    # some code
except ValueError as e:
    print(f"A value error occurred: {e}")

### 21. 반복문 최적화 - 인덱스를 직접 다루기보다 항목 자체를 사용하는 것이 더 pythonic
# #안좋은 예:



for i in range(len(arr)):
    print(arr[i])
# #좋은 예:



for item in arr:
    print(item)



### 22. defaultdict 사용 - defaultdict를 사용하여 더 간결하게 처리.

# #안좋은 예:



d = {}
if key in d:
    d[key] += 1
else:
    d[key] = 1
# #좋은 예:



from collections import defaultdict
d = defaultdict(int)
d[key] += 1



### 23. itertools 사용 - itertools 모듈을 활용하여 더 효율적인 반복 처리.
# #안좋은 예:
for i in range(10):
    print(i)
# #좋은 예:
import itertools
for i in itertools.count(0):
    print(i)



### 24. enumerate 사용 - enumerate를 사용하여 인덱스와 값을 동시에 얻을 수 있음.
# #안좋은 예:
index = 0
for item in collection:
    print(index, item)
    index += 1
# #좋은 예:



for index, item in enumerate(collection):
    print(index, item)



### 25. zip 사용 - zip을 사용하여 두 리스트를 동시에 순회.
# #안좋은 예:
for i in range(len(a)):
    print(a[i], b[i])

# #좋은 예:
for item_a, item_b in zip(a, b):
    print(item_a, item_b)



### 26. sorted 사용 - sorted()를 사용하여 원본 리스트를 변경하지 않고 새로운 정렬된 리스트를 반환.
# #안좋은 예:
numbers = [3, 1, 2]
numbers.sort()
# #좋은 예:
numbers = sorted([3, 1, 2])



### 27. 기본값 인자 사용 - 기본값을 직접 설정하여 간결하게 처리.
# #안좋은 예:
def greet(name):
    if name is None:
        name = "Stranger"
    print(f"Hello, {name}")
# #좋은 예:
def greet(name="Stranger"):
    print(f"Hello, {name}")




### 28. set의 차집합 사용 - isdisjoint() 메서드를 사용하여 더 직관적으로 표현.
# 안좋은 예:
if not any(x in set2 for x in set1):
    print("No common elements")
# 좋은 예:
if set1.isdisjoint(set2):
    print("No common elements")





### 34. 빈 문자열과 리스트 초기화 - not을 사용하여 빈 문자열을 검사.
#안좋은 예:
string = ""
if len(string) == 0:
    print("Empty")

# #좋은 예:
if not string:
    print("Empty")



### 35. 중복된 코드 제거 - max()를 사용하여 더 간결하게 작성.
# 안좋은 예:
if a > 10:
    x = a
else:
    x = 10

# #좋은 예:
x = max(a, 10)



### 36. int 타입으로 변환하기 - 사용자로부터 입력을 받을 때 명시적으로 메시지를 주어 사용자 경험을 향상시킴.
# #안좋은 예:
x = int(input("Enter a number"))
# #좋은 예:
x = int(input("Enter a number: "))

### 37. 조건문에서 is 대신 == 사용 - None과 비교할 때는 is를 사용해야 하지만, 객체 비교시에는 ==를 사용.
# #안좋은 예:
if x is None:
    print("No value")

# #좋은 예:
if x == None:
    print("No value")


###39. 리스트 인덱싱 - enumerate()를 사용하여 코드가 간결하고 효율적임.
# #안좋은 예:
i = 0
for item in items:
    print(i, item)
    i += 1

# #좋은 예:
for i, item in enumerate(items):
    print(i, item)



### 40. 리스트 컴프리헨션에서 조건문 사용 - 리스트 컴프리헨션을 사용하여 조건을 효율적으로 추가.
# #안좋은 예:



numbers = []
for i in range(10):
    if i % 2 == 0:
        numbers.append(i)
# #좋은 예:



numbers = [i for i in range(10) if i % 2 == 0]

### 41. defaultdict 활용 - defaultdict를 사용하여 더 간결하고 효율적인 코드 작성.
# #안좋은 예:
counts = {}
if key in counts:
    counts[key] += 1
else:
    counts[key] = 1

# #좋은 예:
from collections import defaultdict
counts = defaultdict(int)
counts[key] += 1

### 42. any와 all 사용 - any()를 사용하여 조건이 만족되는지 간결하게 확인.
# #안좋은 예:
found = False
for item in items:
    if item == target:
        found = True
        break

# #좋은 예:
found = any(item == target for item in items)

### 43. zip 함수 사용 - zip()을 사용하여 두 리스트를 동시에 순회.
# #안좋은 예:
for i in range(len(a)):
    print(a[i], b[i])

# #좋은 예:
for item_a, item_b in zip(a, b):
    print(item_a, item_b)



### 44. map 함수 사용 - map()을 사용하여 리스트를 더 간결하게 처리.
# #안좋은 예:
squares = []
for x in numbers:
    squares.append(x * x)

# #좋은 예:
squares = list(map(lambda x: x * x, numbers))



### 45. 리스트 중복 제거 - 집합(set)을 사용하여 중복을 자동으로 제거.
# #안좋은 예:



numbers = []
for x in range(10):
    if x not in numbers:
        numbers.append(x)
# #좋은 예:



numbers = list(set(range(10)))

### 46. itertools 사용 - itertools를 사용하여 더 유연한 반복 처리. 
# #안좋은 예:
for i in range(10):
    print(i)

# #좋은 예:
import itertools
for i in itertools.count():
    print(i)


### 47. sorted 사용 - sorted()는 새로운 리스트를 반환하고, sort()는 원본 리스트를 변경.
# #안좋은 예:
numbers = [3, 1, 2]
numbers.sort()

# #좋은 예:
numbers = sorted([3, 1, 2])

### 48. Counter 사용 - Counter를 사용하여 더 직관적이고 간결하게 작성.
# #안좋은 예:
counts = {}
for item in items:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

# #좋은 예:
from collections import Counter
counts = Counter(items)

### 49. join() 사용 - join()을 사용하여 문자열을 더 효율적으로 결합.
# #안좋은 예:



result = ""
for word in words:
    result += word + " "
# #좋은 예:

result = " ".join(words)


### 50. isinstance 활용 - isinstance()를 사용하여 타입 체크.
# #안좋은 예:
if type(x) == int:
    print("x is an integer")

# #좋은 예:
if isinstance(x, int):
    print("x is an integer")



### 51. 예외 처리 (다중 예외 처리) - 여러 예외를 하나로 묶어서 처리.
# #안좋은 예:
try:
    # some code
except ValueError:
    print("ValueError")
except TypeError:
    print("TypeError")

# #좋은 예:
try:
    # some code
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

### 52. try와 except 활용 - 구체적인 예외를 처리하여 코드의 명확성과 안정성 증가.
# #안좋은 예:
try:
    x = 10 / 0
except Exception:
    print("Something went wrong")
# #좋은 예:
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")


### 56. 반복문에서 continue 사용 - continue를 사용하여 불필요한 코드 중복을 줄임.
# #안좋은 예:
for x in range(10):
    if x % 2 == 0:
        print(x)
# #좋은 예:
for x in range(10):
    if x % 2 != 0:
        continue
    print(x)



### 58. unpack 사용 - 튜플 언팩킹을 사용하여 더 간결하게 변수에 값을 할당.
# #안좋은 예:



x = tuple[0]
y = tuple[1]
# #좋은 예:



x, y = tuple



### 59. 반복문에서 else 사용 - 반복문과 else를 활용하여 더 직관적으로 작성.
# #안좋은 예:



for i in range(10):
    if i == 5:
        break
else:
    print("Not found")
# #좋은 예:



for i in range(10):
    if i == 5:
        break
else:
    print("Not found")


### 60. slice 사용 - 리스트 슬라이싱을 더 간단하게 사용할 수 있음.
# #안좋은 예:
sublist = my_list[0:10]

# #좋은 예:
sublist = my_list[:10]


### 61. enumerate()와 함께 사용 - enumerate()를 사용하여 리스트의 인덱스와 값을 동시에 쉽게 얻을 수 있습니다.
#안좋은 예:



for i in range(len(lst)):
    print(i, lst[i])
#좋은 예:



for idx, value in enumerate(lst):
    print(idx, value)

### 62. with 구문 활용 - with 구문을 사용하여 자원을 안전하게 관리하고 자동으로 파일을 닫을 수 있습니다.
#안좋은 예:



file = open('file.txt', 'r')
content = file.read()
file.close()
#좋은 예:



with open('file.txt', 'r') as file:
    content = file.read()



### 64. itertools.islice 활용 - itertools.islice를 사용하여 리스트의 일부분을 간결하게 추출.
#안좋은 예:
subset = []
for i in range(5):
    subset.append(lst[i])
#좋은 예:
import itertools
subset = list(itertools.islice(lst, 5))



### 65. collections.Counter 사용 - Counter를 사용하여 요소의 개수를 더 간결하게 계산.
#안좋은 예:
counts = {}
for item in items:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
#좋은 예:



from collections import Counter
counts = Counter(items)



### 66. 인자 기본값을 None으로 설정 - None을 기본값으로 설정하여 더 유연한 함수 인자 처리.
#안좋은 예:



def foo(a, b):
    if b is None:
        b = []
#좋은 예:



def foo(a, b=None):
    if b is None:
        b = []

### 67. 모듈 가져오기와 이름 변경 - 모듈 import 시 별칭을 사용하여 코드의 가독성을 높입니다.
#안좋은 예:



import numpy as np
import pandas as pd
#좋은 예:



import numpy as np
import pandas as pd



### 68. 정렬된 리스트에서의 이진 탐색 - bisect를 사용하여 정렬된 리스트에서 효율적으로 이진 탐색.
#안좋은 예:



target = 5
if target in sorted_list:
    print("Found!")
#좋은 예:



import bisect
if bisect.bisect_left(sorted_list, target) < len(sorted_list) and sorted_list[bisect.bisect_left(sorted_list, target)] == target:
    print("Found!")

### 69. max()와 min()을 활용한 최대/최소값 찾기 - max()와 min() 함수를 사용하여 최대값과 최소값을 간결하게 구할 수 있습니다.
#안좋은 예:



maximum = -float('inf')
for num in numbers:
    if num > maximum:
        maximum = num
#좋은 예:



maximum = max(numbers)

### 70. __init__에서 super() 사용 - super()를 사용하여 부모 클래스의 초기화 메서드를 호출.
#안좋은 예:



class Child(Parent):
    def __init__(self, a, b):
        Parent.__init__(self, a, b)
#좋은 예:



class Child(Parent):
    def __init__(self, a, b):
        super().__init__(a, b)

### 71. str.format() 대신 f-strings 사용 - f-strings을 사용하여 문자열 포매팅을 간결하게 처리.
#안좋은 예:
name = "Alice"
greeting = "Hello, {}".format(name)

#좋은 예:
name = "Alice"
greeting = f"Hello, {name}"



###72. is를 올바르게 사용 - None 비교에는 is를 사용하는 것이 Pythonic.
#안좋은 예:



if my_list == None:
    print("Empty")
#좋은 예:



if my_list is None:
    print("Empty")


### 74. 리스트 길이 계산에서 len() 사용 - len()을 쓰지 않고 리스트 자체의 불리언 평가를 사용.
#안좋은 예:



if len(my_list) != 0:
    print("Not empty")
#좋은 예:



if my_list:
    print("Not empty")


### 76. 문자열 슬라이싱 - 문자열 슬라이싱을 더 간결하게 사용.
#안좋은 예:
string = string[0:len(string)-1]

#좋은 예:
string = string[:-1]


### 77. dict.get() 사용 - dict.get()를 사용하여 기본값을 지정.
#안좋은 예:



if key in my_dict:
    value = my_dict[key]
else:
    value = None
#좋은 예:



value = my_dict.get(key, None)



### 78. all() 함수 활용 - all()을 사용하여 리스트가 모두 True인지 한 번에 체크.
#안좋은 예:



all_true = True
for x in my_list:
    if not x:
        all_true = False
        break
#좋은 예:



all_true = all(my_list)

### 79. sorted()와 key 인자 사용 - key에 함수 이름을 직접 전달하여 더 간결하게 정렬.
#안좋은 예:



def custom_sort(x):
    return len(x)
sorted_list = sorted(my_list, key=lambda x: len(x))
#좋은 예:



sorted_list = sorted(my_list, key=len)



### 80. any() 함수 활용 - any()를 사용하여 조건을 간결하게 처리.
#안좋은 예:
found = False
for x in my_list:
    if x == target:
        found = True
        break

#좋은 예:
found = any(x == target for x in my_list)


### 81. 단일 문자 반복 - 문자열 곱셈을 사용하여 더 효율적으로 반복 처리.
#안좋은 예:



text = ""
for _ in range(10):
    text += "a"
#좋은 예:



text = "a" * 10

### 82. iter와 next 활용 - iter와 next를 사용하여 반복 가능한 객체를 제어.
#안좋은 예:



for item in collection:
    print(item)
#좋은 예:



it = iter(collection)
while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break



### 83. sorted()와 reverse 사용 - sorted()와 reverse를 한 번에 처리.
#안좋은 예:
numbers.sort()
numbers.reverse()
#좋은 예:
numbers = sorted(numbers, reverse=True)



### 84. 하위 클래스에서 super()로 부모 메서드 호출 - super()를 사용하여 부모 클래스의 메서드를 호출.
#안좋은 예:
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)

#좋은 예:
class Child(Parent):
    def __init__(self):
        super().__init__()



# 85. frozenset 사용 변경 - 불가능한 frozenset을 사용하여 불변 집합을 만들기.
#안좋은 예:
my_set = set([1, 2, 3])
my_set.add(4)
#좋은 예:

my_set = frozenset([1, 2, 3])




# 86. functools.partial 사용 - partial을 사용하여 함수의 일부 인자를 고정하여 새로운 함수 생성.
#안좋은 예:
def multiply(x, y):
    return x * y
multiply_by_2 = lambda x: multiply(x, 2)
#좋은 예:



from functools import partial
multiply_by_2 = partial(multiply, y=2)




### 88. filter 함수 사용 - filter를 사용하여 조건에 맞는 값을 필터링.
#안좋은 예:
result = []
for num in numbers:
    if num > 0:
        result.append(num)

#좋은 예:
result = list(filter(lambda x: x > 0, numbers))



### 89. os.path.join 사용 - os.path.join()을 사용하여 운영 체제에 맞는 경로 구분자를 자동으로 처리.
#안좋은 예:
path = "folder" + "/" + "file.txt"

#좋은 예:
import os
path = os.path.join("folder", "file.txt")



### 90. 주석 및 문서화 - 문서화 문자열을 사용하여 함수에 대한 설명을 추가.
#안좋은 예:
def add(x, y):
    return x + y  # Adds x and y

#좋은 예:
def add(x, y):
    """
    Adds two numbers.
    
    Args:
        x (int): The first number.
        y (int): The second number.
        
    Returns:
        int: The sum of x and y.
    """
    return x + y