#! /usr/bin/python3

def main():
    first_name = ["T","h", "a","n","a","p","o","l"]
    last_name = ["L","i","a","n","g","s","o","o","n","t","h","o","r","n","s","i","t"]
    whole_name = first_name + [" "] + last_name
    print(*whole_name, sep="")

if __name__ == "__main__":
    main()