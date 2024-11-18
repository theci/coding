### 1. Pythonic한 클래스 정의 - property를 사용하여 area를 속성처럼 사용할 수 있게 했습니다. 이렇게 하면 area() 메서드를 속성처럼 접근할 수 있어 읽기 전용 속성으로 만들 수 있습니다.
#안좋은 예:
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

#좋은 예:
import math

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    @property
    def area(self) -> float:
        return math.pi * self.radius  2



### 2. 매직 메서드 (__str__, __repr__, __eq__) 활용 - __str__와 __repr__를 적절히 정의하여 객체의 가독성을 높이고, __eq__를 오버라이드하여 객체 비교를 Pythonic하게 처리합니다.
#안좋은 예:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
#좋은 예:
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Point):
            return (self.x, self.y) == (other.x, other.y)
        return NotImplemented



### 3. 상속과 super() 활용 - super()를 사용하여 부모 클래스의 메서드를 호출하고, 확장성을 더 높였습니다. 자식 클래스에서 부모 클래스의 기능을 확장할 때 유용합니다.
#안좋은 예:
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

dog = Dog()
dog.speak()

#좋은 예:
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Bark")

dog = Dog()
dog.speak()


### 4. 코루틴 (Coroutine) 및 async/await 사용 - async/await를 사용하여 비동기 코드를 작성하고, 코루틴을 사용해 병렬성을 구현합니다.
#안좋은 예:
import time

def fetch_data():
    time.sleep(2)
    return "Data"

def main():
    data = fetch_data()
    print(data)

main()

#좋은 예:
import asyncio

async def fetch_data():
    await asyncio.sleep(2)
    return "Data"

async def main():
    data = await fetch_data()
    print(data)

asyncio.run(main())

### 5. 클로저 (Closure) - 클로저를 사용하여 함수를 반환하는 함수가 외부 변수에 접근하도록 합니다. 이를 통해 상태 캡슐화와 유연성을 제공합니다.
#안좋은 예:
def outer():
    x = 10
    def inner():
        return x
    return inner

closure = outer()
print(closure())

#좋은 예:
def make_multiplier(factor: int):
    def multiplier(number: int) -> int:
        return number * factor
    return multiplier

double = make_multiplier(2)
print(double(5))  # 10


### 6. Enum 활용 - Enum을 사용하여 상태 값을 의미 있는 이름으로 처리하고, 값 비교를 더 명확하게 만듭니다.
#안좋은 예:
class Status:
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3

status = Status.PENDING
#좋은 예:



from enum import Enum

