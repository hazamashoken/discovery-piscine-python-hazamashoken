#! /usr/bin/python

from sys import argv

def downcase_it(string):
    return string.lower()

def main(argc, argv):
    print("none" if argc < 2 else '\n'.join(list(map(str.lower, argv[1:]))))


if __name__ == "__main__":
    main(len(argv), argv)