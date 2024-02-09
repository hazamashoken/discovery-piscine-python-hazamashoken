#! /usr/bin/python3

import datetime

def main():
    my_age = 42 + datetime.datetime.now().year - 2001
    print(my_age) 

if __name__ == "__main__":
    main()