class Status(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3

status = Status.PENDING




### 7. 다형성 (Polymorphism) -- 추상 클래스를 활용해 다형성을 더 잘 표현하고, 인터페이스처럼 행동할 수 있게 만듭니다. 이를 통해 유연한 설계가 가능합니다.
#안좋은 예:
class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

def make_sound(animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)

#좋은 예:
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

def make_sound(animal: Animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)


### 8. 객체 지향적 접근법을 통한 캡슐화 - 캡슐화를 통해 내부 상태(예: _fuel)를 외부에서 직접 접근하지 못하도록 숨깁니다.
#안좋은 예:
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        self._fuel = 100

    def drive(self):
        if self._fuel > 0:
            self._fuel -= 1
            print(f"Driving {self.model}...")
        else:
            print("Out of fuel!")

car = Car("Tesla", 2022)
car.drive()
print(car._fuel)

#좋은 예:
class Car:
    def __init__(self, model: str, year: int):
        self.model = model
        self.year = year
        self._fuel = 100

    def _consume_fuel(self):
        if self._fuel > 0:
            self._fuel -= 1

    def drive(self):
        if self._fuel > 0:
            self._consume_fuel()
            print(f"Driving {self.model}...")
        else:
            print("Out of fuel!")

    def refuel(self, amount: int):
        self._fuel += amount

car = Car("Tesla", 2022)
car.drive()
print(car._fuel)  # Using encapsulation; ideally, _fuel should not be accessed directly

### 9. 상속과 메서드 오버라이딩을 통한 코드 재사용 - 상속을 활용하여 공통적인 기능을 부모 클래스에서 정의하고, 오버라이딩을 통해 자식 클래스에서 구체적인 동작을 정의합니다.
#안좋은 예:
class Animal:
    def speak(self):
        print("Some generic sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

#좋은 예:
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

def make_animal_speak(animal: Animal):
    animal.speak()

make_animal_speak(Dog())  # Bark
make_animal_speak(Cat())  # Meow



### 10. staticmethod 및 classmethod 사용 - @staticmethod와 @classmethod를 사용하여 클래스나 인스턴스와 관련된 메서드를 구분하여 구현합니다.
#안좋은 예:
class MyClass:
    def __init__(self, value):
        self.value = value
    
    def my_method(self, x):
        return self.value + x

    @staticmethod
    def static_method(x):
        return x * 2

    @classmethod
    def class_method(cls, x):
        return cls(x)

#좋은 예:
class MyClass:
    def __init__(self, value: int):
        self.value = value

    def my_method(self, x: int) -> int:
        return self.value + x

    @staticmethod
    def static_method(x: int) -> int:
        return x * 2

    @classmethod
    def class_method(cls, x: int):
        return cls(x)





### 11. __slots__ 사용 (메모리 절약 및 속도 향상) - __slots__를 사용하면 객체가 가질 수 있는 속성을 제한할 수 있고, 메모리 사용을 절약할 수 있습니다. 또한 속성을 동적으로 추가할 수 없도록 강제할 수 있습니다.
#안좋은 예:
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

a = Animal("Lion", "Mammal")
a.age = 5  # 동적으로 속성 추가 가능

#좋은 예:
class Animal:
    __slots__ = ['name', 'species']  # 속성을 제한

    def __init__(self, name, species):
        self.name = name
        self.species = species

a = Animal("Lion", "Mammal")
# a.age = 5  # Error: 'Animal' object has no attribute 'age'



### 12. 상속에서 super()와 다중 상속 처리 - 다중 상속에서 super()를 적절히 사용하여 메서드의 호출 순서를 제어합니다. 메서드 해석 순서(MRO)를 고려해서 부모 클래스들을 호출하는 것이 중요합니다.
#안좋은 예:
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")

class C(A):
    def method(self):
        print("C method")

class D(B, C):
    def method(self):
        print("D method")

d = D()
d.method()  # "D method"

#좋은 예:
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        super().method()
        print("B method")

class C(A):
    def method(self):
        super().method()
        print("C method")

class D(B, C):
    def method(self):
        super().method()
        print("D method")

d = D()
d.method()  # "A method", "C method", "B method", "D method"

### 13. abc 모듈을 사용한 추상 클래스 구현 - 추상 클래스(ABC)와 추상 메서드(abstractmethod)를 사용하여 서브클래스가 반드시 구현해야 할 메서드를 정의하고 강제합니다.
#안좋은 예:
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method")

class Circle(Shape):
    def area(self):
        return 3.14 * self.radius  2
    
#좋은 예:
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius  2



###  14. __call__을 통한 객체를 함수처럼 호출 - __call__을 정의하여 객체를 마치 함수처럼 호출할 수 있습니다. 이를 통해 객체의 행동을 동적으로 변경하거나 간결하게 만들 수 있습니다.
#안좋은 예:
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

counter = Counter()
print(counter.increment())  # 1
print(counter.increment())  # 2

#좋은 예:
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count

counter = Counter()
print(counter())  # 1
print(counter())  # 2

### 15. dataclasses를 이용한 데이터 모델 정의 - @dataclass 데코레이터를 사용하여 클래스를 더 간결하게 작성하고, 기본적인 메서드(예: __init__, __repr__, __eq__)가 자동으로 생성되게 합니다.
#안좋은 예:
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity
    
#좋은 예:
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def total_price(self) -> float:
        return self.price * self.quantity

### 16. @property와 @setter를 활용한 속성 제어 - @property와 @setter를 사용하여 외부에서 접근할 수 있는 속성을 제어하면서도 객체의 내부 구현을 캡슐화합니다.
#안좋은 예:



class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, value):
        self.width = value

    def set_height(self, value):
        self.height = value
#좋은 예:



class Rectangle:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    @property
    def area(self) -> float:
        return self._width * self._height




### 17. 고급 이터레이터 사용 (Iterator, Generator) - 이터레이터를 사용하여 메모리 효율적인 방식으로 객체를 순회할 수 있도록 처리합니다. 이 경우 __iter__와 __next__를 구현하여 제너레이터처럼 동작할 수 있습니다.
#안좋은 예:



class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_numbers(self):
        numbers = []
        for num in range(self.start, self.end):
            numbers.append(num)
        return numbers
#좋은 예:



class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        self.start += 1
        return self.start - 1

my_range = MyRange(1, 5)
for number in my_range:
    print(number)

### 18. asyncio와 Task 활용한 동시성 - asyncio를 사용하여 비동기적으로 여러 작업을 동시에 처리합니다. await를 활용하여 실행 흐름을 제어합니다.
#안좋은 예:
import time

def task1():
    time.sleep(2)
    return "Task 1 completed"

def task2():
    time.sleep(3)
    return "Task 2 completed"

print(task1())
print(task2())

#좋은 예:
import asyncio

async def task1():
    await asyncio.sleep(2)
    return "Task 1 completed"

async def task2():
    await asyncio.sleep(3)
    return "Task 2 completed"

async def main():
    result1 = await task1()
    result2 = await task2()
    print(result1)
    print(result2)

asyncio.run(main())

### 19. typing을 활용한 타입 힌팅 - 타입 힌팅을 사용하여 함수의 입력과 출력 타입을 명시적으로 정의함으로써 코드의 안정성 및 가독성을 높입니다.
#안좋은 예:
def add(a, b):
    return a + b

#좋은 예:
from typing import Union

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

### 20. functools의 lru_cache 활용 - lru_cache를 사용하여 재귀 함수의 계산 결과를 캐시하고 성능을 향상시킵니다.
#안좋은 예:
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))

