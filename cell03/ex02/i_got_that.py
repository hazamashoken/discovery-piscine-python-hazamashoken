#! /usr/bin/python3

def main():
    if (input("What you gotta say? : ") == "STOP"):
        return
    while (input("I got that! Anything else? : ") != "STOP"):
        pass

if __name__ == "__main__":
    main()