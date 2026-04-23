# 문제 1. 다음 리스트에서 "바나나"를 출력하는 코드를 작성하시오.

# fruits = ["사과", "바나나", "포도", "딸기"]
# print(fruits[1])

# # 문제 2. 다음 리스트의 마지막 값을 출력하는 코드를 작성하시오.

# numbers = [10, 20, 30, 40, 50]
# print(numbers[-1])
# # 문제 3. 다음 리스트에 60을 추가한 뒤 전체 리스트를 출력하시오.

# numbers = [10, 20, 30, 40, 50]
# numbers.append(60)
# print(numbers)

# # 문제 4. 다음 리스트에서 "포도"를 "수박"으로 변경한 뒤 출력하시오.

# fruits = ["사과", "바나나", "포도", "딸기"]
# fruits[2]="수박"
# print(fruits)
# # 문제 5. 다음 리스트의 모든 요소의 합을 구하여 출력하시오.

# scores = [80, 75, 90, 100, 65]
# total= 0
# for sc in scores:
#     total += sc
# print(total)    
# # 문제 6. 다음 튜플에서 두 번째 값을 출력하는 코드를 작성하시오.

# colors = ("red", "green", "blue", "yellow")
# print(colors[1])

# # 문제 7. 다음 튜플의 길이를 구하여 출력하시오.

# animals = ("강아지", "고양이", "토끼", "햄스터")
# print(len(animals))

# # 문제 8. 다음 튜플을 리스트로 변환한 뒤 "토끼"를 추가하고 다시 출력하시오.

# pets = ("강아지", "고양이")

# info_list = list(pets)
# info_list.append("토끼")
# print(info_list)

# # 문제 9. 사용자에게 과일 이름 여러 개를 입력받아 리스트로 저장한 뒤,
# # 입력한 과일 개수를 출력하시오.
# # 예시 입력:

# # 사과 바나나 포도 딸기
# user = input("입력 : ").split()
# print(len(user))

# # 문제 10. 다음 리스트에서 짝수만 골라 새로운 리스트로 만들어 출력하시오.

# nums = [3, 8, 11, 20, 25, 30, 41]
# even = []

# for n in nums:
#     if n % 2 == 0 :
#         even.append(n)
# print(even)

# #문제 11 다음 리스트에서 "딸기"의 인덱스 번호를 출력하시오.

# fruits = ["사과", "바나나", "포도", "딸기", "오렌지"]
# print( fruits.index("딸기"))


# #문제 12 다음 리스트에서 30을 삭제한 뒤 전체 리스트를 출력하시오.

# numbers = [10, 20, 30, 40, 50]
# del numbers[2]
# print(numbers)



# #문제 13 다음 튜플에 들어있는 값들을 하나씩 출력하시오.

# colors = ("red", "green", "blue")
# print(colors[0],colors[1],colors[2])



# #문제 14 사용자에게 숫자 3개를 입력받아 리스트로 저장한 뒤, 그중 가장 큰 값을 출력하시오.
# #예시 입력: 10 25 7
# user = input("입력 : ").split()

# numbers = []
# numbers.append(int(user[0]))
# numbers.append(int(user[1]))
# numbers.append(int(user[2]))

# print(max(numbers))


# #문제 15 다음 리스트의 값을 거꾸로 출력하시오.
# nums = [1, 2, 3, 4, 5]

# nums.sort(reverse=True)
# print(nums)


#문제 16 사용자에게 과일 이름 3개를 입력받아 리스트에 저장한 뒤,
#그 리스트의 첫 번째 값과 마지막 값을 출력하시오. 사과 바나나 포도

user = input("입력 : ").split()
print(user[0], user[-1])
