#! /usr/bin/python

def main():
    arr = [2, 8, 9, 48, 8, 22, -12, 2]
    print(arr)
    print(set(n + 2 for n in arr if n > 5))

if __name__ == "__main__":
    main()