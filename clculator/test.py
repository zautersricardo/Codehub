#my own code
print('Give a first number=  ')
number1 =  float(input())

print('Give operator=  ')
operator = str(input())

print('Give a second number=  ')
number2 = float(input())

def calculator():
    if operator == '+':
        output = number1 + number2
    elif operator == '-':
        output = number1 - number2
    elif operator == '*':
        output = number1 * number2
    elif operator == '/':
        output = number1 / number2
    else:
        print("Not defined in software")
    print(output)

calculator()

#chatgpt
def calculator(number1, operator, number2):
    if operator == '+':
        output = number1 + number2
    elif operator == '-':
        output = number1 - number2
    elif operator == '*':
        output = number1 * number2
    elif operator == '/':
        output = number1 / number2
    else:
        print("Error: Invalid operator. Please use +, -, *, or /.")
        return None  # Return None or some other value to indicate an error

    print("Result:", output)
    return output

def main():
    print('Give the first number: ')
    number1 = float(input())

    print('Give operator: ')
    operator = str(input())

    print('Give the second number: ')
    number2 = float(input())

    result = calculator(number1, operator, number2)

    if result is not None:
        print("Calculation successful.")

if __name__ == "__main__":
    main()