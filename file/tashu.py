#대전 광역시 자전거 타슈의 위치 현황 파일을 불러오기
#타슈 자전거 정거장 위치 찾기 만들기
# 동이름 또는 현재 위치 (건물, 지명 등등) 입력받기
#검색어가 포함되어있는 정거장 이름 또는 주소에서 찾기

#조회한 전체 정거장을 추력하는데 중복 없어야 되고
# 정거장명 기준 내림차순으로 정렬하기

import csv

tashu_list= []

with open("file/타슈.csv", "r", encoding="utf-8" ) as f :
    data = csv.reader(f)

    header = next(data)

    for row in data :
        temp_dic = dict()
        for i , v in enumerate(row):
            temp_dic[header[i]] = v
        tashu_list.append(temp_dic)


keyword = input("검색 : ").strip()

result = set()

not_keyword = ["연번","광역시도코드","광역시도명","시군구코드","시군구명","법정동코드","법정동명","행정동코드","행정동명"]

for row in tashu_list:
    for k , v in row.items():
        if k in not_keyword:
            continue
        if keyword in v:
            result.add(row["정거장"])
            

result = sorted(result, reverse=True)


for station in result:
    print(station)



