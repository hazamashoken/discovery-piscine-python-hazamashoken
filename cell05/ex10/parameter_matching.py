#! /usr/bin/python

from sys import argv

def main(argc, argv):
    print("none" if argc != 2 else "Good job!" if argv[1] == input("What was the parameter? ") else "Nope, sorry...")

if __name__ == "__main__":
    main(len(argv), argv)