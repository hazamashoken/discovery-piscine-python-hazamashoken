#! /usr/bin/python3

def main():
    arr = [2, 8, 9, 48, 8, 22, -12, 2]
    print(arr, set(n + 2 for n in arr if n > 5), sep="\n")

if __name__ == "__main__":
    main()


    # n + 2 for n in arr if n > 5

    