#! /usr/bin/python

def find_the_redheads(dic: dict):
    return [key for key, _ in filter(lambda item: item[1] == "red", dic.items())]

def main():
    dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
    }
    print(find_the_redheads(dupont_family))

if __name__ == "__main__":
    main()