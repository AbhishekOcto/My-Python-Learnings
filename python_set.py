thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: the set list is unordered, meaning: the items will appear in a random order.
# Refresh this page to see the change in the result.

# Sets cannot have two items with the same value
# The values True and 1 are considered the same value in sets, and are treated as duplicates


thisset1 = {"apple", "banana", "cherry"}
thisset1.add("orange")
print(thisset1)

thisset2 = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset2.update(mylist)
print(thisset2)