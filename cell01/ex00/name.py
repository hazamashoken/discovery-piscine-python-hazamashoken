#! /usr/bin/python

def main():
    first_name = ["T","h", "a","n","a","p","o","l"]
    last_name = ["L","i","a","n","g","s","o","o","n","t","h","o","r","n","s","i","t"]
    print(*(first_name + [" "] + last_name), sep="")

if __name__ == "__main__":
    main()