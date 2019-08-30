import numpy as np
import random
from sys import argv


def main(argv):
    word = ["drak", "Mannen", "Öhl", "pojken", "pleb", "tnoy", "helvete", "förgöraren", "kuk",
            "röv", "fan", "dödlig", "kränkt", "döden", "f5xrk", "Quantum", "Dataterminal",
            "Jesus", "senpai", "MILF", "smuts", "fitt", "penis", "gamer", "girl", "boy", "röven",
            "Satan", "Baldur", "Kawaii"]
    separator = ["", " ", "/", "\\", "-", "_", "&", "@"]

    def print_names(n):
        new_name = ""
        for i in range(n):
            nr_word = 2 + int(np.random.uniform(-2, 2))
            for j in range(nr_word):
                new_name += random.choice(word)
                if not j == nr_word - 1:
                    new_name += random.choice(separator)
            print(new_name)
            new_name = ""
    

    while True:
        try:
            num = int(input("Enter number of desired names: "))
            print_names(num)
            break
        except ValueError:
            print("Entered value is not an int.")

    return 0


if __name__ == "__main__":
    main(argv)
