from auth import valid as _v
from data import db as _db

def sign_in_process(id, pw):
    if not _v.len_check(id, pw) :
        print( "아이디 또는 비밀번호 길이가 올바르지 않습니다." )
    else :
        uid, upw = _db.find_by_id(id)

        if uid == id and upw == pw:
            print( "로그인 성공")
        else:
            print("아이디 또는 비밀번호가 일치하지 않습니다.")