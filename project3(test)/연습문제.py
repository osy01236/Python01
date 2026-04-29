"""
문제 1. project3/main.py를 만들고 print("project3 시작")을 출력하세요.


문제 2.project3/util/calc.py를 만들고 add(a, b) 함수를 작성하세요.
main.py에서 import 해서 10 + 20 결과를 출력하세요.


문제 3. calc.py에 minus(a, b), multi(a, b), divide(a, b) 함수를 추가하세요.
main.py에서 네 가지 계산 결과를 모두 출력하세요.


문제 4. project3/util/text.py를 만들고 hello(name) 함수를 작성하세요.
"홍길동님 안녕하세요" 형태로 반환하게 하세요.


문제 5. main.py에서 사용자에게 이름을 입력받고, text.py의 hello() 함수를 사용해 인사말을 출력하세요.


문제 6. project3/service/member_service.py를 만들고 get_member() 함수를 작성하세요.
함수는 "gold"라는 아이디를 반환하게 하세요.


문제 7. main.py에서 member_service를 import 해서 get_member() 결과를 출력하세요.


문제 8. member_service.py에 login(id, pw) 함수를 작성하세요.
id가 "gold"이고 pw가 "1234"이면 "로그인 성공", 아니면 "로그인 실패"를 반환하세요.


문제 9. main.py에서 사용자에게 아이디와 비밀번호를 입력받고, login() 함수를 사용해 로그인 결과를 출력하세요.


문제 10. project3/data/db.py를 만들고 find_by_id(id) 함수를 작성하세요.
id가 "gold"이면 ("gold", "1234")를 반환하고, 아니면 (None, None)을 반환하세요.


문제 11. member_service.py의 login() 함수가 직접 "gold"를 비교하지 말고, db.py의 find_by_id()를 사용하도록 수정하세요.


문제 12. project3/auth/valid.py를 만들고 id_check(id) 함수를 작성하세요.
아이디 길이가 4글자 이상이면 True, 아니면 False를 반환하세요.


문제 13. valid.py에 pw_check(pw) 함수를 추가하세요.
비밀번호 길이가 6글자 이상이면 True, 아니면 False를 반환하세요.


문제 14. member_service.py의 login()에서 로그인 전에 id_check(), pw_check()를 사용하세요.
길이 조건이 맞지 않으면 "아이디 또는 비밀번호 길이가 올바르지 않습니다"를 반환하세요.


문제 15. main.py에서 while문을 사용해서 로그인을 반복하세요.
로그인 성공하면 반복 종료, 실패하면 다시 입력받게 하세요.


추가 도전 문제

문제 16. db.py에 회원 정보를 딕셔너리로 저장하세요.
members = {
    "gold": "123456",
    "admin": "111111",
    "test": "222222"
}
find_by_id(id)는 딕셔너리에서 회원을 찾아 반환하게 만드세요.


문제 17. project3/service/sign_service.py를 만들고 sign_up(id, pw) 함수를 작성하세요.
이미 있는 아이디면 "이미 존재하는 아이디입니다"를 반환하고, 없으면 회원을 추가하세요.


문제 18. 회원가입할 때도 valid.py의 id_check(), pw_check()를 사용하세요.


문제 19. main.py에서 메뉴를 만드세요.

1. 로그인
2. 회원가입
3. 종료
번호를 입력받아 각각 기능이 실행되게 하세요.


문제 20. 회원가입한 아이디로 바로 로그인할 수 있게 만드세요.
단, 회원 정보는 db.py의 딕셔너리에 저장하세요.




"""