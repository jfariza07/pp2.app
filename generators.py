#task1
def s(N):
    result = []
    for i in range(N + 1):
        result.append(i * i) 
    return result

print(s(5))


#task2
def even(n):
    return [i for i in range(0, n + 1, 2)]
n = int(input())
print(",".join(map(str, even(n))))


#task3
def divisible(n):
    result = [i for i in range(n + 1) if i % 3 == 0 and i % 4 == 0]
    return result

print(*divisible(50))


#task4
#s-平方
#m-循环的值
def s(a, b):
    return [i * i for i in range(a, b + 1)]
for m in s(3, 7):  
    print(m)  


#task5
#countdown-倒计时
def countdown(n):
    return list(range(n, -1, -1))
print(*countdown(10))
