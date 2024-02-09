#! /usr/bin/python3

class ExpInvalidPass(Exception):
    pass

def main():
    password = "Python is awesome"
    try:
        if input() != password:
            raise ExpInvalidPass
        print("ACCESS GRANTED")
    except ExpInvalidPass:
        print("ACCESS DENIED")


if __name__ == "__main__":
    main()