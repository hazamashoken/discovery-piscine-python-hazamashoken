#! /usr/bin/python
from math import ceil

def main():
    try:
        print(ceil(float(input("Give me a number: "))))
    except ValueError:
        print("number must be number.")

if __name__ == "__main__":
    main()