#task1
def squares_up_to_n(N):
    for i in range(N + 1):
        yield i * i

# Example usage
for num in squares_up_to_n(5):
    print(num, end=" ")


#task2
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter a number: "))
print(",".join(map(str, even_numbers(n))))


#task3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for num in divisible_by_3_and_4(50):
    print(num, end=" ")


#task4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

for val in squares(3, 7):
    print(val)


#task5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

for num in countdown(10):
    print(num, end=" ")

