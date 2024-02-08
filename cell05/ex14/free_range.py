#! /usr/bin/python

from sys import argv

def main(argc, argv):
    if argc != 3:
        return print("none")
    try:
        print(list(range(int(argv[1]), int(argv[2]) + 1)))
    except ValueError:
        print("none")

if __name__ == "__main__":
    main(len(argv), argv)