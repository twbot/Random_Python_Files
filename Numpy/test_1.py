#!/usr/bin/env python3

import numpy as np
import os 

multiple_array = [[1, 2, 3, 4], [1, 5, 6, 7]]

def main():
    current_dir = os.getcwd()
    a = []
    
    new_file = os.path.join(current_dir, 'array.txt')
    array_file = open(new_file, 'r')
    for line in array_file:
        a.append(line.split(','))
    #x = np.reshape(a, (3, 11))
    x = np.asarray(a)
    nx = np.reshape(x, (3,10))
    print(nx)
    array_file.close()

if __name__ == '__main__':
    main()