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

def append_file_string(file_name, string_of_lines):
    f = open(file_name, 'a')
    f.write(string_of_lines)
    f.close()
    
def write_file_list(file_name, list_of_lines):
    f = open(file_name, 'w')
    for num in list_of_lines:
        f.write(str(num) + '\n')
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    file1 = open(file_name_read, 'r')
    file2 = open(file_name_write, 'w')

    for i, list_of_lines in enumerate(file1.readlines()):
        file2.write(str(i+1) + ':' + list_of_lines)

    file1.close()
    file2.close()


if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))