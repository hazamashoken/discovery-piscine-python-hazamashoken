#! /usr/bin/python

from sys import argv

def main(argc, argv):
    print(argv[1].lower() if argc == 2 else "none")

if __name__ == "__main__":
    main(len(argv), argv)