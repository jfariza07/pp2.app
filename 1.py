print("Hello world")

a=int(input())
b=int(input())
print(a+b)


if 5>2:
    print("5 is greater than 2")
if 5 >2 :
         print("5 is greater than 2")
    

x =5
y="Hello world"
print(x)
print(y)


#this is comment
x="Hello world"
print(x)


exit()

import sys
print(sys.version)

'''
This is a comment
written in
more than just one line'''
print("Hello world!")


'''This is a comment
written in 
more than just one line'''

x=5
y="Jack"
print(x)
print(y)

x=4
x="Miko"
print(x)

x=str(3) #x will be '3
y=int(3) # y will be 3
z=float(3) #z will be 3.0

x=5
y="Hii"
print(type(x))
print(type(y))

x="Peter"
#is the same as
x='Peter'

a=4
A="Bili"
#A will not overwrite a

#Legal variable names:
myvar="Jon"
my_var="Jon"
_my_var="Jon"
myVar="Jon"
MYVAR="Jon"
myvar2="Jon"


#Illegal variable names:
2myvar="Jon"
my-var="Jon"
my var="Jon"

#CamelCase
myVariableName="Jon"
#PascalCase
#Each word starts with a capital letter
MyVariableName="jon"
'''SnakeCase
Each word is seprated by an underscore character:'''
my_variable_name="Jon"

#Python allows you to assign values to multiple variables in one line
x,y,z="Banana","Apple","Lemon"
print(x)
print(y)
print(z)

#you can assign the same value to mupltiple variables in one line:
x=y=z="Beibei"
print(x)
print(y)
print(z)

#Unpack a list
fruits=["Cherry","Grape","Orange"]
x,y,z=fruits
print(x)
print(y)
print(z)


#correct syntax to add the valur "Hello" to 3 variables in one statement
x=y=z="Hello"

x="Python is awsome"
print(x)

#In the print() function,you output the multiple variables,seprated by a comma:
x="Python"
y="is"
z="awsome"
print(x,y,z)


#you can alse use the + operator to output multiple variables:
x="Python "
y="is "
z="awsome"
print(x + y + z)


#For numbers,the + character work as a mathematical operator:
x=10
y=9
print(x+y)

#In the print() function,when you try to combine a string and a number with + operator,python will gve you an error:
x=5
y="li"
print(x+y)


#Create a function outsideof a funtion,anduse it inside the funtion
x="awsome"
def myfunc():
    print("Python is " +x)
myfunc()

#Create a variable inside a function,with same name as the global variable
x="awsome"
def myfunc():
    x="fantastic"
    print("Pythom is "+x)
myfunc()
print("Python is " +x)

#if you use the global keyword,the variable belongs to the global scope
def myfunc():
    global x
    x="fantastic"
myfunc()
print("Python is "+x)

#to change the value of global variable inside a function, refer to the variable by using the global keyword:
x="awsome"
def myfunc():
    global x
    x="amazing"
myfunc()
print("Python is "+x)

#Print the data type of given variable:
x=5
print(type(x))

x="Hello"
print(type(x))

x=20.6
print(type(x))

x=1j
print(type(x))

x=["apple","banana","cherry"]
print(type(x))


x=("apple","banana","lemon")
print(type(x))

x=range(6)
print(type(x))

x={"name":"Miko","age":19}
print(type(x))

x={"aplle","banana","cherry"}
print(type(x))

x=frozenset({"apple","banana","cherry"})
print(type(x))

x=True
print(type(x))

x=b"Hello"
print(type(x))

x=bytearray(5)
print(type(x))

x=memoryview(bytes(5))
print(type(x))

x=None
print(type(x))

x=1 #int
y=2.3 #float
z=1j # complex
#To verify the type of any object in python,use the type function:
print(type(x))
print(type(y))
print(type(z))


#Integers:
x=1122234
y=1
z=-34567543
print(type(x))
print(type(y))
print(type(z))

#Floats
x=1.3
y=3.67
z=-234.98
print(type(x))
print(type(y))
print(type(z))

#Complex
x=3+5j
y=5j
z=-5j
print(type(x))
print(type(y))
print(type(z))

#Convert from one type to another
x=1 #int
y=2.8 #float
z=5j #complex
#convert from int to float
a=float(x)
#convert from float to int
b=int(y)
#convert from int to complex
c=complex(z)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

#import the random module,and display a random nujmber between 1 and 9:
import random
print(random.randrange(1,10))

#Integers
x=int(1) #x will be 1
y=int(2.8) # y will be 2
z=int("3") # z will be 3


#Floats
x=float(1) # x will be 1.0
y=float(2.8) # y will be 2.8
z=float("4.5") #z will be 4.5


#Strings 
x=str("s2") # x will be s2
y=str(2) #y will be 2
z=str(2.9) #z will be 2.9

#You can display a string literal with the print() function:
print("Hello")
print('Hello')


#You can use the quotes inside a string,as long as they don't mathch the quote surrounding the string:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Assigning a string to a variable is done with the variable name followed by an equal sign and the string  
a ="Hello"
print(a)

#You can use the three double quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Or three single quotes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Get the character at position 1(remember that the first character has the position 0):
a="Hello,world"
print(a[1])

