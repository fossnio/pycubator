<!-- .slide: data-background="img/puzzles.jpg" -->
# 變數與簡單的資料類型

### Pycubator

---

# 變數與比較

--
### 賦值

在 Python 裡變數可以存值。這可以使用賦值運算子來達成：

    >>> a = 100
    >>> a
    100
    >>> b = 200
    200
    >>> c = a + b
    300

--

### 重賦值

你可以重賦值任何變數：

    >>> a = 10
    >>> a
    10
    >>> a = 20
    >>> a
    20
    >>> a = 5.5
    >>> a
    5.5

--
### 賦值的擴充語法

    >>> a = 50
    >>> a += 10
    >>> a
    60

-   這和 `a = a + 10` 效果一樣。
-   試試：`-=`，`*=`，`/=`，`//=`，`%=` 與 `**=`。

--
### 命名慣例

根據 Python 的慣例，變數名稱應該是小寫字母，且字和字中間用底線隔開：

    # 好的
    age = 12
    first_name = "Joe"
    x = 100

    # 壞的！
    J = 5.5
    UserName = "itzik"
    numOfRetries = 5

--

### 命名錯誤

-   如果你嘗試取得一個不存在的變數會發生什麼事？

        >>> x = 100
        >>> x
        100
        >>> y
        NameError: name 'y' is not defined

-   在 Python 程式裡，每個變數都必須先賦值才能取用：

        print(x)  # 這行會觸發 NameError 例外
        x = 1

--
##### 進階
###  刪除變數名稱

可使用 del 刪除變數名稱 (但我從來沒有遇過需要這樣做的理由)：

    >>> x = 100
    >>> x
    100
    >>> del x
    >>> x
    NameError: name 'x' is not defined

--
### 比較

-   每種資料類型對於比較運算子都有其專屬的行為
-   我們將在後面的投影片看到更多關於比較運算子的行為，但在這邊還是看一下範例：

        >>> 1 > 2
        True
        >>> 5 < 7 <= 10:
        True
        >>> 'abd' > 'abc'
        True


--

|   運算子   | 意義                            |
| --------- | ------------------------------ |
| `<`       | 小於                            |
| `<=`      | 小於等於                         |
| `>`       | 大於                            |
| `>=`      | 大於等於                         |
| `==`      | 相同                            |
| `!=`      | 不同                            |
| `is`      | 是實體物件                       |
| `is not`  | 非實體物件                       |

---

# 布林值

--

### 布林值

Python 布林類型的字面常數為 `True` 與 `False`。
讓我們透過 "if" 敘述來跑一次吧：

    >>> if True:
            print('理所當然')
    理所當然

    >>> if False:
            print('你應該看不到我')


--

### 布林值與其他類型
-   下面敘述視同 `False`：
    -   `None`
    -   `0`
    -   `[]`(或是任何空的序列資料類型，字串也算)
-   其他都視同為 `True`

--

### 布林運算子

|   運算子   | 結果                                          |
| --------- | ---------------------------------------------|
|`x or y`   | 如果 `x` 是 `False` 則為 `y` 否則為 `x`         |
|`x and y`  | 如果 `x` 是 `False` 則為 `x` 否則為 `y`         |
|`not x`    | 如果 `x` 是 `False` 則為 `True` 否則為 `False`  |

--
##### 進階
### 捷徑運算

-   前面的表格其實就是展示了 Python `and` 和 `or` 是一種 **捷徑** 運算子：

        >>> 1 or True
        1
        >>> True or 1
        True

-   `True and (2 + 2)` 的執行結果為何？
-   那 `not 3` 的執行結果呢？

---

# 字串
<!-- .slide: data-background="img/string.jpg" -->
--
### 表達字串的語法

以下這些表達字串的語法都會產生字面上相同的結果：

    "哈囉世界！"
    '哈囉世界！'
    """哈囉世界！"""
    '''哈囉世界！'''

選擇符合你需要的引號吧：

    "今天天氣真好。"
    '這表示著 "哈囉世界！"。'

--
### 多行字串

三重引號允許你的程式碼裡面出現多行的字串：

    """購物清單：
    起司
    蘋果
    麵包"""

    '''ABC
    DEF
    GHI'''

