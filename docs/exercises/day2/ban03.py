#!/usr/bin/python3
passwd = open('passwd.txt')

for line in passwd:
    splitted_line = line.split(':')
    user_account = splitted_line[0]
    if int(splitted_line[2]) >= 1000:
        print(user_account)
    

passwd.close()
