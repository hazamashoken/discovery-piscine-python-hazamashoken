#! /usr/bin/python3

from sys import argv

def main(argc, argv):
    if argc < 2:
        return print("none")
    print(*[param + "ism" if "ism" not in param else param for param in argv[1:]], sep="\n")

if __name__ == "__main__":
    main(len(argv), argv)