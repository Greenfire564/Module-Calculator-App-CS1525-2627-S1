from operations import *
def main() -> None:
    num1 = 4.2364783
    num2 = 67.238999444
    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
    print(f"{num1} / {num2} = {divide(num1, num2)}")
if __name__ == "__main__":
    main()