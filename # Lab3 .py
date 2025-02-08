# Lab3

class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print("String in uppercase:", self.input_string.upper())

s= StringManipulator()
s.getString()
s.printString()


class Shape:
    def area(self):
        return 0  # Default area for generic shape

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def __str__(self): 
        return f"Square with length {self.length},area: {self.area()}"

square=Square(5)
print(square)

class Shape:
    def area(self):
        return 0  

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):   
        return self.length * self.width

    def __str__(self):  
        return f"Rectangle with length {self.length}, width {self.width}, area: {self.area()}"

s= Rectangle(5, 10)

print(s.area())
print(s)


import math 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates of the point: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        print(f"Point moved to: ({self.x}, {self.y})")

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance

p1 = Point(3, 4)
p2 = Point(7, 1)

p1.show()
p1.move(6, 8)
p2.show()
distance = p1.dist(p2)
print(f"Distance between p1 and p2: {distance:.2f}")


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner  
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount} accepted. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of ${amount} accepted. Current balance: ${self.balance}")
        else:
            print("Insufficient funds!") 

account = BankAccount("John Doe", 100)
account.deposit(50) 
account.withdraw(30)
account.withdraw(200)


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example of using filter with lambda to filter prime numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers in the list:", prime_numbers)

import math
import random
from itertools import permutations

def grams_to_ounces(grams):
    return 28.3495231 * grams

def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits
    return None

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

def string_permutations(s):
    return list(permutations(s))

def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

def sphere_volume(radius):
    return (4 / 3) * math.pi * radius ** 3

def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def histogram(lst):
    for num in lst:
        print('*' * num)

def guess_the_number():
    name = input("Hello! What is your name?\n")
    number = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    guesses = 0
    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break

movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

def is_highly_rated(movie):
    return movie["imdb"] > 5.5

def highly_rated_movies(movies):
    return [movie for movie in movies if is_highly_rated(movie)]

def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"].lower() == category.lower()]

def average_imdb(movies):
    return sum(movie["imdb"] for movie in movies) / len(movies)

def average_imdb_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb(category_movies) if category_movies else 0

# Output Results

# 1. Check if a movie is highly rated
movie = movies[0]  # Usual Suspects
print(f"Is '{movie['name']}' highly rated? {is_highly_rated(movie)}")

# 2. List of highly rated movies
print("\nHighly rated movies:")
highly_rated = highly_rated_movies(movies)
for m in highly_rated:
    print(f"{m['name']} - IMDb: {m['imdb']}")

# 3. Movies by category (e.g., Romance)
category = "Romance"
print(f"\nMovies in '{category}' category:")
romance_movies = movies_by_category(movies, category)
for m in romance_movies:
    print(f"{m['name']} - IMDb: {m['imdb']}")

# 4. Average IMDb score of all movies
print("\nAverage IMDb score of all movies:")
print(f"Average IMDb score: {average_imdb(movies)}")

# 5. Average IMDb score by category (e.g., Romance)
print(f"\nAverage IMDb score for '{category}' category:")
print(f"Average IMDb score: {average_imdb_by_category(movies, category)}")

import math
import random
from itertools import permutations

def grams_to_ounces(grams):
    return 28.3495231 * grams

def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits
    return None

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

def string_permutations(s):
    return list(permutations(s))

def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

def sphere_volume(radius):
    return (4 / 3) * math.pi * radius ** 3

def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def histogram(lst):
    for num in lst:
        print('*' * num)

def guess_the_number():
    name = input("Hello! What is your name?\n")
    number = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    guesses = 0
    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break
s="abc"
print(string_permutations(s))

