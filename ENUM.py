# 문제점 : 가독성이 떨어짐
from datetime import date

def get_menu(input_date):
    weekday = input_date.isoweekday()  # 1:월요일, 2:화요일, ... , 7: 일요일
    if weekday == 1:
        menu = "김치찌개"
    elif weekday == 2:
        menu = "비빔밥"
    elif weekday == 3:
        menu = "된장찌개"
    elif weekday == 4:
        menu = "불고기"
    elif weekday == 5:
        menu = "갈비탕"
    elif weekday == 6:
        menu = "라면"
    elif weekday == 7:
        menu = "건빵"
    return menu


print(get_menu(date(2021, 12, 6))) # 김치찌개
print(get_menu(date(2021, 12, 18))) # 라면



### 해결법
from datetime import date
from enum import IntEnum

# 숫자를 바로 사용하지 않고 Enum 자료형을 만들어 상수로 사용하면 유지보수에 유리하며 가독성도 좋아진다.
class Week(IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def get_menu(input_date):
    menu = {
        Week.MONDAY: "김치찌개",
        Week.TUESDAY: "비빔밥",
        Week.WEDNESDAY: "된장찌개",
        Week.THURSDAY: "불고기",
        Week.FRIDAY: "갈비탕",
        Week.SATURDAY: "라면",
        Week.SUNDAY: "건빵",
    }
    return menu[input_date.isoweekday()]


print(get_menu(date(2021, 12, 6))) # 김치찌개
print(get_menu(date(2021, 12, 18))) # 라면

# name과 value를 통해 속성 접근 가능
print(Week.MONDAY.name) # MONDAY
print(Week.MONDAY.value) # 1

# 반복문 가능
for week in Week:
    print("{}:{}".format(week.name, week.value))