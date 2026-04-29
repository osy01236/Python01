# 컴프리헨션 연습


# ============================================================
# 리스트 컴프리헨션 기본 형태
# ============================================================
# 리스트 컴프리헨션은 반복문으로 리스트를 만드는 코드를 짧게 쓰는 방법이다.
#
# 기본 형태:
# [표현식 for 변수 in 반복대상]
#
# 조건이 있는 형태:
# [표현식 for 변수 in 반복대상 if 조건식]


# ============================================================
# 문제 1
# 1부터 10까지 숫자 중에서 짝수만 리스트에 저장하세요.
# ============================================================

# 일반 반복문 풀이
result1 = []

for i in range(1, 11):
    if i % 2 == 0:
        result1.append(i)

print("문제 1 일반 반복문:", result1)


# 컴프리헨션 풀이
result1_comprehension = [i for i in range(1, 11) if i % 2 == 0]

print("문제 1 컴프리헨션:", result1_comprehension)

result1_C = [i for i in range(1, 11) if i % 2 == 0]


# ============================================================
# 문제 2
# prices 리스트에서 5000원 이상인 가격만 골라서 리스트에 저장하세요.
# ============================================================

prices = [3200, 7800, 12000, 4500, 9900, 2500]

# 일반 반복문 풀이
result2 = []

for price in prices:
    if price >= 5000:
        result2.append(price)

print("문제 2 일반 반복문:", result2)


# 컴프리헨션 풀이
result2_comprehension = [price for price in prices if price >= 5000]

print("문제 2 컴프리헨션:", result2_comprehension)


# ============================================================
# 문제 3
# names 리스트에서 이름이 3글자인 사람만 리스트에 저장하세요.
# ============================================================

names = ["이순신", "김유신", "정약용", "장보고", "세종", "율곡"]

# 일반 반복문 풀이
result3 = []

for name in names:
    if len(name) == 3:
        result3.append(name)

print("문제 3 일반 반복문:", result3)


# 컴프리헨션 풀이
result3_comprehension = [name for name in names if len(name) == 3]

print("문제 3 컴프리헨션:", result3_comprehension)


# ============================================================
# 추가 정리
# ============================================================
# 일반 반복문:
# result = []
# for 변수 in 반복대상:
#     if 조건식:
#         result.append(저장할값)
#
# 컴프리헨션:
# result = [저장할값 for 변수 in 반복대상 if 조건식]

# 연습 1
# 1부터 20까지 숫자 중에서 3의 배수만 저장
practice1 = []

for i in range(1, 21):
    if i % 3 == 0:
        practice1.append(i)

print("연습 1 일반 반복문:", practice1)

# practice1_comprehension =
# print("연습 1 컴프리헨션:", practice1_comprehension)

practice1_comprehension = [ i for i in range(1,21) if i % 3 == 0]

print("문제1 : ", practice1_comprehension)



# 연습 2
# 1부터 10까지 숫자의 제곱을 저장
practice2 = []

for i in range(1, 11):
    practice2.append(i * i)

print("연습 2 일반 반복문:", practice2)

# practice2_comprehension =
# print("연습 2 컴프리헨션:", practice2_comprehension)

practice2_comprehension = [i * i for i in range(1,11)]

print("문제2",practice2_comprehension)

# 연습 3
# scores 리스트에서 80점 이상만 저장
scores = [65, 90, 72, 88, 100, 45, 79]
practice3 = []

for score in scores:
    if score >= 80:
        practice3.append(score)

print("연습 3 일반 반복문:", practice3)

# practice3_comprehension =
# print("연습 3 컴프리헨션:", practice3_comprehension)

practice3_comprehension =[score for score in scores if score >= 80 ]

# 연습 4
# fruits 리스트에서 글자 수가 2글자인 과일만 저장
fruits = ["사과", "바나나", "포도", "복숭아", "귤", "수박"]
practice4 = []

for fruit in fruits:
    if len(fruit) == 2:
        practice4.append(fruit)

print("연습 4 일반 반복문:", practice4)

# practice4_comprehension =
# print("연습 4 컴프리헨션:", practice4_comprehension)


practice4_comprehension= [fruit for fruit in fruits if len(fruit) ==2]
print("문제4 : ", practice4_comprehension)





# 연습 5
# prices 리스트에서 1000원을 할인한 가격을 저장
prices2 = [5000, 12000, 8000, 3000, 15000]
practice5 = []

for price in prices2:
    practice5.append(price - 1000)

print("연습 5 일반 반복문:", practice5)

# practice5_comprehension =
# print("연습 5 컴프리헨션:", practice5_comprehension)

practice5_comprehension = [price - 1000 for price in prices2 ]


# ============================================================
# 추가 연습 6~8
# 아래 일반 반복문 3개를 컴프리헨션으로 바꿔보세요.
# ============================================================


# 연습 6
# 1부터 15까지 숫자 중에서 홀수만 저장
practice6 = []

