
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))

while True:
    print("0. exit")
    print("1. addition")
    choice = int(input("enter choice: "))

    if(choice == 0):
        print("bye!")
        exit(0)
    elif(choice == 1):
        res = num1 + num2
        print("addition:", res)
