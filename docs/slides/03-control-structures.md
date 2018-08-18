<!-- .slide: data-background="img/puzzles.jpg" -->
# 控制結構

### Pycubator

--
### 區塊

-   所有的控制結構 (if, while/for, 函式) 內容必須在區塊內。
-   區塊是根據縮排來判定的。
-   pep8 程式碼風格指南建議使用 4 個空白作為標準的縮排。
-   如果你正在使用 Tab 作為縮排，要確認你的編輯器會將其轉換為 4 個空白。

        if True:
            print('沒錯就是這樣')

---

# if 與 while

--
### 簡單的 if

    x = int(input())  # 在 python 2 中記得使用 raw_input()
    if x > 5:
        msg = '大於 5'
    elif x == 5:
        msg = '等於 5'
    else:
        msg = '小於 5'
    print(msg)

--
### 三元運算子

    x = int(input())
    msg = '大於 5' if x > 5 else '小於等於 5'
    print(msg)

--
### 簡單的 while

    while True:
        name = input('輸入你的名字')
        print('哈囉 {}!'.format(name))

--
### break 與 continue:

    SECRET = 'xyzzy'

    while True:
        password = input('請輸入你的密碼：')
        if not password:
            continue
        elif password == SECRET:
            break

        print('密碼錯誤！')


    print('歡迎！')

--
###### 練習

`while` and `if` [exercises](http://lms.10x.org.il/item/12/)

---

# for 迴圈

--
### 在字串上使用 for

    >>> for c in 'Hello World!':
            print(c, end=' ')
    H e l l o   W o r l d !

--
### 使用 range()

    >>> for i in range(10):
            print(i, end=',')
    0,1,2,3,4,5,6,7,8,9,

    >>> for i in range(1, 11, 2):
            print(i, end=',')
    1,3,5,7,9,

    >>> for i in range(10, 0, -1):
            print(i, end=',')
    10,9,8,7,6,5,4,3,2,1,

--
### range() 的行為

*   `range(n)` 產生 `[0, 1, ..., n-1]`
*   `range(i, j)` 產生 `[i, i+1, ..., j-1]`
*   `range(i, j, k)` 產生 `[i, i+k, ..., m]`

--

### 巢狀迴圈

    for i in range(10):
        for j in range(10):
            print(i, j)

--
### enumerate()
    >>> for i, c in enumerate('Hello World!'):
            print(i, c)
    0 H
    1 e
    2 l
    3 l
    4 o
    5
    6 W
    7 o
    8 r
    9 l
    10 d
    11 !

--
###### 練習
[for loops](http://lms.10x.org.il/item/15/)

---

# 函式

--
### 定義

    >>> def increment(x):
            return x + 1
    >>> increment(3)
    4

*   冒號 (:) 代表一個區塊的開始
*   隨後的程式碼皆要縮排
*   函式定義不指定回傳的型別
*   所有的函式都會回傳一個值 (若沒有指定則回傳 None)
*   傳入的參數型別也一樣不指定

--
###### 練習

[Functions](http://lms.10x.org.il/item/145/)
(Progress bar, 2 exercises)
