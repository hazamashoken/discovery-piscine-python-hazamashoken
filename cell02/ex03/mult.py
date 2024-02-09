#! /usr/bin/python3

def main():
    try:
        num1 = int(input("Enter the first number:\n")) 
        num2 = int(input("Enter the second number:\n"))
        res = num1 * num2
        print(f"{num1} * {num2} = {res}")

        print("The result is {}".format(["negative", "positive and negative", "positive"][(1 + (res >> 31) - (-res >> 31))]))
    except ValueError:
        print("Input is not a number")
            

if __name__ == "__main__":
    main()