#staticmethod
class hello:
    num = 10

    @staticmethod
    def calc(x):
        return x + 10

print(hello.calc(10)) # 20


#classmethod
class hello:
    num = 10

    @classmethod
    def calc(cls, x):
        return x + 10

print(hello.calc(10)) # 20