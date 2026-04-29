# dataType2.py 학습 내용 정리 노트
# 제외: 과일 재고 관리 프로그램, 연습문제


# ============================================================
# 1. 딕셔너리(dict)
# ============================================================
# 딕셔너리는 데이터를 key:value 형태로 저장하는 자료형이다.
# key를 이용해서 value를 꺼내기 때문에 데이터의 의미를 알기 쉽다.

info = {
    "name": "이순신",
    "age": 20,
    "job": "군인",
}

print(info["name"])       # key로 값 가져오기
print(info.get("city"))   # 없는 key를 조회해도 오류가 나지 않고 None 반환


# 딕셔너리에 값 추가 또는 수정
info["city"] = "대전"
info["age"] = 21
print(info)


# 딕셔너리 값 삭제
city = info.pop("city")   # 삭제하면서 값을 반환
print(city)

del info["age"]           # key를 이용해서 삭제
print(info)


# key 존재 여부 확인
if "name" in info:
    print("이름 정보가 있습니다.")


# value 존재 여부 확인
if "이순신" in info.values():
    print("이순신이 있습니다.")


# 딕셔너리 반복
for key, value in info.items():
    print(key, value)


# 딕셔너리에서 자주 사용하는 기능
# dict.keys()   : key만 가져오기
# dict.values() : value만 가져오기
# dict.items()  : key와 value를 쌍으로 가져오기


# 딕셔너리는 이런 데이터를 저장할 때 많이 사용한다.
# - 로그인 회원 정보
# - 상품 정보
# - 게시글 하나의 정보
# - 설정값
# - JSON 데이터
# - API 응답 데이터


# 딕셔너리 key로 사용할 수 있는 자료형
# - 문자열
# - 정수
# - 실수
# - 튜플
sample = {
    "id": 4000,
    1: "정수 key",
    3.14: "실수 key",
    ("x", "y"): "튜플 key",
}
print(sample)


# ============================================================
# 2. 딕셔너리 활용
# ============================================================
member = {
    "id": 4000,
    "email": "hello@naver.com",
    "name": "이순신",
    "birth": "20010424",
    "address": "대전 광역시 중구 선화동 방산빌딩 2층 203호",
}


# 이름 확인
if "name" in member:
    if member["name"] == "이순신":
        print("이순신이다.")
    else:
        print("이순신이 아니다.")
else:
    print("이름 정보가 없습니다.")


# 이메일에서 도메인만 꺼내기
if "email" in member:
    email = member["email"]
    domain = email[email.index("@") + 1:]
    print(domain)

    # split을 사용해도 된다.
    domain2 = email.split("@")[1]
    print(domain2)


# 주소 문자열 수정
if "address" in member:
    address = member["address"]
    address = address.replace("선화동", "대흥동")
    member["address"] = address

print(member)


# ============================================================
# 3. 리스트 컴프리헨션
# ============================================================
# 리스트 컴프리헨션은 반복문으로 리스트를 만드는 코드를 짧게 쓰는 방법이다.
# 기본 형태:
# [표현식 for 변수 in 반복대상]

nums = []
for i in range(1, 5):
    nums.append(i * 2)
print(nums)


nums2 = [i * 2 for i in range(1, 5)]
print(nums2)


# 조건이 있는 리스트 컴프리헨션
# [표현식 for 변수 in 반복대상 if 조건식]

nums3 = [i for i in range(1, 16) if i % 3 == 0]
print(nums3)


# if~else를 표현식에 사용하는 경우
# [참일때값 if 조건식 else 거짓일때값 for 변수 in 반복대상]

cost = [4500, 6700, 3100, 5800, 2700, 4900]
result = ["저가형" if price <= 5000 else "고가형" for price in cost]
print(result)


# ============================================================
# 4. 중첩 딕셔너리
# ============================================================
# 딕셔너리 안에 또 다른 딕셔너리를 넣으면 구조적인 데이터를 표현할 수 있다.
# 예: 학생 이름을 key로 두고, 과목별 점수를 value로 저장

std1 = [89, 56, 73]
std2 = [45, 87, 35]
std3 = [81, 85, 94]
std4 = [90, 34, 61]
std5 = [59, 63, 70]

std_names = ["이순신", "임꺽정", "한석봉", "정약용", "김춘추"]
std_scores = [std1, std2, std3, std4, std5]
subjects = ("국어", "수학", "영어")

score = dict()

for i, name in enumerate(std_names):
    temp = dict()

    for k, subject in enumerate(subjects):
        temp[subject] = std_scores[i][k]

    score[name] = temp

print(score)


# 특정 학생의 성적 출력
print(score["한석봉"])

for subject, point in score["한석봉"].items():
    print(subject, point)


# ============================================================
# 5. set
# ============================================================
# set은 중복을 허용하지 않고, 순서가 없는 자료형이다.
# 중복 제거, 데이터 검색, 집합 연산에 자주 사용한다.

data = {1, 2, 3, 4, 5, 3, 4, 5, 4, 2, 3, 5}
print(data)  # 중복값은 하나만 남는다.


# 빈 set 만들기
set1 = set()
print(set1)


# 리스트를 set으로 변환하면 중복을 제거할 수 있다.
names = ["이순신", "김춘추", "장영실", "이순신", "장영실"]
set2 = set(names)
print(set2)


# set은 순서가 없기 때문에 인덱스로 접근할 수 없다.
# print(set2[1])  # 오류 발생


# set에 값 추가
set2.add("한석봉")
print(set2)


# set에 여러 값 추가
set2.update(["정약용", "문익점", "이성계"])
print(set2)


# set 값 삭제
set2.remove("한석봉")  # 값이 없으면 오류 발생
print(set2)

set2.discard("한석보")  # 값이 없어도 오류 발생 안 함
print(set2)


# set 안에 값이 있는지 확인
if "이순신" in set2:
    print("이순신이 있습니다.")


# ============================================================
# 6. set 집합 연산
# ============================================================
a = {"복숭아", "배", "메론", "체리", "포도"}
b = {"사과", "배", "딸기", "바나나"}
c = {"바나나", "참외", "사과", "귤", "포도", "딸기", "토마토"}

print(a & b)  # 교집합: 둘 다 가지고 있는 값
print(a | c)  # 합집합: 모든 값을 합침
print(b - c)  # 차집합: b에는 있고 c에는 없는 값
print(a ^ c)  # 대칭 차집합: 한쪽에만 있는 값


# set도 반복문으로 값을 하나씩 꺼낼 수 있다.
for item in c:
    print(item)


# ============================================================
# 7. 자료형 비교 정리
# ============================================================
# list
# - 여러 데이터를 저장한다.
# - 중복을 허용한다.
# - 순서가 있다.
# - 추가, 수정, 삭제가 가능하다.

# tuple
# - 여러 데이터를 저장한다.
# - 중복을 허용한다.
# - 순서가 있다.
# - 추가, 수정, 삭제가 불가능하다.

# dict
# - key:value 구조로 데이터를 저장한다.
# - key는 중복될 수 없다.
# - key를 이용해서 value에 접근한다.

# set
# - 중복을 허용하지 않는다.
# - 순서가 없다.
# - 중복 제거, 검색, 집합 연산에 사용한다.
