#! /usr/bin/python3

def main():
    try:
        n1 = input("Give me a number: ")
        print("This number is a decimal.") if (int(float(n1)) != float(n1)) else print("This number is an integer.")
    
    except ValueError:
        print("number must be number.")

if __name__ == "__main__":
    main()