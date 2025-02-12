#!/usr/bin/env python3
# Author ID: apersaud-cheteram

def read_file_string(file_name):
    f = open(file_name)
    read_data = f.read()
    f.close()
    return read_data

def read_file_list(file_name):
    f = open(file_name)
    read_data_list = f.read().splitlines()
    f.close()
    return read_data_list

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))