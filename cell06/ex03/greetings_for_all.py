#! /usr/bin/python

def greetings(name="noble stranger"):
    print(f"Hello, {name}." if isinstance(name, str) else "Error! It was not a name.")

def main():
    greetings("Alexandra")
    greetings("Will")
    greetings()
    greetings(42)

if __name__ == "__main__":
    main()
