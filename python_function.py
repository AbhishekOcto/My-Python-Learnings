def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Abhishek", child2="Rahul", child3="Priya")


def my_function2(**kid):
    print("His last name is " + kid["lname"])
    print("His first name is " + kid["fname"])


my_function2(fname="Shreyash", lname="Thakur")


# If the number of keyword arguments is unknown, add a double ** before the parameter name
# Arbitrary Keyword Arguments are often shortened to **kwargs

def my_function3(country="Norway"):
    print("I am from " + country)


my_function3("Sweden")
my_function3("India")
my_function3()
my_function3("Brazil")


# default parameter value.
#
# If we call the function without argument, it uses the default value


# To let a function return a value, use the return statement
def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


def myfunction():
    pass

# having an empty function definition like this, would raise an error without the pass statement


