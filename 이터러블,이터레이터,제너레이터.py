# Iterable 객체란? : __iter__(). 객체 안에 있는 원소(element)를 하나씩 반환 가능한 객체
# Iterator 객체란? : __next__(), 내장 함수인 next()를 부르면서, 원소(element)를 순차적으로 반환 할 수 있는 객체
# 제너레이터(Generator)란? : 일반 함수 return과 다른 yield는 해당 함수(generator)가 종료하지 않고, 그대로 유지됩니다. 

(x**2 for x in range(10)) 