#Loop through the letters in the word "banana"
for x in "banana":
    print(x)

#the len() function returns the length of a string
a="Hello,world"
print(len(a))

#Check if "Free" is present in the following text
txt="The best things in life are free!"
print("free" in txt)

#Print if only "free" is present:
txt ="The best things in life are free"
if "free" in txt:
    print("Yes,'free'is present")

#check if "expensive"is not present in the following text:
txt="The best things in life are free"
print("expensive" not in txt)

#Print only if "expensive" is not present:
txt= "Best thins in life are free"
if "expensive" not in txt:
    print("No,'expensive' is not present")

#Gets the character from position 2 to position 5(not included):
b="Hello,world!"
print(b[2:5])

#Gets the character from starts to position 5(not included):
b="Hello ,world!"
print(b[:5])

#Get the character from position 2, and all the way to the end:
b="Hello,world!"
print(b[2:])

'''Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):'''

b = "Hello, World!"
print(b[-5:-2])

#The upper() method returns the string in upper case:
a="Hello,world!"
print(a.upper())

#The lower() methond returns the string in lower case:
a="Hello,world!"
print(a.lower())

#The strip() method removes any whitespace frome the begnning or the end;
a=" Hello,world! "#a will be "Hello,wordl!"
print(a.strip())

#The replace() method replaces a string with another string:
a="Hello world!"
print(a.replace("H","J"))
      

#The split() method splits string into substrings if it find instances of the separator:
a="Hello world!"
print(a.split(","))

#Merge variable a with variable b into variable c:
a="Hello,"
b="world!"
c=a+b
print(c)

#To add a space between them:
a="Hello"
b="world"
c=a+" "+b
print(c)

age=36
txt="My naame is John,my age is"+age
print(txt)

#Create an f-string
age=36
txt=f"my name is John,my age {age}"
print(txt)

#Add a placehoders for a price variable:
price=34
txt=f"The price is {price} dollars"
print(txt)

#Display the price with 2 decimals:
price=56
txt=f"The price is {price:.2f}"
print(txt)

txt=f"The price is {23*12} dollars"
print(txt)

txt="We are the so-called "Viking" from the north"

#The escape character allows you to use double quotes when you normally would not be allowed
txt="We are so-called \"vikings\" from thw north"
print(txt)

txt="We are so-called \'viking\' from the north."
print(txt)

txt="We are so-called \\viking\\ from the north."
print(txt)

txt="We are so-called \nviking from the north"
print(txt)

txt="we are so-called \tviking from the north."
print(txt)

txt="We are so-called \bviking from the north."
print(txt)

txt="We are so-called \fviking  from the north."
print(txt)

txt="hello, and welcome to my world."
x=txt.capitalize()
print(x)

txt="Hello,This is My World!"
x=txt.casefold()
print(x)

txt="banana"
x=txt.center(20)
print(x)

txt="I love cherry,cherry is my favorite fruit"
x=txt.count("cherry")
print(x)

txt = "My name is Ståle"
x=txt.encode()
print(x)

txt="Hello,welcome to my world."
x=txt.endswith(".")
print(x)


txt="H\te\tl\tl\to"
x=txt.expandtabs(2)
print(x)

txt="Hello,welcome to my world."
x=txt.find("welcome")
print(x)

txt="For only {price:.2f} dollars"
print(txt.format(price=49))

txt="hello,welcome to my world"
x=txt.index("welcome")
print(x)

txt="Company12"
x=txt.isalnum()
print(x)

txt="CompanyX"
x=txt.isalpha()
print(x)

txt="Company123"
x=txt.isascii()
print(x)

txt="1234"
x=txt.isdecimal()
print(x)

txt="23456"
x=txt.isdigit()
print(x)

txt="demo"
x=txt.isidentifier()
print(x)

txt="hello world"
x=txt.islower()
print(x)

txt="54332"
x=txt.isnumeric()
print(x)

txt="Hello, are you #1 ?"
x=txt.isprintable()
print(x)

txt="   "
x=txt.isspace()
print(x)

txt="Hello,And Welcome To My world"
x=txt.istitle()
print(x)

txt="HELLO"
x=txt.isupper()
print(x)

mytuple={"hi","hello","salem"}
x="*".join(mytuple)
print(x)

txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")

txt="Hello,My World"
x=txt.lower()
print(x)

txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

txt="I could eat cherry all day"
x=txt.partition("cherry")
print(x)

txt="I like cherry"
x=txt.replace("cherry","apple")
print(x)

txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)

txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)

#Return 20 charaters long,right justified version of the word "Cherry"
txt="Cherry"
x=txt.rjust(20)
print(x,"is my favorite")

txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")

print(x)

txt="hi, salem, privet"
x=txt.rsplit(",")
print(x)

txt="welcome to almaty"
x=txt.split()
print(x)

txt="Thank you for the help\nwelcome to Almaty"
x=txt.splitlines()
print(x)

txt="Hello,welcome"
x=txt.startswith("hello")
print(x)

txt="helLo mY name"
x=txt.swapcase()
print(x)

txt="Hello welcome to almaty"
x=txt.title()
print(x)

txt="50"
x=txt.zfill(20)
print(x)



