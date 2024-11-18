# 순열 - 서로 다른 n 개 중 r 개를 골라 순서를 정해 나열하는 가짓수
import itertools

arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2)
print(list(nPr)) # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# 조합 - 조합은 순서를 고려하지 않는다

arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr)) # [('A', 'B'), ('A', 'C'), ('B', 'C')]


### 값이 주어졌을 때 합이 125인 조합 찾기
import itertools

# 숫자와 그에 해당하는 값들
data = {
    "Cadillac": 87,
    "DS": 33,
    "Ford": 13,
    "Jaguar": 22,
    "Jeep": 19,
    "Land Rover": 18,
    "Lexus": 68,
    "Mini": 0,
    "Nissan": 99,
    "RR": 49
}

# 숫자들만 리스트로 추출
values = list(data.values())
names = list(data.keys())

# 목표 합
target = 125

# 가능한 모든 조합을 찾기
for r in range(1, len(values) + 1):
    for comb in itertools.combinations(enumerate(values), r):
        indices, comb_values = zip(*comb)
        if sum(comb_values) == target:
            result = [names[i] for i in indices]
            print(f"합이 {target}인 조합: {result}")
            break



# zip - 동일한 개수로 이루어진 iterable한 객체들을 인수로 받아 묶어서 iterator로 반환
z = zip([1, 2, 3], ('A', 'B', 'C'))
print(next(z)) # (1, 'A')
print(next(z)) # (2, 'B')
print(next(z)) # (3, 'C')

# all - iterable한 객체를 인수로 받아서 원소가 모두 참이면 True, 아니면 False를 반환
a = all([1, 2, 3]) # True
a = all([0, 1, 2]) # False

# any - iterable한 객체를 인수로 받아서 원소가 하나라도 참이면 True, 아니면 False를 반환
a = any([0, 1, 2]) # True
a = any([0, False, []]) # False
            
# chain - iterable한 객체들을 인수로 받아 하나의 iterator로 반환
c1 = [1, 2]
ca = ['A', 'B']
c = itertools.chain(c1, ca)
print(next(c)) # 1
print(next(c)) # 2
print(next(c)) # A
print(next(c)) # B