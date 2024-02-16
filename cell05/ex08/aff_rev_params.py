#! /usr/bin/python3

from sys import argv

def main(argc, argv):
    print("\n".join(argv[:0:-1]) if argc > 1 else "none")

if __name__ == "__main__":
    main(len(argv), argv)