class home:
    def add(a, b):
        print(f"Addition is {a + b}")

    def sub(a, b):
        print(f"Subraction is {a - b}")

    def div(a, b):
        print(f"Division is {a / b}")

    def multi(a, b):
        print(f"Multiply is {a * b}")


r = 'y'
while r == 'y':
    x = int(input("Enter the value: "))
    y = int(input("Enter the value : "))
    home.add(x, y)
    home.sub(x, y)
    home.multi(x, y)
    home.div(x, y)
    r = input("want to try again (y/n) : ")
