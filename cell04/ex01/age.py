#! /usr/bin/python3

def main():
    try:
        age = int(input("Please tell me your age: "))
        print(f"You are currently {age} years old.")
        for i in range(10, 31 ,10):
            print(f"In {i} years, you will be {age + i} years old.")
    except ValueError:
        print("Age must be a number.")

if __name__ == "__main__":
    main()