#좋은 예:
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))




### 21. contextlib의 contextmanager 활용 - contextmanager 데코레이터를 사용하여 코드가 더 간결해지고, 리소스 관리가 자동화됩니다.
#안좋은 예:
class FileOpener:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileOpener("file.txt") as file:
    content = file.read()
#좋은 예:
from contextlib import contextmanager

@contextmanager
def open_file(filename):
    f = open(filename, 'r')
    try:
        yield f
    finally:
        f.close()

with open_file("file.txt") as file:
    content = file.read()




### 22. itertools.chain으로 여러 이터러블 결합하기 - itertools.chain을 사용하여 여러 이터러블을 효율적으로 결합할 수 있습니다.
#안좋은 예:
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = []
for l in lists:
    result.extend(l)
#좋은 예:
import itertools

lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = list(itertools.chain(*lists))




### 23. namedtuple을 이용한 명확한 데이터 구조 - namedtuple을 사용하면 불변 객체로 명확한 이름을 가진 데이터 구조를 만들 수 있습니다.
#안좋은 예:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
#좋은 예:
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)




### 24. 람다와 map을 사용한 함수형 프로그래밍 - map을 사용하여 코드가 더 간결하고 효율적으로 변환 작업을 처리합니다.
#안좋은 예:
def square(numbers):
    return [n * n for n in numbers]

numbers = [1, 2, 3, 4]
squares = square(numbers)
#좋은 예:
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))




### 25. functools.reduce 사용 - reduce를 사용하여 반복적인 집합 작업을 간결하게 표현할 수 있습니다.
#안좋은 예:
numbers = [1, 2, 3, 4, 5]
result = 1
for number in numbers:
    result *= number
#좋은 예:
from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)




### 26. __del__을 이용한 객체 소멸자 정의 - __del__을 사용하여 객체가 소멸될 때 자원을 자동으로 해제할 수 있습니다.
#안좋은 예:
class FileReader:
    def __init__(self, filename):
        self.file = open(filename, 'r')
    
    def close(self):
        self.file.close()

reader = FileReader("file.txt")
reader.close()
#좋은 예:
class FileReader:
    def __init__(self, filename):
        self.file = open(filename, 'r')

    def __del__(self):
        self.file.close()

reader = FileReader("file.txt")
# 객체가 소멸될 때 자동으로 close가 호출됩니다.



### 27. with 구문을 사용한 파일 읽기 - with 구문을 사용하여 파일을 자동으로 열고 닫을 수 있어 리소스 관리를 효율적으로 처리합니다.
#안좋은 예:
file = open("file.txt", "r")
content = file.read()
file.close()
#좋은 예:
with open("file.txt", "r") as file:
    content = file.read()




### 28. asyncio.gather로 여러 비동기 작업 동시 실행 - asyncio.gather를 사용하면 여러 비동기 작업을 동시에 실행할 수 있습니다.
#안좋은 예:
import asyncio

async def task1():
    await asyncio.sleep(2)
    return "Task 1 completed"

async def task2():
    await asyncio.sleep(3)
    return "Task 2 completed"

