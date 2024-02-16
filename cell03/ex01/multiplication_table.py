#! /usr/bin/python3

def main():
    try:
        num = int(input("Enter a number\n"))
        print(*[f"{num} x {n} = {num * n}" for n in range(10)], sep="\n")
    except ValueError:
        print("Input is not a number")


if __name__ == "__main__":
    main()