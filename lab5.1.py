#task1
def match(s):
    if s.startswith("a") and s.count("a") == 1 and all(c == "b" for c in s[1:]):
        return True
    return False
test = ["a", "ab", "abb", "ac", "b", "aabb"]
for s in test:
    print(f"{s}: {match(s)}")


#task2
def m(s):
    if s == "abb" or s == "abbb":
        return True
    return False
test = ["abb", "abbb", "a", "ab", "abbbb", "abc"]
for s in test:
    print(f"{s}: {m(s)}")


#task3
def m(s):
    parts = s.split("_")
    return all(part.islower() for part in parts) if len(parts) > 1 else False
t = ["my_name", "abs_sba", "hye_hi"]
for s in test:
    print(f"{s}: {m(s)}")


#task4
def m(s):
    return s[0].isupper() and s[1:].islower() if len(s) > 1 else False
test = ["Hello", "HELLO", "hello", "Fariza"]
for s in test:
    print(f"{s}: {m(s)}")


#task5
def m(s):
    return s.startswith("a") and s.endswith("b") and len(s) >= 2
test = ["ab", "axb", "a123b", "a", "b", "abc", "a_b"]
for s in test_strings:
    print(f"{s}: {m(s)}")


#task6
def replace(s):
    for char in " ,.":
        s = s.replace(char, ":")
    return s
test = ["hello hii", "a,b.c", "My name is."]
for s in test:
    print(replace(s))


#task7
def snake_to_camel(s):
    parts = s.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])
test = ["hi_hiii", "snake_case_example", "my_name"]
for s in test:
    print(snake_to_camel(s))


#task8
def split(s):
    result = [s[0]]
    for char in s[1:]:
        if char.isupper():
            result.append(char)
        else:
            result[-1] += char
    return result
print(split_at_uppercase("Hiii")) 
print(split_at_uppercase("SplitAtUpperCase")) 
print(split_at_uppercase("MyNameIs"))


#task9
def insert(s):
    result = s[0] 
    for char in s[1:]:
        if char.isupper():
            result += " " + char
        else:
            result += char
    return result
print(insert("Hiii")) 
print(insert("SplitAtUpperCase")) 
print(insert("MyNameIs"))


#task10
def camel_to_snake(s):
    result = s[0].lower()
    for char in s[1:]:
        if char.isupper(): 
            result += "_" + char.lower()
        else:
            result += char 
    return result
print(camel_to_snake("Hiii"))  
print(camel_to_snake("CamelCaseExample")) 
print(camel_to_snake("MyNameIs"))





