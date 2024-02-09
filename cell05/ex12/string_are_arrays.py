#! /usr/bin/python3

from sys import argv

def main(argc, argv):
    if argc != 2:
        return print("none")
    print("none" if argv[1].count("z") == 0 else 'z' * argv[1].count("z"))

if __name__ == "__main__":
    main(len(argv), argv)