#! /usr/bin/python3

class ExpNotZero(Exception):
    pass

def main():
    try:
        if int(input()) != 0:
            raise ExpNotZero
        print("This number is equal to zero")

    except ExpNotZero:
        print("This number is not equal to zero")
    except ValueError:
        print("Input is not a number.")
        
if __name__ == "__main__":
    main()