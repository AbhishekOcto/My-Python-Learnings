fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)  #this will give all fruits name having 'a' in them


#With list comprehension you can do all that with only one line of code
# Syntax: newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist1 = [x for x in fruits if "a" in x]

print(newlist1)


newlist2 = [x for x in fruits if x != "apple"]
print(newlist2)

newlist3 = [x for x in fruits]
print(newlist3)

newlist4 = [x for x in range(10)]  #range() function to create an iterable
print(newlist4)

newlist5 = [x for x in range(10) if x < 5]
print(newlist5)

newlist6 = [x.upper() for x in fruits]  #this will set the names to upper case letters
print(newlist6)

newlist7 = [x if x != "banana" else "orange" for x in fruits]
#"Return the item if it is not banana, if it is banana return orange"
print(newlist7)