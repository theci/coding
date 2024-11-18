from abc import ABCMeta, abstractmethod

# 추상 클래스는 이를 상속받은 자식 클래스가 부모 클래스의 특정 메서드를 구현하도록 강제하는 클래스이다
class Bird(metaclass=ABCMeta):
    # 구현을 강제해야 하는 fly() 메서드의 데코레이터로 abc 모듈의 abstractmethod를 지정하자.
    @abstractmethod
    def fly(self):
        pass


class Eagle(Bird):
    def fly(self):
        # pass # 에러남. 반드시 구현해줘야 한다.
        print("very fast")


eagle = Eagle()
eagle.fly()