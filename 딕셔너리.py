name = ['merona', 'gugucon']
price = [500, 1000]

icecream = dict(zip(name, price))
print(icecream) # {'merona': 500, 'gugucon': 1000}



# setdefault 메서드
data = {}

ret = data.setdefault('a', 0)    # key로 'a'를 추가학 value 0을 설정함, setdefault는 현재 value 값을 리턴
print(ret, data) # 0 {'a': 0}

ret = data.setdefault('a', 1)   # 이미 key가 있는 경우 setdefault 현재 value 값을 리턴
print(ret, data) # 0 {'a': 0}

# 딕셔너리 컴프리헨션
name = ['merona', 'gugucon', 'bibibig']
price = [500, 1000, 600]

icecream = {k:v for k, v in zip(name, price) if v < 1000}
print(icecream) # {'merona': 500, 'bibibig': 600}