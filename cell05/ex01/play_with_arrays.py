#! /usr/bin/python

def main():
    arr = [2, 8, 9, 48, 8, 22, -12, 2]
    print("Original array:", arr)
    print("New array:", [n + 2 for n in arr])

if __name__ == "__main__":
    main()