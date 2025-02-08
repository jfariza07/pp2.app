# ====== 代码来自 Lab1.ipynb ======

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



# ====== 代码来自 Lab2.ipynb ======

print(10>9)
print(10==9)
print(10<9)

a=222
b=33
if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Evaluate a string and a number
print(bool("Hello"))
print(bool(14))

# Evaluate two variables
x="Hello"
y=5
print(bool(x))
print(bool(y))

print(bool("abs"))
print(bool(12))
print(bool(["apple","banana","cherry"]))

# The following will return false;
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


def myFunction():
    return True

print(myFunction())

def myfunc():
    return True

if myfunc():
    print("Yes")
else:
    print("No")

# isinstance()function ,which can be used to determine if an object is of a certain data type:
# check if an object is an integer or not;
x=20
print(isinstance(x,int))

# Python Arithmetic Operators
x=10
y=5
print(x+y) #Addition
print(x-y)#Subtraction
print(x*y) #Multiplication
print(x/y) #Division
print(x%y)#Modulus
print(x**y)#Exponentiation
print(x//y)#Floor division


#Python Bitwise Operators
x=2 
y=5
print(x&y) #AND
print(x|y) #OR
print(x ^y) #XOR
print(~x) #NOT
print(x<<2)#Zero fill left shift
print(x>>2)#Signed right shift

thislist=["a","b","c"]
print(thislist)

#Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#List Length
list=["2","6","9"]
print(len(list))

#List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]

#type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

List=["apple","banana","cherry"]
print(List[1])

#Negative indexing
list=["banana","cherry","apple"]
print(list[-1])

#range of indexes
list=["a","b","c","d","e","f","g"]
print(list[2:5])
#The search will start at index 2 (included) and end at index 5 (not included).

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list[-4:-1])

#Check if Items Exists
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if "apple" in thislist:
    print("Yes,it exists")

#Change Item Value
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[1]="watermelon"
print(thislist)

#Change a range of item values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[2:4]=["grapes","lemon"]
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[1:2]=["lemon","pineapple"]
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[1:3]=["watermelon"]
print(thislist)

#Insert Items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.insert(2,"watermelon")
print(thislist)

# Append Item:to add an item to the end of the list,use the append() method
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.append("watermelon")
print(thislist)

#Insert Item:To insert a list item at a specified index,use the insert() method:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.insert(1,"watermelon")
print(thislist)

#Extend List:To append elements from another list to the current list,use the extend() list:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Add any iterable:The extend() method does not have to append lists,you can add any iterable object;
thislist = ["apple", "banana", "cherry"]
thistuple=("kiwi","lemon")
thislist.extend(thistuple)
print(thislist)

#Remove specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("apple")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Remove specified index:the pop() method remove specified index
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.pop(1)
print(thislist)

#If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.pop()
print(thislist)

#The del keyword alse removes specified index
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
del thislist[0]
print(thislist)

#the del keyword can alse delete the list completely
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
del thislist

#clear the list
#the clear() method empties the list,the list still ramains,but it has no content
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Loop Through a list
#You can loop through the list item by using for loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#Loop through the Index Numbers
#You can loop through the list items by referring to their index number
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#Using a While loop
thislist = ["apple", "banana", "cherry"]
i=0
while i<len(thislist):
    print(thislist[i])
    i=i+1
    

#Loop using list Comprehension
#List comprehension offers a shortest syntax for looping through the list
thislist = ["apple", "banana", "cherry"]
[print (x) for x in thislist]

#for loop
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[]
for x in fruits:
    if 'a' in x:
        newlist.append(x)

print(newlist)

#with list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x for x in fruits if "a" in x]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x for x in fruits if x!="apple"]
print(newlist)

newlist=[x for x in range(10)]
print(newlist)

newlist=[x for x in range(10) if x<5]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x.upper() for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=["banana" for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x if x != "banana" else "orange" for x in fruits]
print(newlist)

#Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sort Descending:Use th key word reverse=True
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Customize Sort Function
#You can also customize your own function by using the key word argument key=function
#The function will return a number that will be used to sort the list(the lowest number first)
def functionf(n):
    return abs(n-50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=functionf)
print(thislist)

#Case Insensitive Sort
#by default the sort() method is case sensitive,resulting in all capital letters being sorted before lower case letter
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Reverse Order
#the reverse() method reverses the current sorting older of the elements
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Use the copy() method
# make a copy of a list with the copy() method
thislist = ["apple", "banana", "cherry"]
mylist=thislist.copy()
print(mylist)

#Use the list() method
thislist = ["apple", "banana", "cherry"]
mylist=list(thislist)
print(mylist)

#Use the slice Operator
# make a copy of a list with the : operator
thislist = ["apple", "banana", "cherry"]
mylist=thislist[:]
print(mylist)

