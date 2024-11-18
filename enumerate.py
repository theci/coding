# enumerate는 for 루프를 사용하기 위한 인터페이스를 지원하지 않는다
# 문제점 - 인덱스를 추적하는 번거로움

# 기존 방식: 인덱스 추적을 수동으로 해야 함
fruits = ['apple', 'banana', 'cherry']

index = 0  # 인덱스를 수동으로 초기화
for fruit in fruits:
    print(f"Index: {index}, Fruit: {fruit}")
    index += 1  # 인덱스를 수동으로 증가시켜야 함



# 해결법 - enumerate() 함수 사용

# enumerate를 사용한 방식
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# start 매개변수를 사용하여 인덱스를 1부터 시작
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits, start=1):
    print(f"Index: {index}, Fruit: {fruit}")


