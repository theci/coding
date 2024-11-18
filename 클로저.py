def outer(num):
    def inner():
        print(num)
    return inner


class Outer:
    def __init__(self, num):
        self.num = num
    def __call__(self):
        print(self.num)