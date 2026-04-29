
# =========================
# 1. 딕셔너리 문제 3개
# =========================

# 문제 1
# student = {"name":"민수", "age":17, "grade":2}
# 위 딕셔너리를 만들고 이름과 나이를 출력해보세요.
student = dict()
student["name"]="민수"
student["age"]=17
student["grade"]=2
print(student)


# 문제 2
# 위 student 딕셔너리에 "school": "대전고" 를 추가한 뒤
# 전체 딕셔너리를 출력해보세요.
student["school"]="대전고"
print(student)


# 문제 3
# student 딕셔너리에 "age" 키가 있으면 나이를 출력하고,
# 없으면 "나이 정보 없음" 을 출력해보세요.

if "age" in student :
    print(student["age"])
else:
    print("나이 정보없음")

# =========================
# 2. 리스트 컴프리헨션 문제 3개
# =========================

# 문제 4
# 1부터 10까지 숫자 중 짝수만 담은 리스트를
# 컴프리헨션으로 만들어 출력해보세요.
num = [i*2 for i in range(1,6)]
print(num)


# 문제 5
nums = [1, 2, 3, 4, 5]
# 위 리스트를 이용해서 각 값의 제곱으로 이루어진
# 새 리스트를 컴프리헨션으로 만들어보세요.
result = [i ** 2 for i in nums]
print(result)


# 문제 6
price = [3000, 7000, 4500, 9000]
# 5000원 이하면 "저가", 초과면 "고가" 로 분류한
# 새 리스트를 컴프리헨션으로 만들어보세요.
results= ["저가" if p<=5000 else "고가" for p in price]
print(results)


# =========================
# 3. set 문제 3개
# =========================

# 문제 7
fruits = ["사과", "바나나", "사과", "포도", "바나나"]
# 위 리스트를 set으로 바꿔서 중복을 제거해보세요.
set =set(fruits)
print(set)


# 문제 8
a = {"사과", "배", "포도"}
b = {"배", "딸기", "포도"}
# a와 b의 교집합을 구해보세요.
print(a & b)


# 문제 9
# 위 a, b를 이용해서
# 1) 합집합
# 2) 차집합
# 을 각각 구해보세요.
print(a|b)
print(a-b)


# =========================
# 4. 프로그램 응용 문제 3개
# =========================

fruits = [
    {"name": "사과", "price": 3000, "stock": 20},
    {"name": "바나나", "price": 1500, "stock": 30},
    {"name": "포도", "price": 5000, "stock": 11},
    {"name": "복숭아", "price": 4000, "stock": 8},
    {"name": "수박", "price": 9900, "stock": 34},
]


# 문제 10
# fruits에서 재고가 10개 이하인 과일만 출력해보세요.
for fruit in fruits:
    if fruit["stock"]<= 10:
        print(fruit["name"], fruit["stock"])


# 문제 11
# 사용자가 과일 이름을 입력하면
# 그 과일의 가격과 재고를 출력해보세요.
user= input("과일 이름 : ")
for fruit in fruits :
    if fruit["name"] == user:
        print(fruit["price"], fruit["stock"])


# 문제 12
# 사용자가 과일 이름을 입력했을 때,
# 그 과일이 있으면 stock을 1 감소시키고
# 변경된 결과를 출력해보세요.

user= input("과일이름 : ")
for fruit in fruits:
    if fruit["name"]==user:
        fruit["stock"] -= 1
        print(fruit)