for i in range(1, 16):
    if i % 2 == 1:
        practice6.append(i)

print("연습 6 일반 반복문:", practice6)

# practice6_comprehension =
# print("연습 6 컴프리헨션:", practice6_comprehension)


# 연습 7
# words 리스트에서 글자 수를 저장
words = ["python", "java", "html", "css", "javascript"]
practice7 = []

for word in words:
    practice7.append(len(word))

print("연습 7 일반 반복문:", practice7)

# practice7_comprehension =
# print("연습 7 컴프리헨션:", practice7_comprehension)


# 연습 8
# scores2 리스트에서 60점 이상은 "합격", 60점 미만은 "불합격"으로 저장
scores2 = [95, 40, 73, 58, 80, 100]
practice8 = []

for score in scores2:
    if score >= 60:
        practice8.append("합격")
    else:
        practice8.append("불합격")

print("연습 8 일반 반복문:", practice8)

# practice8_comprehension =
# print("연습 8 컴프리헨션:", practice8_comprehension)


practice8_comprehension = ["합격" if score >= 60 else "불합격" for score in scores2]

# ============================================================
# 추가 연습 9~11
# if~else가 들어가는 컴프리헨션으로 바꿔보세요.
# 형태: [참일때값 if 조건식 else 거짓일때값 for 변수 in 반복대상]
# ============================================================


# 연습 9
# nums4 리스트에서 짝수는 "짝수", 홀수는 "홀수"로 저장
nums4 = [3, 8, 11, 20, 7, 16]
practice9 = []

for num in nums4:
    if num % 2 == 0:
        practice9.append("짝수")
    else:
        practice9.append("홀수")

print("연습 9 일반 반복문:", practice9)

# practice9_comprehension =
# print("연습 9 컴프리헨션:", practice9_comprehension)


practice9_comprehension = ["짝수" if num % 2 == 0 else "홀수" for num in nums4]
print("연습 9 일반 반복문:", practice9_comprehension)


# 연습 10
# ages 리스트에서 20살 이상은 "성인", 20살 미만은 "미성년자"로 저장
ages = [15, 22, 19, 31, 8, 20]
practice10 = []

for age in ages:
    if age >= 20:
        practice10.append("성인")
    else:
        practice10.append("미성년자")

print("연습 10 일반 반복문:", practice10)

# practice10_comprehension =
# print("연습 10 컴프리헨션:", practice10_comprehension)


practice10_comprehension = ["성인" if age >=20 else "미성년자" for age in ages]
print("연습 10 일반 반복문:", practice10_comprehension)


# 연습 11
# prices3 리스트에서 10000원 이상은 "고가", 10000원 미만은 "저가"로 저장
prices3 = [5000, 12000, 9900, 20000, 7500, 15000]
practice11 = []

for price in prices3:
    if price >= 10000:
        practice11.append("고가")
    else:
        practice11.append("저가")

print("연습 11 일반 반복문:", practice11)

# practice11_comprehension =
# print("연습 11 컴프리헨션:", practice11_comprehension)


practice11_comprehension= ["고가" if price >= 10000 else "저가" for price in prices3]
print("연습 11 일반 반복문:", practice11_comprehension)

# ============================================================
# 추가 연습 12~14
# if~else가 들어가는 컴프리헨션으로 바꿔보세요.
# 형태: [참일때값 if 조건식 else 거짓일때값 for 변수 in 반복대상]
# ============================================================


# 연습 12
# temperatures 리스트에서 30도 이상은 "더움", 30도 미만은 "보통"으로 저장
temperatures = [28, 31, 35, 22, 30, 26]
practice12 = []

for temp in temperatures:
    if temp >= 30:
        practice12.append("더움")
    else:
        practice12.append("보통")

print("연습 12 일반 반복문:", practice12)

# practice12_comprehension =
# print("연습 12 컴프리헨션:", practice12_comprehension)

practice12_comprehension= ["더움" if temp >= 30 else "보통" for temp in temperatures]


# 연습 13
# numbers 리스트에서 0 이상은 "양수", 0 미만은 "음수"로 저장
numbers = [10, -3, 0, 7, -12, 5]
practice13 = []

for number in numbers:
    if number >= 0:
        practice13.append("양수")
    else:
        practice13.append("음수")

print("연습 13 일반 반복문:", practice13)

# practice13_comprehension =
# print("연습 13 컴프리헨션:", practice13_comprehension)



# 연습 14
# stocks 리스트에서 재고가 1개 이상이면 "판매가능", 0개면 "품절"로 저장
stocks = [5, 0, 12, 3, 0, 8]
practice14 = []

for stock in stocks:
    if stock >= 1:
        practice14.append("판매가능")
    else:
        practice14.append("품절")

print("연습 14 일반 반복문:", practice14)

# practice14_comprehension =
# print("연습 14 컴프리헨션:", practice14_comprehension)
