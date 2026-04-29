
# print("project3 시작")

# from calc import add
# print( add(10,20) )

# from text import hello
# name = input("입력 : ")
# print(hello(name))

# from member_service import get_member
# print(get_member())

# from member_service import get_id
# from member_service import get_pw

# id=input("아이디 입력 : ")
# pw=input("비밀번호 입력 : ")

# if get_id(id) and get_pw(pw):
#     print("로그인 성공")
# else:
#     print("로그인 실패")

from member_service import login

id = input("아이디 입력 : ")
pw = input("비밀번호 입력 : ")

print(login(id, pw))