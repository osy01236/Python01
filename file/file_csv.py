#csv - 쉼표로 구분된 데이터
import csv

# with open("file/test.csv" , "r", encoding="utf-8" ) as f:
#     data= csv.reader(f) #확장자가 scv 파일 일경우
#     print(data)
#     header = next(data)
#     print(header)
#     for row in data:
#         print(row)



# with open("file/test2.csv", "w" , newline="" , encoding="utf-8") as f : # newline=""옵션을 주면 데이터가 띄어쓰기 없이 들어가기
#     w = csv.writer(f)
#     w.writerow(["이름","생년월일","연락처"])
#     w.writerow(["김유신" , "19990411" , "010-1234-1234"])



# with open("file/test2.csv", "a" , newline="" , encoding="utf-8") as f :
#     w = csv.writer(f)
#     w.writerow(["이순신" , "19960522" , "010-2222-2222"])


# with open("file/test2.csv", "r", encoding="utf-8") as f :
#     dic = csv.DictReader(f)

#     for row in dic:
#         print(row)

header = ["이름","나이","직업"]
with open("file/test2.csv", "w", newline="",encoding="utf-8") as f :
    w= csv.DictWriter(f , fieldnames=header)
    w.writeheader()
    w.writerow({"이름":"문익점","나이":34 , "직업":"산업스파이"})
    w.writerow({"이름":"정약용","나이":45 , "직업":"발명가"})