##### 1. Single Responsibility Principle (단일 책임 원칙)
# 한 클래스가 너무 많은 일을 담당하면 코드가 복잡해지고 유지보수가 어려워집니다.
# 클래스는 하나의 목적을 가지고, 그 목적에 맞는 기능만 수행해야 합니다.

# 잘못된 예시 (단일 책임 원칙 위반)
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def save_to_database(self):
        # DB에 저장하는 코드
        pass

    def send_email(self):
        # 이메일 보내는 코드
        pass

# 해결책: User 클래스의 책임을 분리
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class UserDatabase:
    def save(self, user):
        # DB에 저장하는 코드
        pass

class EmailService:
    def send(self, user):
        # 이메일 보내는 코드
        pass


# 2. Open/Closed Principle (개방/폐쇄 원칙)
# 기능을 확장할 때 기존의 코드를 수정해야 한다면, 기존 코드에서 버그가 발생할 위험이 커집니다.
# 기존 코드는 닫혀 있고, 확장만 가능합니다.

# 잘못된 예시 (개방/폐쇄 원칙 위반)
class TaxCalculator:
    def calculate_tax(self, income, country):
        if country == "US":
            return income * 0.1
        elif country == "UK":
            return income * 0.2
        # 새로운 국가를 추가하려면 이 메소드를 수정해야 함

# 해결책: 다형성을 이용하여 확장
class TaxCalculator:
    def calculate_tax(self, income, tax_strategy):
        return tax_strategy.calculate_tax(income)

class USTax:
    def calculate_tax(self, income):
        return income * 0.1

class UKTax:
    def calculate_tax(self, income):
        return income * 0.2


##### 3. Liskov Substitution Principle (리스코프 치환 원칙)
# 부모 클래스에서 정의한 계약을 서브클래스가 위반하면, 코드가 예상치 못한 동작을 할 수 있습니다.
# 자식 클래스는 부모 클래스의 모든 기능을 충족해야 하며, 부모 클래스에서 정의된 동작을 변경하지 않아야 합니다.

# 잘못된 예시 (리스코프 치환 원칙 위반)
class Bird:
    def fly(self):
        print("Flying")

class Ostrich(Bird):  # 타조는 날지 않음
    def fly(self):  # 날지 않으므로 이 메소드를 덮어쓰는 것이 잘못됨
        raise Exception("Can't fly")

# 해결책: 메소드의 동작을 적절하게 설계
class Bird:
    def move(self):
        pass

class Sparrow(Bird):
    def move(self):
        print("Flying")

class Ostrich(Bird):
    def move(self):
        print("Running")


# 4. Interface Segregation Principle (인터페이스 분리 원칙)
# 하나의 큰 인터페이스를 사용하면, 클라이언트 클래스가 필요하지 않은 메소드를 구현해야 할 수 있습니다.
# 각 클래스는 필요한 메소드만 구현하고, 불필요한 메소드를 구현하지 않아도 됩니다.

# 잘못된 예시 (인터페이스 분리 원칙 위반)
class Machine:
    def print(self):
        pass

    def scan(self):
        pass

    def fax(self):
        pass

class OldPrinter(Machine):
    def print(self):
        pass

    def scan(self):
        pass

    def fax(self):
        raise NotImplementedError("Fax not supported")  # 필요 없는 기능을 구현하지 않으면 안 됨

# 해결책: 인터페이스를 분리
class Printer:
    def print(self):
        pass

class Scanner:
    def scan(self):
        pass

class Fax:
    def fax(self):
        pass

class OldPrinter(Printer, Scanner):
    def print(self):
        pass

    def scan(self):
        pass



# 5. Dependency Inversion Principle (의존성 역전 원칙)
# 하위 모듈이 상위 모듈에 의존하면, 상위 모듈이 변경되면 하위 모듈도 변경되어야 합니다.
# 상위 모듈이 하위 모듈에 의존하는 것이 아니라, 추상화된 인터페이스나 추상 클래스에 의존하게 됩니다.

# 잘못된 예시 (의존성 역전 원칙 위반)
class LightBulb:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class Switch:
    def __init__(self, bulb):
        self.bulb = bulb

    def operate(self):
        self.bulb.turn_on()  # Switch는 직접적으로 LightBulb에 의존

# 해결책: 의존성 역전 원칙 적용
class Switchable:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class Switch:
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self):
        self.device.turn_on()  # Switch는 Switchable 인터페이스에 의존
