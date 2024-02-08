#! /usr/bin/python

def famous_births(dic: dict):
    print(*[f"{ppl[1]['name']} is a great scientist born in {ppl[1]['date_of_birth']}." for ppl in sorted(dic.items(), key=lambda item: item[1]["date_of_birth"])], sep="\n")

def main():
    women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }
    famous_births(women_scientists)

if __name__ == "__main__":
    main()