def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

first_operation = True
while True:
    if first_operation:
        a = float(input("What's the first number?: "))
    else:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    for symbols in operations:
        print(symbols)
    operation = input("Pick an operation: ")
    b = float(input("What's the next number?: "))

    c = operations[operation](a, b)
    print(f"{a} {operation} {b} = {c}")

    user_input = input(f"Type 'y' to continue calculating with {c}, or type 'n' to start a new calculation: ")
    if user_input == "y":
        first_operation = False
        a = c
    else:
        first_operation = True
