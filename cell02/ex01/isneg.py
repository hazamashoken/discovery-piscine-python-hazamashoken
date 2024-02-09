#! /usr/bin/python3

class ExpPositive(Exception):
    pass

class ExpNegative(Exception):
    pass

def main():
    try:
        num = int(input())
        if (num < 0):
            raise ExpNegative
        elif (num > 0):
            raise ExpPositive
        print("This number is equal to zero")
    except ExpPositive:
        print("This number is positive")
    except ExpNegative:
        print("This number is negative")
    except Exception:
        print("This is not a number")

if __name__ == "__main__":
    main()