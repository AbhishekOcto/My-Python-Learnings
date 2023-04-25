country = open("/Users/abhishek Kumar/Abhishek/Python_Basics/login_app/countries.txt", "r")
print(country.readable()) #Boolean: Do we have access to read the file? True/false
#print(country.readlines()) #This will print all the lines in a List
#print(country.readlines()[2]) #This will print the item at index 2


for files in country.readlines():   #This will loop through all the items 
    print (files)

country.close()