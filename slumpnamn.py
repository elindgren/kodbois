# -*- coding: utf-8 -*-

import random
from sys import argv
import readlist
import json


def main(argv):
    word = {"drak", "Mannen", "Öhl", "pojken", "pleb", "tnoy", "helvete", "förgöraren", "kuk",
            "röv", "fan", "dödlig", "kränkt", "döden", "f5xrk", "Quantum", "Dataterminal",
            "Jesus", "senpai", "MILF", "smuts", "fitt", "penis", "gamer", "girl", "boy", "röven",
            "Satan", "Baldur", "Kawaii"}
    
    word = word | readlist.read_files()

    separator = ["", " ", "/", "\\", "-", "_", "&", "@"]

    def print_names(n):
        output_json = {}
        for i in range(n):
            new_name = ""
            nr_word = random.randint(1, 3)
            for j in range(nr_word):
                #new_name += random.choice(word)
                new_name += random.sample(word, 1)[0]
                if not j == nr_word - 1:
                    new_name += random.choice(separator)
            output_json[i] = new_name
        print(json.dumps(output_json))


    try:
        # num = int(input("Enter number of desired names: "))
        num = int(argv[1])
        print_names(num)
    except:
        print_names(1)

    return 0


if __name__ == "__main__":
    main(argv)