#Join two list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3=list1 + list2
print(list3)

#join two list by appending all the items from list2 into list1,one by one
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)

print(list1)

#use the extend() method ,where the purpose is add elements from one list to another list
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

#A tuple is a collection which is ordered and unchangeble(write with round brackets)
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Allow Duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


#Create Tuple With One Item
thistuple=("apple",)
print(thistuple)

#Not a tuple
thistuple=("apple")
print(thistuple)

#Create Tuple With One Item
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

#Tuples are defined as objects with the data type 'tuple'
#<class 'tuple'>
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#The tuple() ConstructorThe tuple() Constructor
#using the tuple() methond to make a tuple
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes")

x = ("apple", "banana", "cherry")
y=list(x)
y[1]="lemon"
x=tuple(y)
print(x)

#Add Items
#convert the tuple into a list,add "orange",and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#Remove Items
thistuple = ("apple", "banana", "cherry")
y=list(thistuple)
y.remove("apple")
new=tuple(y)
print(new)

# The del ketword can delete the tuple completely
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)

fruits = ("apple", "banana", "cherry")
(green,red,yellow)=fruits
print(green)
print(red)
print(yellow)

#Using Asterisk*
#If the number of variables is less than the number of values,ou can add * to the variable name and the values will be assighned to the variable as list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)

#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green,*tropic,red)=fruits
print(green)
print(tropic)
print(red)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

#Using a While Loop
thistuple = ("apple", "banana", "cherry")
i=0
while i<len(thistuple):
    print(thistuple[i])
    i=i+1

#Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3=tuple1+tuple2
print(tuple3)

#Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple=fruits*2
print(mytuple)

#count()
#index()

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set1 = {"abc", 34, True, 40, "male"}

#type()
myset = {"apple", "banana", "cherry"}
print(type(myset))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

thisset = {"apple", "banana", "cherry"}
for i in thisset:
    print(i)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

#add an item to the set,,using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#Add sets
#To add item from another set into the current set,use the update() method:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#using remove() method
#thisset = {"apple", "banana", "cherry"}
thisset.remove("apple")
print(thisset)

#using discard() method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#using pop() method
thisset = {"apple", "banana", "cherry"}
x=thisset.pop()
print(x)
print(thisset)

#clear() method empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

thisset = {"apple", "banana", "cherry"}
for i in thisset:
    print(i)

#Union
#The union() method returns a new set with all items from both set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3=set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3=set1|set2
print(set3)

#Join Multiple Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset=set1.union(set1,set2,set3,set4)
print(myset)

#Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset=set1|set2|set3|set4
print(myset)

#Join a Set and a Tuple
x = {"a", "b", "c"}
y = (1, 2, 3)
z=x.union(y)
print(z)

#Update
#The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#Intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3=set1.intersection(set2)
print(set3)

#Use & to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3=set1 &set2
print(set3)

#Keep the items that exist in both set1, and set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set1)
print(set1)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3=set1.intersection(set2)
print(set3)

#Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3=set1.difference(set2)
print(set3)

#Use - to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3=set1-set2
print(set3)

#Use the difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

#Symmetric Differences
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference(set2)
print(set1)

#Use ^ to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3=set1^set2
print(set3)

#Use the symmetric_difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

#Using the dict() method to make a dictionary:
thisdict=dict(age=36,name="patamgul",contry="baigaistan")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
x=thisdict.get("model")
print(x)

thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
x=thisdict.keys()
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x=car.keys()
print(x)
car["color"]="black"
print(x)

#Get Values
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x=car.values()
car["year"]=2025

print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x=car.values()
car["color"]="red"
print(x)

#Get Items
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x=car.items()
print(x)
car["year"]=2020
print(x)

#Check if Key Exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Change Values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"]=28
print(thisdict)

#Update Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year":28})
print(thisdict)

#Adding Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"]="red"
print(thisdict)

#Update Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)

#Removing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict=thisdict.copy()
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict=dict(thisdict)
print(mydict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)

#Access Items in Nested Dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily["child2"]["name"])

#You can loop through a dictionary by using the items() method like this:
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

a = 33
b = 200
if b > a:
  print("b is greater than a")

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

a=int(input())
b=int(input())
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


#and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


#or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#Nested If
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#The pass Statement
a = 33
b = 200

if b > a:
  pass

#The while Loop
i = 1
while i < 6:
  print(i)
  i += 1

#The break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#The continue Statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#The else Statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#Python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Looping Through a String
for x in "banana":
  print(x)

#The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#The range() Function
for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x)

#Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#The pass Statement
for x in [0, 1, 2]:
  pass



# ====== 代码来自 Lab3.ipynb ======

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



