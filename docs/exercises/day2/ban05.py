#!/usr/bin/python3
passwd = open('passwd.txt')

WHITE_LIST = ['william', 'chyang']

for line in passwd:
    splitted_line = line.split(':')
    user_account = splitted_line[0]
    if user_account in WHITE_LIST:
        continue
    if int(splitted_line[2]) >= 1000 and 'home' in splitted_line[-2]:
        print(user_account)
    

passwd.close()