async def main():
    result1 = await task1()
    result2 = await task2()
    print(result1)
    print(result2)

asyncio.run(main())
#좋은 예:
import asyncio

async def task1():
    await asyncio.sleep(2)
    return "Task 1 completed"

async def task2():
    await asyncio.sleep(3)
    return "Task 2 completed"

async def main():
    results = await asyncio.gather(task1(), task2())
    print(results[0])
    print(results[1])

asyncio.run(main())




### 29. deque를 사용한 큐(Queue) 처리 - deque를 사용하면 큐 연산(enqueue, dequeue)이 더 효율적입니다.
#안좋은 예:
queue = []
queue.append(1)
queue.append(2)
queue.append(3)
queue.pop(0)
#좋은 예:
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()  # O(1)으로 빠른 큐 연산



### 30. is 연산자로 객체의 동일성 비교 - is 연산자는 객체가 동일한 객체인지 확인할 때 사용됩니다. 이는 값 비교가 아닌 객체 비교에 유용합니다.
#안좋은 예:
a = [1, 2, 3]
b = [1, 2, 3]
if a == b:
    print("Equal")
#좋은 예:
a = [1, 2, 3]
b = a
if a is b:
    print("Same object")


### 31. itertools.combinations를 사용한 조합 생성 - itertools.combinations을 사용하여 조합을 간단하게 생성합니다.
#안좋은 예:
pairs = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        pairs.append((lst[i], lst[j]))
#좋은 예:
import itertools

pairs = list(itertools.combinations(lst, 2))




### 32. 다양한 조건을 하나의 표현식으로 처리하기 - in을 사용하여 조건을 간결하게 표현합니다.
#안좋은 예:
def check_value(value):
    if value == "a":
        return True
    elif value == "b":
        return True
    elif value == "c":
        return True
    else:
        return False
#좋은 예:
def check_value(value):
    return value in ("a", "b", "c")



### 33. collections.Counter를 이용한 요소 빈도 계산 - Counter를 사용하여 간단하고 효율적으로 각 요소의 빈도를 계산할 수 있습니다.
#안좋은 예:
numbers = [1, 2, 2, 3, 3, 3, 4]
counts = {}
for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
#좋은 예:
from collections import Counter

numbers = [1, 2, 2, 3, 3, 3, 4]
counts = Counter(numbers)



### 34. collections.defaultdict로 기본값 설정 - defaultdict를 사용하면 기본값을 설정하여 코드를 간결하게 만듭니다.
#안좋은 예:
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
#좋은 예:
from collections import defaultdict

d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)




### 35. assert를 사용한 간단한 조건 검사 - assert를 사용하여 조건을 간결하게 검사하고, 디버깅 시 유용하게 활용합니다.
#안좋은 예:
if not isinstance(value, int):
    raise TypeError("Value must be an integer")
#좋은 예:
assert isinstance(value, int), "Value must be an integer"



### 36. functools.partial로 부분 적용 함수 만들기 - partial을 사용하여 함수를 부분적으로 적용하여 더 간결하게 표현할 수 있습니다.
#안좋은 예:
def multiply(x, y):
    return x * y

double = lambda x: multiply(2, x)
triple = lambda x: multiply(3, x)
#좋은 예:
from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
triple = partial(multiply, 3)




### 37. min과 max에 key 인자 사용 - key 인자를 사용하면 더 효율적으로 특정 조건에 맞는 최솟값/최댓값을 찾을 수 있습니다.
#안좋은 예:
numbers = [(1, 'a'), (2, 'b'), (3, 'c')]
max_num = max(numbers, key=lambda x: x[0])
#좋은 예:
numbers = [(1, 'a'), (2, 'b'), (3, 'c')]
max_num = max(numbers, key=lambda x: x[0])




### 39. 함수형 프로그래밍 스타일로 filter와 map 사용 - filter와 map을 사용하여 함수형 스타일로 처리합니다.
#안좋은 예:
numbers = [1, 2, 3, 4, 5]
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
#좋은 예:
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))




### 40. super() 활용하여 다형성 구현 - super()를 사용하여 부모 클래스의 메서드를 명확하게 호출하면서 다형성을 유지합니다.
#안좋은 예:
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

dog = Dog()
dog.sound()

#좋은 예:
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        super().sound()  # 부모 클래스의 sound 호출
        print("Bark")

dog = Dog()
dog.sound()