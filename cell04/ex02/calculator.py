#! /usr/bin/python

def main():
    try:
        n1 = int(input("Give me the first number: "))
        n2 = int(input("Give me the second number: "))
        print(f"""Thank you!
{n1} + {n2} = {n1 + n2}
{n1} - {n2} = {n1 - n2}
{n1} / {n2} = {int(n1 / n2)}
{n1} * {n2} = {n1 * n2}""")

    except ValueError:
        print("number must be number.")

if __name__ == "__main__":
    main()