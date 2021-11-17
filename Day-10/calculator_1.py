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

num1 = int(input("What's the first number?:"))
num2 = int(input("What's the second number?:"))
for symbol in operator:
    print(symbol)
operator_symbol = input("Pick an operation from the line above: ")
calculation_fun = operator[operator_symbol]
answer = calculation_fun(num1, num2)

print(f"{num1} {operator_symbol} {num2} = {answer}")