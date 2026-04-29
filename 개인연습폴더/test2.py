#문제 1. 1부터 10까지 차례대로 출력하세요.
for i in range(1, 11):
    print(i)
#문제 2. 10 부터 1 까지 차례대로 출력하세요.
for i in range(10, 0, -1):
    print(i)

# 문제 3. 1부터 10까지의 합을 구해서 출력하세요.
total=0
for i in range(1, 11):
    total += i
print(total)

# 문제 4. 1부터 20까지의 짝수만 출력하세요.
for i in range(1, 21):
    if i % 2 == 0:
        print(i) 

# 문제 5. 1부터 20까지의 홀수만 출력하세요.
for i in range(1, 21):
    if i % 2 == 1:
        print(i)

# 문제 6. 구구단 2단을 출력하세요.
for i in range(2, 10):
    print(f"2 * {i} = {2*i}")

# 문제 7. 구구단 2단부터 9단까지 모두 출력하세요.
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}")

# 문제 8. [3, 7, 2, 9, 5] 리스트의 총합을 구해서 출력하세요.
list = [3, 7, 2, 9, 5]
total=0
for i in list:
    total += i
print(total)

# 문제 9. [3, 7, 2, 9, 5] 리스트에서 가장 큰 수를 구해서 출력하세요.
list = [3, 7, 2, 9, 5]
print(max(list))

# 문제 10. [3, 7, 2, 9, 5] 리스트에서 5보다 큰 값만 출력하세요.
list = [3, 7, 2, 9, 5]
for i in list:
    if i > 5 :
        print(i)