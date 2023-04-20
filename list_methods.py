numbers = [1,2,3,4,5,5,6,6,7,8,89,10]
fruits = ['banana', 'apple', 'orange', 'pineapple', 'guava', 'peers', 'pomegranate', 'grapes']

numbers.extend(fruits) #will add second list to first
print(numbers)


fruits.append('cherry') #will add more items at end
print(fruits)


print (len(fruits)) #will give the length of list

fruits.insert(0, 'litchi')
print(fruits)

fruits.reverse() #takes no args, will reverse the list
print(fruits)