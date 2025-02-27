def squares_up_to_n(N):
    for i in range(N + 1):
        yield i * i

# Example usage
for num in squares_up_to_n(5):
    print(num, end=" ")
