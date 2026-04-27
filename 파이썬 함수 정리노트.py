# 파이썬 함수 정리노트


# ============================================================
# 1. 함수란?
# ============================================================
# 함수는 자주 사용하는 코드를 이름 붙여서 묶어 놓은 것이다.
# 필요할 때 함수 이름을 호출하면 안에 있는 코드가 실행된다.
#
# 함수를 사용하는 이유
# - 같은 코드를 반복해서 쓰지 않아도 된다.
# - 코드가 짧고 보기 좋아진다.
# - 기능별로 나누어 관리하기 쉽다.


def hello():
    print("안녕하세요")


hello()
hello()


# ============================================================
# 2. 함수 기본 형태
# ============================================================
# def 함수이름():
#     실행할 코드


def print_line():
    print("====================")


print_line()
print("메뉴")
print_line()


# ============================================================
# 3. 매개변수
# ============================================================
# 매개변수는 함수가 실행될 때 외부에서 값을 받는 변수이다.


def greet(name):
    print(name, "님 안녕하세요")


greet("이순신")
greet("김춘추")


# 매개변수는 여러 개 사용할 수 있다.


def add(a, b):
    print(a + b)


add(10, 20)
add(3, 7)


# ============================================================
# 4. return
# ============================================================
# return은 함수의 결과값을 함수 밖으로 돌려주는 명령어이다.
# print는 화면에 출력만 하고, return은 값을 돌려준다.


def add2(a, b):
    return a + b


result = add2(10, 20)
print(result)


# return으로 받은 값은 다른 계산에 다시 사용할 수 있다.


def get_total(price, count):
    return price * count


total = get_total(3000, 5)
print("총금액:", total, "원")


# ============================================================
# 5. return과 함수 종료
# ============================================================
# 함수는 return을 만나면 값을 돌려주고 바로 종료된다.
# return 아래에 있는 코드는 실행되지 않는다.


def check_age(age):
    if age >= 20:
        return "성인"

    return "미성년자"


print(check_age(25))
print(check_age(17))


# ============================================================
# 6. 기본값 매개변수
# ============================================================
# 매개변수에 기본값을 정해두면 값을 넣지 않았을 때 기본값이 사용된다.


def introduce(name, age=20):
    print("이름:", name)
    print("나이:", age)


introduce("이순신", 30)
introduce("김춘추")


# 기본값이 있는 매개변수는 뒤쪽에 적는 것이 원칙이다.
# def test(a=10, b):  # 오류
#     pass


# ============================================================
# 7. 키워드 인자
# ============================================================
# 함수를 호출할 때 매개변수 이름을 직접 지정해서 값을 넣을 수 있다.
# 이 방식을 사용하면 순서가 바뀌어도 정확하게 전달된다.


def print_member(name, age, city):
    print(name, age, city)


print_member("이순신", 20, "대전")
print_member(city="서울", name="김유신", age=30)


# ============================================================
# 8. 가변 인자 *args
# ============================================================
# 몇 개의 값이 들어올지 모를 때 *args를 사용한다.
# args는 튜플 형태로 값을 받는다.


def print_numbers(*args):
    print(args)

    for number in args:
        print(number)


print_numbers(1, 2, 3)
print_numbers(10, 20, 30, 40, 50)


def sum_numbers(*args):
    total = 0

    for number in args:
        total += number

    return total


print(sum_numbers(1, 2, 3))
print(sum_numbers(10, 20, 30, 40))


# ============================================================
# 9. 가변 키워드 인자 **kwargs
# ============================================================
# key=value 형태로 여러 값을 받을 때 **kwargs를 사용한다.
# kwargs는 딕셔너리 형태로 값을 받는다.


def print_info(**kwargs):
    print(kwargs)

    for key, value in kwargs.items():
        print(key, value)


print_info(name="이순신", age=20, job="군인")
print_info(item="사과", price=3000, stock=20)


# ============================================================
# 10. 지역 변수와 전역 변수
# ============================================================
# 함수 안에서 만든 변수는 함수 안에서만 사용할 수 있다.
# 이것을 지역 변수라고 한다.


def local_test():
    message = "함수 안에서 만든 변수"
    print(message)


local_test()
# print(message)  # 오류: 함수 밖에서는 message를 사용할 수 없다.


# 함수 밖에서 만든 변수는 전역 변수라고 한다.

count = 10


def global_test():
    print(count)


global_test()


# 전역 변수 값을 함수 안에서 수정하려면 global을 사용할 수 있다.
# 하지만 전역 변수 수정은 코드가 복잡해질 수 있으므로 꼭 필요할 때만 사용한다.

num = 0


def increase():
    global num
    num += 1


increase()
increase()
print(num)


# ============================================================
# 11. 함수 안에서 리스트, 딕셔너리 사용하기
# ============================================================


def print_fruits(fruits):
    for fruit in fruits:
        print(fruit["name"], fruit["price"], "원")


fruit_list = [
    {"name": "사과", "price": 3000, "stock": 20},
    {"name": "바나나", "price": 1500, "stock": 30},
    {"name": "포도", "price": 5000, "stock": 11},
]

print_fruits(fruit_list)


def find_fruit(fruits, keyword):
    result = []

    for fruit in fruits:
        if keyword in fruit["name"]:
            result.append(fruit)

    return result


search_result = find_fruit(fruit_list, "사")
print(search_result)


# ============================================================
# 12. 람다 함수
# ============================================================
# lambda는 이름 없는 짧은 함수를 만들 때 사용한다.
# 간단한 계산이나 정렬 기준을 만들 때 자주 사용한다.


add3 = lambda a, b: a + b
print(add3(10, 20))


students = [
    {"name": "이순신", "score": 89},
    {"name": "김춘추", "score": 75},
    {"name": "장영실", "score": 95},
]

sorted_students = sorted(students, key=lambda student: student["score"])
print(sorted_students)


# ============================================================
# 13. 함수 작성 연습 예시
# ============================================================


def is_even(number):
    if number % 2 == 0:
        return True

    return False


print(is_even(10))
print(is_even(7))


def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"

    return "F"


print(get_grade(95))
print(get_grade(82))
print(get_grade(58))


def sell_item(item, count):
    if item["stock"] >= count:
        item["stock"] -= count
        return item["price"] * count

    return 0


apple = {"name": "사과", "price": 3000, "stock": 20}
sale_price = sell_item(apple, 3)

print("판매 금액:", sale_price)
print("남은 재고:", apple["stock"])


# ============================================================
# 14. 함수 정리
# ============================================================
# def
# - 함수를 만들 때 사용한다.

# 매개변수
# - 함수가 외부에서 받는 값이다.

# 인자
# - 함수를 호출할 때 실제로 넣는 값이다.

# return
# - 함수의 결과값을 밖으로 돌려준다.
# - return을 만나면 함수는 종료된다.

# 기본값 매개변수
# - 값을 넣지 않았을 때 사용할 기본값을 정해둔다.

# *args
# - 여러 개의 값을 튜플로 받는다.

# **kwargs
# - key=value 형태의 여러 값을 딕셔너리로 받는다.

# 지역 변수
# - 함수 안에서 만든 변수이다.
# - 함수 밖에서는 사용할 수 없다.

# 전역 변수
# - 함수 밖에서 만든 변수이다.
# - 함수 안에서 읽을 수 있다.
