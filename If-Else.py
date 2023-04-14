name = input("enter name:")
if name.lower() == "moki":
    print(True)
else:
    print(False)


print(name)


def if_example(a):
    if a == 1:
        print('One')
    elif a == 2:
        print('Two')
    else:
        print('Something else')

if_example(2)
if_example(4)
if_example(1)


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
