#!/usr/bin/python3
passwd = open('passwd.txt')

for line in passwd:
    print(line, end='')

passwd.close()
