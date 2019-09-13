def sum_(a, b):

    return a + b

def multiply(a, b):

    return a * b

def divide(a, b):

    return a / b

def subtract(a, b):

    return a - b
def main():
    print("Select an operation\n")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    option = int(input("Enter your choice: "))
    a = int(input("Enter the first operand"))
    b = int(input("enter the second operand"))
#practicing dictionary
   # option_list = {
   #     1: print(sum_(a, b)),
   #     2: print(subtract(a, b)),
   #     3: print(multiply(a, b)),
   #     4: print(divide(a, b))
   # }

    #option_list.get(option, "Invalid")
#practicing if statements
    if option == 1:
        print(sum_(a,b))
    elif option == 2:
        print(subtract(a, b))
    elif option == 3:
        print(multiply(a, b))
    elif option == 4:
        print(divide(a, b))
    else:
        print("invalid operation")


if __name__ == "__main__":
    main()