#! /usr/bin/python

def main():
    try:
        if int(input()) != 0:
            raise Exception
        print("This number is equal to zero")

    except Exception:
        print("This number is not equal to zero")

if __name__ == "__main__":
    main()