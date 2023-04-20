def welcome_message():
    print('Welcome to Goa Singham!!!!!!!!!!!!!!')
welcome_message()


def message(name):
    print('Welcome to Goa' +name)
message('Singham !!!!!')


def alert(speed):
    print('Reduce your speed, as it is crossing ' + str(speed) + ' Kmph') 
    #diff data types cant concanate, casting speed as string
alert(80)


def greeting(name, age):
    print(f"Hi {name}! What's up? Your age is {age} years")
greeting('Mokinder', 25)


def add_function(n1, n2):
    return n1 + n2
n1 = int(input('enter first number: '))
n2 = int(input('enter second number: '))
print('sum of both numbers is : ' + str(add_function(n1, n2))) 
