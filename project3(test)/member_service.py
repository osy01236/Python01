def get_member():
    return "gold"


def get_id(id):
     return id == "gold"

def get_pw(pw):
    return pw =="1234"


from data.db import find_by_id

def login(id, pw):
    db_id, db_pw = find_by_id(id)

    if db_id == id and db_pw == pw:
        return "로그인 성공"
    else:
        return "로그인 실패"