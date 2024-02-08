#! /usr/bin/python

def main():
    try:
        num = int(input("Enter a number\n"))
        for i in range(10):
            print("{} x {} = {}".format(num, i, num * i))
    except ValueError:
        print("Input is not a number")


if __name__ == "__main__":
    main()