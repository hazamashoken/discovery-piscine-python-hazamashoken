#! /usr/bin/python3

from sys import argv

def main(argc, argv):
    print(argv[2].count(argv[1]) if argc == 3 else "none")

if __name__ == "__main__":
    main(len(argv), argv)