def add(num1, num2):
    answer = num1 + num2
    return(f"{num1} + {num2} = {answer}")

def sub(num1, num2):
    answer = num1 - num2
    return(f"{num1} - {num2} = {answer}")

def div(num1, num2):
    answer = num1 / num2
    return(f"{num1} / {num2} = {answer}")  

def mul(num1, num2):
    answer = num1 * num2
    return(f"{num1} * {num2} = {answer}")

def pow(num1, num2):
    answer = num1 ** num2
    return(f"{num1} to the power of {num2} = {answer}")

def main():
    print("""
to add two numbers, type 'add'
to subtract two numbers, type 'sub'
to divide two numbers, type 'div'
to multiply two numbers, type'mul'
to raise a number to a power, type 'pow'
    """)

    while True:
        operation = input("Enter the operation you want to perform: ")
        if operation == "add":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(add(num1, num2))
            break
        elif operation == "sub":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(sub(num1, num2))
            break
        elif operation == "div":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if num2 != 0:
                print(div(num1, num2))
            else:
                print("Error: Division by zero!")
            break
        elif operation == "mul":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(mul(num1, num2))
            break
        elif operation == "pow":
            num1 = float(input("Enter the base number: "))
            num2 = float(input("Enter the exponent: "))
            print(pow(num1, num2))
            break
        else:
            print("Invalid operation! Please try again.")
            continue
    
if __name__ == "__main__":
    main()