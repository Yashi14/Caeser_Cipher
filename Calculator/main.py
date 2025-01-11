import art


def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculator():
    print(art.logo)
    first_number = int(input("What is the first number:"))

    still_solving = True
    while still_solving:
        print("+\n-\n*\n/")
        operation = input("pick an operation:")
        second_number = int(input("What is the next number: "))
        result = operations[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")

        calc_continue = input(
            f"Type 'y' to continue calculating with {result} ,or type 'n' to start a new calculation: ")
        if calc_continue == "y":
            first_number = result

        elif calc_continue == "n":
            still_solving = False
            print("\n" * 30)
            calculator()
        else:
            print("Invalid")
            still_solving= False

calculator()