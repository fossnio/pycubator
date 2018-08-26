#!/usr/bin/python3
my_file = open(r'passwd.txt')

for line in my_file:
    print(line, end='')
    
my_file.close()
