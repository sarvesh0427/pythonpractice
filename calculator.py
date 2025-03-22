"""
Simple Calculator Using Functions

This Python program is a basic calculator that allows users to perform:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
"""

def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y

def calc():

    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    print("Operations: \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")
    operation = int(input("Select the operation: "))
    if operation == 1:
        print("Result: ", addition(first_number,second_number))
    elif operation == 2:
        print("Result: ",subtraction(first_number,second_number))
    elif operation == 3:
        print("Result: ", multiplication(first_number, second_number))
    elif operation == 4:
        while True:
            if second_number == 0:
                print("Second number should not be zero for division.")
                second_number = float(input("Re-enter the second number: "))
                continue
            else:
                print("Result: ", division(first_number,second_number))
                break

    else:
        print("Invalid...")


