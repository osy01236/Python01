# import calc 
# import calc as c


# print(calc.add(10,20))  

# print(c.add(10,20))  #as 를 했을경우

#특정 함수나 변수를 사용하고자  한다면 아래와 같이 하면된다.
#import 파일명
#import 파일명 as 별명
#from 파일명 ㅑimport 함수명(변수명),   함수명

# from calc import add

#모든 파일인 util 폴더밑에 있는 calc 가져오기
# from util import calc

#특정 함수 가져오기
from util.calc import add , avg
from service import user_serivce as us


print(add(10,20))
print(avg([1,2,3,4,5]))

print( us.get_user_id)
print( us.login_id) # 모듈 파일의 변수 가져오기
#모듈 파일으 ㅣ전역 변수는 모듈 파일내부에서는 전역 변수이다.
#import 해준 파일에서는 전역 변수가 아니다.


us.login_id = 2
print(us.login_id)

from service.user_serivce import login_id
print(login_id)
login_id = 200 #user_serivce 의 변수값 수정아니고 main1.py





#모듈로 사용되는 파일에서는 함수정의 , 전역 변수 정의
# 이외 다른 코드는 작성하지 않는게 좋다.
#import 모듈을 가져오면 해당 모듈파일의 코드가 실행된다.



"""
project2 라는 폴더 생성  main.py ->메인 파일
하위 폴더 만들기
member_service 폴더생성
data 폴더 생성

member_service.login.py 생성
login.py

-> def login_process(id, pw :)
입력한 아이디와 비밀번호를 검증하는 함수이다.   (id : gold , pw:123456)

data.db.py 생성
db.py
-> conn = "db연결 성공"
    def find_by_id(id):
데이터베이스에서 id로 조회하는 함수 , id 와 pw 반환

"""
