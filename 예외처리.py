try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)


class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다." 
    
def say_nick(nick):
    if nick == '바보':
        raise MyError() # 일부러 오류를 발생시키기 위해 사용
    print(nick)

say_nick("천사") # 천사
say_nick("바보") # MyError: 허용되지 않는 별명입니다