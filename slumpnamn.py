# -*- coding: utf-8 -*-

import random
from sys import argv


def main(argv):
    word = ["drak", "Mannen", "Öhl", "pojken", "pleb", "tnoy", "helvete", "förgöraren", "kuk",
            "röv", "fan", "dödlig", "kränkt", "döden", "f5xrk", "Quantum", "Dataterminal",
            "Jesus", "senpai", "MILF", "smuts", "fitt", "penis", "gamer", "girl", "boy", "röven",
            "Satan", "Baldur", "Kawaii"]
    separator = ["", " ", "/", "\\", "-", "_", "&", "@"]

    def print_names(n):
        for i in range(n):
            new_name = ""
            nr_word = random.randint(1,3)
            for j in range(nr_word):
                new_name += random.choice(word)
                if not j == nr_word - 1:
                    new_name += random.choice(separator)
            print(new_name)


    try:
        # num = int(input("Enter number of desired names: "))
        num = int(argv[1])
        print_names(num)
    except:
        print_names(1)

    return 0


if __name__ == "__main__":
    main(argv)
