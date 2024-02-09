#! /usr/bin/python3

def main():
    print(*[chr.lower() if chr.isupper() else chr.upper() for chr in input()], sep="")

if __name__ == "__main__":
    main()