num1 = int(input("Enter the first digit: "))
num2 = int(input("Enter the second digit: "))

operation = input(''' 
A for addition
S for subtraction
M for multiplication
D for division
Enter the operation:''').lower()

#lower() is used to convert the input to lowercase
'''triple single quotes are used for multiline strings or
 can be used to make multiline comments'''

if operation == "a":
    print(f"The sum is {num1 + num2}")
elif operation == "b":
    print(f"The difference is {num1 - num2}")
elif operation == "c":
    print(f"The product is {num1 * num2}")
elif operation == "d":
    print(f"The quotient is {num1 + num2}")
else:
    print("Invalid operation")