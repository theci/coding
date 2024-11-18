from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    married: bool = False


user1 = User("홍길동", 33, True)
user2 = User("홍길동", 33, True)

print(user1)
print(user1 == user2)

### 참고
# dataclass를 frozen=True로 설정하면 User 클래스로 생성한 객체의 속성을 변경할 수 없게 된다. 
@dataclass(frozen=True)
class User:
    name: str
    age: int
    married: bool = False
