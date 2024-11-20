### 문제점 - 딕셔너리로 이와 같은 집계용 코드를 작성할 때는 항상 초깃값에 신경 써야 한다. 

text = "Life is too short, You need python."

d = dict()
for c in text:
    if c not in d: # 방어적인 코드
        d[c] = 0
    d[c] += 1

print(d) # {'L': 1, 'i': 2, 'f': 1, 'e': 3, ' ': 6, 's': 2, 't': 3, 'o': 5, 'h': 2, 'r': 1, ',': 1, 'Y': 1, 'u': 1, 'n': 2, 'd': 1, 'p': 1, 'y': 1, '.': 1}


### 해결법
# collections의 defaultdict를 사용하면 이러한 번거로움을 피할 수 있다. 
# int를 기준으로 생성한 딕셔너리 d의 값은 항상 0으로 자동 초기화되므로 초기화를 위한 별도의 코드가 필요 없다.
from collections import defaultdict

text = "Life is too short, You need python."

d = defaultdict(int)
for c in text:
    d[c] += 1

print(dict(d))


