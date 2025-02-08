
# Lab2

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

