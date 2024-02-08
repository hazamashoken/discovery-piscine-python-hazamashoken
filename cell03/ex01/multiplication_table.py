#! /usr/bin/python

def main():
    try:
        num = int(input("Enter a number\n"))
        for n in range(10):
            print(f"{num} x {n} = {num * n}")
    except ValueError:
        print("Input is not a number")


if __name__ == "__main__":
    main()