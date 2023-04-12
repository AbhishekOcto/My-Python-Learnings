"""Lists are used to store multiple items in a single variable.
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc."""

"""When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
Since lists are indexed, lists can have items with the same value"""

list1 = ["apple", "banana", "cherry"]  # String, int and boolean data types
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1, list2, list3)

list4 = ["abc", 34, True, 40, "male"]  # list with strings, integers and boolean values
print(list4)
print(type(list4))

mylist = ["apple", "banana", "cherry"]  # data type of list
print(type(mylist))

thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets -> list() constructor
print(thislist)

# Return the third, fourth, and fifth item
fruitlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruitlist[2:5])

thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist3[:4])
# This will return the items from index 0 to index 4.


thislist4 = ["apple", "banana", "cherry"]  # this will insert watrmelon at index 2
thislist4.insert(2, "watermelon")
print(thislist4)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)  # this will add tropical after thisList
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")  # this will add anything to last of the list
print(thislist)

newList = ["monkey", "lion", "fox", "deer", "cheetah", "tiger", "elephant"]
newList.remove("lion")
print(newList)

newList2 = ["monkey", "lion", "fox", "deer", "cheetah", "tiger", "elephant"]
newList.extend(newList2)
print(newList2)

newList3 = ["monkey", "lion", "fox", "deer", "cheetah", "tiger", "elephant"]
newList3.pop(3)  # this will remove item at index 3
print(newList3)

newList4 = ["monkey", "lion", "fox", "deer", "cheetah", "tiger", "elephant"]
newList4.clear()
print(newList4)

newList5 = ["monkey", "lion", "fox", "deer", "cheetah", "tiger", "elephant"]
for i in newList5:  # looping in list
    print(i)

thislist6 = ["apple", "banana", "cherry", "monkey", "lion", "fox", "deer", "cheetah", "tiger", "elephant"]
i = 0
while i < len(thislist6): #Looping using while
    print(thislist6[i])
    i = i + 1

thislist7 = ["apple", "banana", "cherry"]
[print(x) for x in thislist7] #A short cut for loop that will print all items in a list
