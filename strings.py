#strings are arrays
print("Hello")
print('Hello')
# both "",'' will work as same

#You can assign a multiline string to a variable by using three quotes """ """, or using 3 single quotes

a = "Hello, World!"
print(a.upper())  #The upper() method returns the string in upper case

a = "Hello, World!"
print(a.lower()) #The lower() method returns the string in lower case


#The strip() method removes any whitespace from the beginning or the end
d = " Hello, World!       "
print(d.strip()) # returns "Hello, World!"


#The format() method takes unlimited number of arguments, and are placed into the respective placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 

#The escape character allows you to use double quotes when you normally would not be allowed
txt = "We are the so-called \"Vikings\" from the north."
print(txt)