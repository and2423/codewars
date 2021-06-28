#! /usr/bin/env python3


def tower_builder(n_floors):
    char = '*'
    mybase = list()
    starskip = n_floors * 2
    for items in range(1, starskip+1, 2):
        mybase.append((char*items).center(starskip-1))
    return mybase


def main():
    print(tower_builder(1))


if __name__ == '__main__':
    main()
