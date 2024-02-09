#! /usr/bin/python3

def array_of_names(dic: dict[str, str]):
    return ([f"{key.capitalize()} {value.capitalize()}" for key, value in dic.items()])

def main():
    persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
    }
    print(array_of_names(persons))

if __name__ == "__main__":
    main()