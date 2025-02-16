#!/usr/bin/env python3
# Author ID: apersaud-cheteram

def add(number1, number2):
    try:
        total = int(number1) + int(number2) 
        return total
    
    except ValueError:
        return 'error: could not add numbers'

def read_file(filename):
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()
        return lines
    except(FileNotFoundError):
        return 'error: could not read file'

        
if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception