def get_user_number() -> int:
    while True:
        user_input = input("Enter a number: ")

        if user_input.isdigit():
            return int(user_input)
        else:
            print("Put ONLY a number")

def get_operations() -> str:
    while True:
        operation = input("Choose an operation (+, -, *, /): ")
        if operation in ("+", "-", "*", "/"):
            return operation
        print("Choose ONLY +, -, *, or /.")