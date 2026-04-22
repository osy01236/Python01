# print("숫자 : 1")
# print("숫자 : 2")
# print("숫자 : 3")
# print("숫자 : 4")
# print("숫자 : 5")

#for 변수 in 반복가능한_객체:
#    실행할_코드
#5번 반복하는 반복문

# for i in range(1,-11,-1):
#     print("숫자 :"+str(i))

# print("=========================")

# for hi in "hello" :
#     print(hi)

# for name in ["차도헌","박지연","이성찬","김진숙","이동렬","김현규"]:
#     if name.startswith("이"):
#         print(name)

# #문제1 1부터 10까지의 총합을 구하세요. 반복문을 사용해서
# sum=0
# for i in range (1,11):
#     sum += i
# print("총합 : "+str(sum))

#문제2. ["15,000", "13,000", "8,700", "9,000", "25,000"]
#배열에 출금 금액들이 저장되어 있다.
#만원 이상 금액들에 대해 출력하세요.

# list =["15,000", "13,000", "8,700", "9,000", "25,000"]

# for price in list :
#     l= int(price.replace(",",""))
#     if l >= 10000 :
#         print(price)

# for i in range( len(list)):
#     print("금액: ", i+1 , list[i] )

# #enumerate  반복문에서 순서번호(인덱스)랑 값 같이 꺼내는 함수
# for i, v in enumerate(list):
#     print ( i , v )      

#문제3. [89, 56, 78, 92, 61, 96, 83, 74]
# 203호 학생들의 성적이다. 성적의 총합과 평균을 출력하세요.
#80점 이상인 학생들의 위치(인덱스)도 출력하세요.
# list = [89, 56, 78, 92, 61, 96, 83, 74]
# sum= 0   
# for jumsu in list :
#     sum += jumsu
#     avg = int(sum/(len(list)))
# print("총합 :",str(sum)+"점")    
# print("평균 :",str(avg)+"점")

# for i, v in enumerate(list):
#     if v >= 80 :
#         print(i , str(v)+"점")

#반복문 while
# while 조건 :
#     실행할_코드
#while문은 조건식이 참인경우 동작 하기 때문에
# 쉽게 무한루프에 들어갈 수 있다.
# 하여 while문을 사용시 중단 시킬 수 있는 break를 같이 사용하는게 좋다.
# num = 5
# while num > 2:
#     print("2보다 크다")
#     break

# while True :
#     num +=1
#     print( num)
#     if num == 10 :break

# print ("====================")
# while True:
#     cmd = input("명령어 입력 : ").strip().lower()
#     if cmd == "history" :
#         print( "모든기록 출력")
#     elif cmd == "mkdir":
#         print("새로운 폴더 만들기")
#     elif cmd == "remove" :
#         print("파일 삭제")
#     elif cmd == "exit":
#         break
#     else:
#         print("존재 하지 않는 명령어입니다.")

#파이썬 랜덤 사용
# import random
# num = random.randint(1,10)
# 동전 앞면 뒷면 맞추기 게임 만들기


# while True:
#     com = random.choice(["앞","뒤"])
#     user = input("입력 : ")
#     if user == com :
#         print("맞춤")
#         break
#     else:
#         print("틀림")
import random
win=0
lose=0
drow=0

game = ["가위","바위","보"]

for n in range(5):
    com =random.choice(game)
    user=random.choice(game)
    print("컴퓨터:"+com, "사용자:"+user)
    if com == user :
        drow += 1
    elif com == "가위" and user == "바위" :
        win += 1
    elif com == "가위" and user == "보" :
        lose += 1
    elif com == "바위" and user == "보" :
        win += 1
    elif com == "바위" and user =="가위":
        lose += 1
    elif com == "보" and user =="바위":
        lose += 1
    elif com == "보" and user =="가위":
        win +=1    
print("승리횟수 : ",win)
print("패배횟수 : ",lose)        
print("비긴횟수 : ",drow)    
#=======================================================
   
def compare(a,b):
    if a>b: return 1
    elif a<b: return -1
    else: return 0


game = ["가위","바위","보"]
win = lose = draw=0
for i in range(5):
    com =random.choice(game)
    user=input("입력 : ").strip()

    print("컴퓨터:"+com, "사용자:"+user)
    #game.index("가위")
    # 사전적 순서 비교 방법은 비교연산자
    cidx = game.index(com)
    uidx = game.index(user)

    comp = cidx - uidx # 유저와 컴의 가위바위 보 값 비교
    #가위-0, 바위-1, 보-2 -> 유저가 0 컴이 1이라면 컴의 승
    #즉 comp에 1이 있다면 컴의 승
    if com == user:
        print("비김")
        draw += 1
    elif comp == -1 or comp == 2:
        print("사용자 승")
        win += 1
    else:
        print("사용자 패배")
        lose += 1
print("승:",win,"패:",lose,"무:",draw)