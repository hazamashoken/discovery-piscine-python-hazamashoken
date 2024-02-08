#! /usr/bin/python

class ExpMoreThan25(Exception):
    pass

def main():
    try:
        num = int(input("Enter a number less than 25\n"))
        if num > 25:
            raise ExpMoreThan25
        while num <= 25:
            print("Inside the loop, my variable is {}".format(num))
            num += 1
    except ExpMoreThan25:
        print("Error")
    except ValueError:
        print("Input is not a number")


if __name__ == "__main__":
    main()