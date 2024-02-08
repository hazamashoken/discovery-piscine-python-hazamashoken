#! /usr/bin/python


def main():
    password = "Python is awesome"
    try:
        if input() != password:
            raise ValueError
        print("ACCESS GRANTED")
    except ValueError:
        print("ACCESS DENIED")


if __name__ == "__main__":
    main()