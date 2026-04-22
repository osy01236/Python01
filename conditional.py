
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
# import random

# user = input("입력 : ")
# com = random.choice(["가위","바위","보"])
# print("컴퓨터 : ", com)

# if user == com :
#     print("비겼습니다.")
# elif user == "가위" and com =="보" :
#     print("이겼습니다.")
# elif user == "바위" and com =="가위":
#     print("이겼습니다.")
# elif user == "보" and com =="바위":
#     print("이겼습니다.")
# else:
#     print("졌습니다.")
#=====================================================

#문자열 바꾸기 .replace("현재문자열에서 변경 할 문자열", "교체할문자열")

# word= "찬용이는 진섭이보다 지금이 좋다고 한다"
# word = word.replace("찬용이","성현이")
# print( word )

# #문자열 나누기 - 배열
# text = "도헌-지연-동렬-진섭"
# result =text.split("-")
# print(result)


# 배열을 하나의 문자열로 합치기
# text = ",".join(result) #배열값 하나하나에, 를 넣어서 하나의 문자열 만들기
# print(text)

# #숫자인지 아닌지 확인
# text = "12345" 
# print( text.isdigit() )#문자열을 숫자로 변환하기전에 확인하는 용도 True  , False 로 표현

# #문자 종류 확인
# text1 = "tomato"
# text2 = "  "
# text3 = "4월20일"
# print ( text1.isalpha()) #문자만 있는지  True  , False 로 표현
# print ( text2.isspace()) #공백만 있는지  True  , False 로 표현
# print ( text3.isalnum()) #문자+숫자인지  True  , False 로 표현

# #문자열 정렬
# text = "15"
# print (text.zfill(6)) #함수()안에 자릿수 넣기
# print ( text.rjust(4))
# print ( text.ljust(5))

#문제1 . - 공백제거와 소문자 변환을하려면?
#input으로 입력받아서 공백제거와 소문자 변환을 하세요.

# word = input("입력 : ")

# # print(word.strip().lower()) 

# result = word.strip().lower()

# print(result)

#================================================= 
#문제2 "행복,우울,기쁨,슬픔,화남" 
# 위 문자열을 나누어 보세요.

# text = "행복,우울,기쁨,슬픔,화남" 
# result = text.split(",")
# print(result)

#문제3. 회원가입시 이메일 입력을 하는데 특정 주소만 가능하다.
# naver.com , gmail.com , nate.com , daum.net
#위 4개만 가능하다
#input 으로 이메일을 받아서 가입 가능인지 불가능인지 출력


# email =  input("이메일 입력 : ").strip().lower()

# if email.endswith("naver.com"):
#     print("가입 가능")
# elif email.find("gmail.com"):
#     print("가입 가능")
# elif email.split("@")[1]=="nate.com":
#     print("가입가능")
# elif email.endswith("daum.net"):
#     print("가입가능")
# else :
#     print("가입 불가능")


# if 'naver.com'in email :
#     print("가입 가능")
# elif 'gmail.com' in email:
#     print("가입 가능")
# elif 'nate.com' in email:
#     print("가입가능")
# elif 'daum.net' in email:
#     print("가입가능")
# else :
#     print("가입 불가능")

#문제4. 금액 계산하기
#각 업체별 입금이 되었다. 총액이 얼마인지 출력하세요.

쿠팡 = "135,900원"
네이버 = "540,000원"
오드론 = "2,340,090원"

num= int(쿠팡.replace(",","").replace("원",""))
num2=int(네이버.replace(",","").replace("원",""))
num3=int(오드론.replace(",","").replace("원",""))
num4= num + num2 + num3

print("총금액 : ",str(num4))
print(f"총금액 :{num4:,}원")