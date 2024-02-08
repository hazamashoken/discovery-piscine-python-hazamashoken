#! /usr/bin/python

def main():
    print(''.join([chr.lower() if chr.isupper() else chr.upper() for chr in input()]))

if __name__ == "__main__":
    main()