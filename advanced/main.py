from operations import *
from utils import *

def main() -> None:
    num1 = get_user_number()
    num2 = get_user_number()
    operations = get_operations()

    if operations == "+":
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif operations == "-":
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif operations == "*":
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif operations == "/":
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("N/A")


if __name__ == "__main__":
    main()
