def calculator():
    while True:
        print("Press(1) for addition\n")
        print("Press(2) for subtraction\n")
        print("Press(3) for multiplication\n")
        print("Press(4) for division\n")
        a=int(input("Enter the first number\n"))
        b=int(input("Enter the second number\n"))
    
        choice=input("Enter the operation you want to perform\n")
        if choice=='1':
            print("You chose addition")
            result=a+b
            print("Result is", result)
        elif choice=='2':
            print("You chose Subtraction")
            result=a-b
            print("Result is", result)
        elif choice=='3':
            print("You chose Multiplication")
            result=a*b
            print("Result is", result)
        elif choice=='4':
            print("You chose Division")
            result=a/b
            print("Result is", result)
            break
        else:
            print("Invalid Operation")
if __name__ == '__main__':
    calculator()

