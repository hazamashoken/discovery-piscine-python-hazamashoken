#! /usr/bin/python

from sys import argv

def main(argc, argv):
    print("Number of parameters:", argc - 1)

if __name__ == "__main__":
    main(len(argv), argv)