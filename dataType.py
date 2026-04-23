# #리스트 ,튜플
# #리스트 - 여러 데이터를 저장 관리 하기 위 한 파이선 자료 구조이다.
# #튜플도 리스트와 같은데 차이점은 리스트는 수정이 가능하지만 
# # 튜플은 수정이 불가능하다.

# #리스트 - 순서 유지, 인덱스를 통해 접근 , 추가 , 수정 , 삭제 기능
# # 다른 자료형도 저장가능
# number =[ 10 ,20 ,30 ,40 ,50 ]
# empty = []
# name = list()

# print( number[0])
# print( number[-2]) # 40 나옴

# #리스트 자르기
# num = number[2:4]
# print(num)
# num2 = number[:3]
# print(num2)
# num3 = number[2:]
# print(num3)

# #리스트 수정
# number[2] = 100
# print (number)

# #리스트 추가
# number.append(60) #리스트의 마지막에 추가
# print(number)

# number.insert(2,500) #  리스트에 원하는 위치에 추가 (인덱스, 값)
# print(number)

# #리스트 값 삭제
# number.remove(100) # 리스트에서 삭제 할 데이터 입력 존재하지 않는 값을 지운다고하면 오류!!!
# print(number)
# number.pop(1) #리스트에서 삭제할 데이터의 인덱스 입력
# print(number)
# del number[2] #인덱스로 삭제   존재하지 않는 인덱스를 삭제할경우 오류!!
# print (number)

# #리스트 크기 (길이)
# print(len(number))

# for num in number : 
#     print (num)

# for i , num in enumerate(number):
#     print(i , num )

# #리스트 검색
# print (40 in number) # 값의 존재 여부 True, False
# print ( number.index(50)) #인덱스 찾기 - 없으면 오류
# #index를통해 인덱스를 찾기 전에 in으로 존재 여부 확인  먼저 하기

# #리스트 정렬 sort
# number.sort()
# print(number)
# number.sort(reverse=True)
# print(number)

#리스트는 일반적으로 많이 사용되는 자료 구조이다.
#자바에서 List (ArrayList)를 많이 사용된다면 파이썬은 리스트이다.
#여러데이터를 저장할 수 있고, 수정, 추가 가능하고 반복문 사용 쉽고 
# 정렬, 검색도 되고 그래서 사용하기 좋은 녀석이다.

#리스트 문제 풀기 !!!!!
#문제 1 5명의 이름이 저장되어 있는 리스트 만들기
# 5명의 이름 출력하는 반복문 만들기

# List = ["페이커","오너","도란","케리아","페이즈"]
# print(type(List))
# for list in List:
#     print(list)

# #문제 2 정도전 이름을 추가하고 출력하세요.
# List.append("정도전")  #원하는 위치 추가는 insert
# print(List)    

# #문제 3. 리스트에 김유신이 있는지 확인하는 코드 작성하기
# if "김유신" in List:
#     print("있음")
# else :
#     print("없음")

# #문제4 이름 리스트에 출력하세요.
# List.sort(reverse=True)
# print(List)

# #문제5 과일의 이름이 두글자인 과일만 출력하세요.

# fruits = ["사과" , "바나나" , "파인애플" , "딸기" , "오렌지" , "포도" , "배"]

# for f in fruits :
#     if len(f) == 2:
#         print(f)
    
# fruits.sort(key=len, reverse=True)
#print(fruits)    

#문제6 과일 검색 프로그래 만들기
# 과일 이름 키보드를 통해 입력받는다.
#입력한 과일이 리스트에 있다면 판매중, 없다면 품절이라고 출력
# user = input("검색 : ").strip()

# # for f in fruits :
# #     if user == f :
# #         print("판매중")
# #         break
# # else:
# #     print("품절")

# if user in fruits:
#     print("판매중")
# else:
#     print("품절")

#문제 7 구매 하고자 하는 과일 을 입력 하면 총 지불 금액 얼마인지 출력
# 단, 과일은 1개를 구매할 수 도 있고 여러개 구매할 수 도 있다.
# fruits = ["사과" , "바나나" , "파인애플" , "딸기" , "오렌지" , "포도" , "배"]
# fruits.sort #딸기, 바나나,배 ,사과, 오렌지, 파인애플, 포도
# price = [5000, 8000, 12000, 9500, 15500, 20400, 9000]

# user = input("입력 : ").split()

# total=0

# for f in user:
#     if f in fruits:
#         idx = fruits.index(f)
#         total += price[idx]
# print("총 금액 : ", total)    
   
#튜플 - 리스트처럼 여러 데이터를 저장 할수 있는 자료형이다.
# 저장한 데이터를 수정 할 수 없다.
# 데이터를 보호 하기 위한 목적
# 속도와 메모리 효율성
# 딕셔너리 키로 사용
# 여러개의 값을 반환(return) 시킬때

#튜플 만들기
number =(10, 20, 30, 40) #작은 괄호 - 튜플 , 대괄호 - 리스트
print(number)
print( type((1,2,3,4)))
print( type((10,)))

print( number[1] ) #인덱스 0 부터 시작

number[0] = 100

#튜플 슬라이싱 (자르기)
print(number[1:3])

#튜플 검색 
print( 10 in number)
print(number.index(20))

#리스트와 다른점
# 수정 불가
# number.append(200) 오류
# number.remove(20) 오류
# number.pop(20(오류
# del number[2] 

print(number.count(20))#특정값 갯수 구하기

Data = 10,20, 30, 40, 50 #패킹 여러값을 하나로 묶기
print(type(data))

a,b,c,d,e = data #언패킹- 묶여있는 값을 여러개로 나누기
print(a,b,c,d,e)

red=20
blue=10
red, blue = blue,red
print(red, blue)

#함수 반환 여러개 
def get():
    return 10,20,30,40


#리스트 <--> 튜플
info = ("다음주","금요일","빨간날","그래서","우리는","5월6일","봐요")

info[0]="이번주"

info_list = list(info) #튜플 -> 리스트 변환
info_list[0]="이번주"

info = tuple(info_list) # 리스트 -> 리스트 변환
print(info)