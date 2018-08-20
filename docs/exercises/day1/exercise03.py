#!/usr/bin/python3
while True:
    your_input = input('請輸入你的年齡：')
    if your_input.isdigit():
        your_age = int(your_input)
        if your_age >= 18:
            print('你是成年人')
        else:
            print('你是小孩子')
    else:
        print('請輸入數字')
