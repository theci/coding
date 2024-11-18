# 디폴트 인자의 초기화가 함수가 호출될 때마다 일어나는 것이 아니라 함수 정의 시점에 일어나는 이유는 파이썬의 성능과 효율성 때문입니다. 
# 디폴트 인자는 매번 함수가 호출될 때마다 새로 평가되면 비효율적일 수 있기 때문에, 한 번만 평가하고 이후에는 그 값을 재사용하는 방식으로 설계되어 있습니다.


# 문제점
def say_shopping_cart(cart: list = []):
    if "apple" not in cart:
        print("사과는 꼭 사야하니 추가합니다.")
        cart.append("apple")

    print(cart)    # 쇼핑카트 출력


# 첫 호출
say_shopping_cart() # '사과는 꼭 사야하니 추가합니다.' ['apple']

# 재호출시 초기화를 바랬지만 같은 객체를 가리키고 있다.
say_shopping_cart() # ['apple']



### 해결법
def say_shopping_cart(cart: list = None):
    if cart is None:
        cart = []  # cart가 None일 때만 빈 리스트를 새로 생성

    if "apple" not in cart:
        print("사과는 꼭 사야하니 추가합니다.")
        cart.append("apple")

    print(cart)