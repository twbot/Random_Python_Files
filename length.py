#!/usr/bin/env python3
import os

def get_length(file):
    for i,l in enumerate(file):
        print('{}, {}'.format(i, l))
    #return i+1

def main():
    dir = os.getcwd()
    path = os.path.join(dir, 'skyline_input.txt')
    new_file = open(path, 'a')
    print(get_length(new_file))

if __name__ == '__main__':
    main()
