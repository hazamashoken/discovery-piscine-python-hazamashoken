#! /usr/bin/python

from sys import argv

def main(argc, argv):
    if argc < 2:
        return print("none")
    print("parameters:", argc - 1)
    for param in argv[1:]:
        print(f"{param}:", len(param))    

if __name__ == "__main__":
    main(len(argv), argv)