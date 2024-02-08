#! /usr/bin/python

from sys import argv

def shrink(string):
    print(string[:8])

def enlarge(string):
    print(string if len(string) > 8 else string + "Z" * (8 - len(string)))

def main(argc, argv):
    if argc < 2:
        return print("none")
    for param in argv[1:]:
        shrink(param) if len(param) > 8 else enlarge(param)


if __name__ == "__main__":
    main(len(argv), argv)