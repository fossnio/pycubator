#!/usr/bin/python3
my_file = open(r'passwd.txt')
content = my_file.read()
print(content)
my_file.close()
