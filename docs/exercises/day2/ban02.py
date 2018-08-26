#!/usr/bin/python3
passwd = open('passwd.txt')

for line in passwd:
    splitted_line = line.split(':')
    user_account = splitted_line[0]
    # user_account = line.split(':')[0]
    print(user_account)

passwd.close()