--
### 字串跳脫序列

幾個比較重要的跳脫序列

*    `\n`: 換行
*    `\t`: tab
*    `\'` 與 `\"`： 單引號與雙引號
*    `\\`: 反斜線
*    `\x68`: ASCII 字元 104 (16 進位的 "68" 等同 10 進位的 104)

--
### 範例

    "我寫：\"哈囉！\"。\n他寫：\"掰掰！\"。"

-   若要更多資訊，請查看 Python 文件中的 [字彙分析][lex]。

[lex]: http://docs.python.org/3/reference/lexical_analysis.html#string-literals

--
##### 進階
### 原始字串

若想關閉跳脫序列，可以使用原始字串：

    >>> print('c:\windows\newstuff\todo')  # 喔哦!
    c:\windows
    ewstuff odo
    >>> print(r'c:\windows\newstuff\todo') # 好多了。
    c:\windows\newstuff\todo

---

# 常見的字串物件方法

--
### 檢查
*   endswith, startswith

        'hello world'.startswith('he')  # -> True
*   isalnum, isalpha, isdigit, islower, isupper, isspace

        '123'.isdigit()  # -> True
        'Hello World'.islower()  # -> False

--
### 搜尋

*   count

        'hello world'.count('l')  # -> 3
*   find (index 功能和 'find' 相同，唯一的差別是找不到時會引發例外。)

        'hello world'.find('l')  # -> 2
        'hello world'.find('t')  # -> -1



--
### 更動操作

請注意： `str` 是不可變動的類型。
下面的操作都是傳回一個新的字串 (沒辦法就地變動)。

--

*   lower, upper , title , capitalize , swapcase

        'hello world'.title()  # -> 'Hello World'
        'hello world'.capitalize()  # -> 'Hello world'

*   replace

        'hello world'.replace('world', 'john')  # -> 'hello john'

*   strip, rstrip, lstrip - 移除前後、後面、與前面的空白或換行字串：

        '     hello!    \n'.strip() # -> 'hello!'

--
### `+` 與 `*`

    '哈囉 ' + '世界'  # -> '哈囉 世界'

    '哈囉 ' * 3  # -> '哈囉 哈囉 哈囉 '

---

# 互動式輸入與格式化字串
<!-- .slide: data-background="img/input.png" -->

--
### 互動式輸入
- `input()`
- `input(prompt)` 先顯示 `prompt` 於螢幕上再讓你輸入
- **注意！** 在 Python 2 中是 `raw_input()`

--
### 格式化

    name = '王小明'

    # 不好的格式化語法
    print('哈囉 ' + name + '！' )

    # 舊式格式化語法
    print('哈囉 %s！' % name)

    # 新式格式化語法
    print('哈囉 {}！'.format(name))

--

-   Named formatting

        TMPL = '你在 {file} 檔案中第 {line} 行有個錯誤'
        #.....
        # ....

        print(TMPL.format(file='a.py', line=5))

-   positional formatting

        >>> print('{0} {0}, {1}'.format('重複我','不要重複我'))
        重複我重複我不要重複我

--

-   字串至少要有 x 個字元: `{:x}` (格式化表格時好用)

        TEST_RESULTS_TMPL = '{test:40} {status:10}'
        print(TEST_RESULTS_TMPL.format(test='NDU', status='Failed'))
        print(TEST_RESULTS_TMPL.format(test='Cluster expansion', status='Succeed'))
        ---
        NDU                                      Failed
        Cluster expansion                        Succeed
--

-   格式化數字成 2 進位 `{:b}` 或 16 進位 `{:x}`

        >>> print('{:b}'.format(5))
        101

-    簡單說， `{name!conversion:format}` 提供了基於 `{}` 語法之上的參數

--
### 資源
-   [Format Specification Mini-Language](https://docs.python.org/2/library/string.html#format-specification-mini-language).
-   [Examples](https://docs.python.org/2/library/string.html#format-examples)
-   [String Formatting Cookbook](http://ebeab.com/2012/10/10/python-string-format/)
-   [Common use cases](http://pyformat.info/)


--
###### 練習
[輸入與格式化字串練習](http://lms.10x.org.il/item/123/)
