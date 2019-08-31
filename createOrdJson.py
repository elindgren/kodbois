from sys import argv
import glob
import json


def main(argv):
    words = dict.fromkeys(read_files())
    print(words)
    with open('roligaord.json', 'w') as outfile:
        json.dump(words, outfile)


def read_files():
    files = glob.glob('*.txt')
    words = set()

    try:
        for filename in files:
            words = words | set_from_file(filename)
    except:
        pass

    return words


def set_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        res = {line.strip() for line in file.readlines()}

    return res


if __name__ == "__main__":
    main(argv)