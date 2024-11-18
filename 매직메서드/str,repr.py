import datetime
a = datetime.datetime(2017, 9, 27)
print(str(a)) # 2017-09-27 00:00:00
print(repr(a)) # datetime.datetime(2017, 9, 27, 0, 0) 
# datetime 객체를 repr()로 생성한 문자열에 다시 eval() 함수를 실행하면 datetime 객체가 만들어진다. 문자열로 객체를 생성할 때는 eval() 함수를 사용