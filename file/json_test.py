
import json

info = [{
    "name" : "김유신",
    "age" : 35,
    "addr" : "경주"
},
{
    "name" : "이순신",
    "age" : 50,
    "addr" : "여수"
}

]

with open("file/info.json", "w", encoding="utf-8 ") as f:
    json.dump(info , f , ensure_ascii=False, indent=3)



# #json 읽기 - 하나만 있을경우엔 이 방법으로 가능
# with open("file/info.json", "r" , encoding="utf-8") as f:
#     member = json.load(f)

# print(member["name"])

with open("file/info.json", "r" , encoding="utf-8") as f:
    member = json.load(f)

for user in member:
    print(user["name"], user["age"])

#Json 은 추가 모드 "a" 를 사용하지 않는다.

member.append({"name":"문익점","age":44,"addr":"개경"})

with open("file/info.json", "w", encoding="utf-8") as f:
    json.dump(member , f, ensure_ascii=False, indent=3)


"""
파이썬과 json
dict - object
list - array
str - string
ont, float - number
True - true
False - false
None -null



"""