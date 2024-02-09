#! /usr/bin/python3

from sys import argv

def main(argc, argv):
    if len(argv) > 1:
        return print("none")
    for n1 in range(11):
        print(f"Table de {n1}: {' '.join([str(n1 * n2) for n2 in range(11)])}")


if __name__ == "__main__":
    main(len(argv), argv)