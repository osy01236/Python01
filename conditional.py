
#if 조건식 : 
#    실행할 커드

# num  = 10
# if num > 5 :
#     print("크다")
#     print("10이 크다")
# elif num < 5:
#     print("같다")
#     print("5랑 같다")
# else: 
#     print("작다") 
#     print("5보다 작다")   

# 변수 apple의 값이 10이상이라면 1봉지 8000원 이라고 출력
# apple의 값이 10미만 이라면 개당 2000원 출력

# apple = int(input("입력 : "))
# if apple >= 10 :
#     print("1봉지 8000원")
# else :
#     print("개당 2000원")    

#자바의 switch 유사한 python 의 match
# res =2
# match res:
#     case 0 : 
#         print("종료")
#     case 1 :
#         print("시작")
    
# like 좋아요 변수의 값이 100이상이면 spot 등록 출력
# 좋아요 변수의 값이 10이하라면 관심 spot 출력

# like = int(input("좋아요 : "))    
# if like >=100 : 
#     print("spot 등록")
# elif like <= 10 :
#     print("관심 spot")            
# else :
#     print("관심직전")

# 아이디 와 비밀번호를 입력받아 일치하면 로그인 성공 불일치하면 
# 아이디 또는 비밀번호가 잘못되었습니다. 출력
# #아이디는 진섭

# id= '진섭' 
# pw= 'babo'

# if id == input("id:") and pw == input("pw:"):
#     print("로그인 성공")
# else :
#     print("아이디 또는 비밀번호가 잘못되었습니다.")
    
#파이썬에서 문자열 포함 여부 확인하는 방법
# word ="나는 김진섭 입니다." 
# if  '김진섭' in word :
#     print("있다")
# else :
    # print("없다")

# word = "나는 진섭이가 짝궁일때 별로 였다."

# # word 안에 동렬 이름이 없다라는 것을 확인할수 있는 코드 만드세요.

# if '동렬' not in word :
#     print("없다.")

# startswith() 함수 시작 문자열 비교
# word = "차도헌님께서 입장하셨습니다."
# if word.startswith('이창호') :
#     print("신원 확인")
# else:
#     print("이창호님이 아닙니다.")
# #대소문자 변환
# word = " i like banana"
# print (word.upper()) #대문자
# print (word.lower()) #소문자
# print (word.title()) #대문자 - 단어의  첫글자만

# #공백 제거 - 개발시 필요필수 (이거때문에 오류나면 골치 아픔)
# word =" banana "
# print (word) #공백 제거 없이
# print(word.strip()) #양쪽 공백 제거
# print(word.lstrip())#왼쪽 공백 제거
# print(word.rstrip())#오른쪽 공백 제거

# #찾기
# word= "찬용이는 진섭이보다 지금이 좋다고 한다"
# print (word.find("진섭")) #있다면 위치 반환(인덱스) 없으면 -1
# print (word.index("동렬")) #인덱스 반환, 없으면 에러


# ====================================================
# id= 'osy01236'
# pw= 'qqqwww'

# if id == input("id:") and pw == input("pw:"):
#      print("로그인 성공")
# else :
#      print("아이디 또는 비밀번호가 잘못되었습니다.")

#=====================================================

# word= "오늘은 21일 화요일 입니다."

# print(word.find(input("입력 : ")))

# if input("입력 : ") in word :
#     print("확인완료")
# else : 
#     print("해당사항없음")

#===================================================== 
import random

user = input("입력 : ")
com = random.choice(["가위","바위","보"])
print("컴퓨터 : ", com)

if user == com :
    print("비겼습니다.")
elif user == "가위" and com =="보" :
    print("이겼습니다.")
elif user == "바위" and com =="가위":
    print("이겼습니다.")
elif user == "보" and com =="바위":
    print("이겼습니다.")
else:
    print("졌습니다.")