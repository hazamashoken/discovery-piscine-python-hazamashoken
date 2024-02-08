#! /usr/bin/python

def main():
    first_name = ["T","h", "a","n","a","p","o","l"]
    last_name = ["L","i","a","n","g","s","o","o","n","t","h","o","r","n","s","i","t"]
    print(''.join(list([*first_name, " ", *last_name])))

if __name__ == "__main__":
    main()