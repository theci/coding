


# 어떤 클래스(타입)의 객체가 있을 때 '( )'를 붙여주면 해당 클래스에 정의된 매직 메소드인 __call__이 호출됩니다. 
class MyFunc:
    def __call__(self, *args, **kwargs):
        print("호출됨")


f = MyFunc()
f() # 호출됨

# 변수가 어떤 객체를 바인딩하고 있을 때 점(.)을 찍으면 클래스의 __getattribute__ 라는 이름의 매직 메소드를 호출해줍니다.
class Stock:
    def __getattribute__(self, item):
        print(item, "객체에 접근하셨습니다.")


s = Stock()
print(s.data) # data 객체에 접근하셨습니다.

