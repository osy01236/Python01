# import calc 
# import calc as c


# print(calc.add(10,20))  

# print(c.add(10,20))  #as 를 했을경우

#특정 함수나 변수를 사용하고자  한다면 아래와 같이 하면된다.

from calc import add

print(add(10,20))