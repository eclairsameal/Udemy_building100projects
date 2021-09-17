# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = int(input("What's the first number?:"))

    for symbol in operator:
        print(symbol)
    should_continue = True

    while should_continue:
        operator_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?:"))
        calculation_fun = operator[operator_symbol]
        answer = calculation_fun(num1, num2)

        print(f"{num1} {operator_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}:, or type 'n' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()   # 遞迴
calculator()