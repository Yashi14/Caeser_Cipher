import art
print(art.logo)

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
    first_number = int(input("What is the first number:"))
    print("+\n-\n*\n/")
    operation = input("pick an operation:")

    still_solving = True
    while still_solving:
        second_number = int(input("What is the next number: "))
        result = operations[operation](n1=first_number, n2=second_number)
        print(result)

        calc_continue = input(
            f"Type 'y' to continue calculating with {result} ,or type 'n' to start a new calculation: ")
        if calc_continue == "y":
            first_number = result

        if calc_continue == "n":
            still_solving = False
            print("\n" * 30)
            calculator()
        else:
            print("Invalid")

calculator()