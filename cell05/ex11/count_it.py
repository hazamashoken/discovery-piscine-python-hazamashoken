#! /usr/bin/python

from sys import argv

def main(argc, argv):
    if argc < 2:
        return print("none")
    print(f"parameters: {argc - 1}", *[f"{param}: {len(param)}" for param in argv[1:]] ,sep="\n")

if __name__ == "__main__":
    main(len(argv), argv)