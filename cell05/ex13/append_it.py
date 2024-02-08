#! /usr/bin/python

from sys import argv

def main(argc, argv):
    if argc < 2:
        return print("none")
    for param in argv[1:]:
        print(param + "ism" if "ism" not in param else param)

if __name__ == "__main__":
    main(len(argv), argv)