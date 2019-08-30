# -*- coding: utf-8 -*-

from sys import argv

def main(argv):
    words = set()
    for filename in argv[1:]:
        try:
            words = words | set_from_file(filename)
        except:
            pass
    
    for word in words:
        print(word)

def set_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        res = {line.strip() for line in file.readlines()}

    return res

if __name__ == "__main__":
    main(argv)