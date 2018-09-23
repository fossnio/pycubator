<!-- .slide: data-background="img/function.jpg" -->
# 函式與函式編程
### Pycubator

---

# 位置參數與關鍵字參數
<!-- .slide: data-background="img/steen_argument_over_a_card_game.jpg" -->
<small>Jan Steen, Argument over a Card Game, Wikimedia Commons.</small>

--

### 位置參數

    def func(arg1, arg2, arg3):
        pass

    func(a, b, c)

-   `arg1`, `arg2` 與 `arg3` 就是位置參數
-   當呼叫 `func` 時，一定要傳入 3 個參數，錯誤數量的參數會引發 `TypeError` 例外
-   傳入的順序決定它會綁定至哪個參數

--
### 關鍵字參數

    def say(arg1, named1, named2):
        print(arg1, named1, named2)

    say('make', named2='day', named1='my')

    # 輸出
    make my day

-   因為可以指定名稱，所以順序可以任意


--

### 預設參數

    def func(arg1, named1=val1, named2=val2):
        pass

    func(a, named2=b, named1=c)

-   預設參數可以接在一般的參數後面
-   `val1` 與 `val2` 就是那些變數的預設值
-   如果沒有傳入對應的參數，那預設值會被使用

--
##### 進階
### 預設參數常見錯誤

-   預設參數會在定義函式時被執行
-   在任何呼叫中，會使用初始計算完的結果作為其值。
-   如果該預設值是可變動的型別，對於該參數的變動將會讓後續的呼叫都受到影響
-   `def func(a=[])` 將會改變其後所有呼叫的預設值
-   使用 None 作為預設值避免這個改變的問題

        def func(a=None):
            a = a or []

--
##### 進階
### Memoization

-   Memoization 是一種優化的作法，將函式呼叫運算的結果存在緩存中
-   前面運算的結果可以在後面的呼叫中直接查找
-   可以使用 dictionary 作為 default arg 來儲存結果
-   `def func(arg, cache={}):`
-   儲存結果在 `cache[arg] = ans`
-   在進行其他工作前先檢查 cache 中對應的 arg 索引

---

# 參數與關鍵字參數
<!-- .slide: data-background="img/argument-shadows.jpg" -->

--

### *args

     def func(arg1, *args):
        print(args)
     func(1, 2, 3, 4)

     # 輸出
    (2, 3, 4)

-   可傳入任意數量的位置參數
-   可以取任何名稱，但使用 `args` 是慣例
-   `args` 是一個包含 0 或多個物件的 tuple

--
###### 練習
### 列出學生列表

-   實作 `list_students` 函式

        expected_result = '''0 Tim
        1 Tom
        2 Tal'''

        assert expected_result == list_students('tal', 'tom', 'tim')


--
### **kwargs

    def foo(arg1, **kwargs):
        print(kwargs)

    foo(1,two=2, three=3)

    # 輸出
    {'two': 2, 'three': 3}

-   於最後的位置使用 `**kwargs`
-   可取任何名稱，但使用 `kwargs` 是慣例
-   kwargs 是個存放字串為鍵的 dictionary
-   kwargs 的鍵名要對應關鍵字參數

--
###### 練習
實作 `person_details` 並傳入 kwargs
```python
# 輸出
assert person_details(name='Mike', age=28) == 'Mike is 28 years old'
```
--

### 在函式呼叫中使用 `*`

    def bar(arg1, arg2, arg3):
        print(arg1+arg2+arg3)

    l = [1, 2, 3]
    bar(*l)

    # 輸出
    6

- `l` 是可疊代的
- 它會被展開，就像是 `bar` 的位置參數一樣

--
### 在函式呼叫中使用 `**`

    def print_person(name, age):
        print('{} is {} years old'.format(name, age))

    person = {'name': 'Mike', 'age': 28}
    print_person(**person)

    # 輸出
    Mike is 28 years old


- `person` 必須是 `{'string': val, ...}` 的 dictionary
- 它會被展開，就像是 `print_person` 的 keyword arguments 一樣


--
##### 進階
### 疊代器展開

    a, *the_rest = range(4)
    print(the_rest)

    # 輸出
    (1, 2, 3)


-   只能在 Python 3 上跑
-   `a,*var_name = range(5)`：`var_name` 是一個含 0 或多個值的 list

--
##### 進階
### 必要關鍵字參數

-   Python 3 限定
-   任何在 `*args` 之後的參數都是關鍵字參數
-   如果沒有任何預設值被指定，它們就是必要關鍵字參數
-   `def func(*args, named):`
    - `named` 就是必要關鍵字參數
-   若想實作只能有必要關鍵字參數而不允許位置參數，請在前面加上 `*`
-   `def func(arg1, *, named)`
    - named 是必要關鍵字參數
    - func 只能傳入一個位置參數與一個關鍵字參數


--
##### 進階
### 函式註解

    def func(name: str, hight: float = 1.90)-> int:
        pass

-   函式參數與回傳值可被註解 (annotated)
-   Python 不會強制任何語意在註解中
-   欲知詳情請參閱 [PEP 3107](https://www.python.org/dev/peps/pep-3107/) and [PEP 484](https://www.python.org/dev/peps/pep-0484/)

---

##### 進階
# 閉包 (Closures), Global 與 Non-Local
<!-- .slide: data-background="img/global.jpeg" -->

--

### 閉包 (Closures)

    def list_fruits():
        fruits = ['bannana', 'apple']
        def show():
            print(fruits)

        return show

    fruit_list = list_fruits()
    fruit_list()

    # 輸出
    ['bannana', 'apple']


--

-   一個可以知道定義在它的 scope 外的變數定義的函式。
-   `show()` 是一個 closure 因為它知道 `fruits` 的值
-   Closures 是唯讀的：於 `show()` 執行 `fruits += ['kiwi']` 會觸發 `UnboundLocalError` 例外。

--

### Global

    a = 42
    def func():
        global a
        a += 1

-   更改全域的變數狀態有可能是危險的，所以 Python 要求你必須明確宣告
-   `global` 可以規避唯讀的 closures
-   `global` 關鍵字宣告了區塊範圍的變數，變成全域範圍
-   宣告為全域的變數不用事先綁定

--

### Nonlocal

    def outer():
        a = 42
        def func():
            nonlocal a
            print(a)
            a += 1
        func()

-   Python 3 限定
-   `nonlocal` 宣告區塊範圍的變數，指涉到最接近的上層區塊範圍 (enclosing scope)
-   如果最接近的上層區塊範圍是全域範圍，則引發 `SyntaxError`
-   參考 [PEP 3104](https://www.python.org/dev/peps/pep-3104/)


---

##### 進階
# 函式編程
<!-- .slide: data-background="img/lambda.jpg" -->
--

### 背景 (1)

-   函式編程始於 lambda(&Lambda;) 演算
-   一種用來探索如何將機器轉成更適用於計算的手段
-   將程式表達成函式敘述並與其他函式互動
-   函式編程試圖讓推論程式的行為更加簡單
-   避免改變資料狀態以讓多執行緒的程式更加容易撰寫

--

### 背景 (2)
-   Python 的資料型別有些是可變動的，也會有 side-effects
-   有一些函式編程的概念在裡面
-   不是一個理想的函式編程開發環境

--

### First Class Functions
-   **higher order functions** 是一種擁有至少以下一個行為的函式：
    - 接受函式作為它的參數之一
    - 回傳一個函式

-   你可以將函式當作變數般去使用
-   函式是不可變動的所以可用來作為 dictionary 的 key
-   函式可以作為另一個函式的傳回值

--

### &lambda; (lambda) 函式

    f = lambda x: x + 1

-   匿名函式是沒有名字的函式物件
-   lambdas 可以跟一般函式一樣擁有參數：
`lambda arg, *args, named=val, **kwargs: ret`
-   lambdas 必須寫成一行且不支援 annotations
-   一種用來將短的函式傳給其他函式的 '語法糖衣'。

--

### Higher Order Functions
-   最常見到的就是 `map` 與 `filter`
-   `map(f, seq)` 回傳一個將 `seq` 中每個元素都傳進 `f` 作為函式參數並取得回傳值的疊代物件
-   `filter(f, seq)` 回傳一個將 `seq` 中每個元素 `i` 傳入 `bool(f(seq[i]))` 其結果為 `True` 的疊代物件


--

### Functions 作為 Keyword 參數

-   很多函式接受另一個函式作為 kwarg `sorted(seq, key=f)`
-   `sorted` 會對每一個元素呼叫 `f` 以決定順序
-   產生的結果其元素將會與原本在 `seq` 中的元素為相同物件
-   若 key 對應的值為 tuple 則可以用來根據多個欄位排序
-   `min(seq, key=f)` 和 `max(seq, key=f)` 行為類似
-   這是 lambda 派上用場的好地方

--

### Partial Function Application

    from functools import partial
    def add(x, y):
        return x + y

    add_3 = partial(add, 3)

-   Partial function application 會建立一個新的函式，建立時傳入一個已存在的函式與部份參數，使其呼叫行為改變

---

##### 進階
# 裝飾器
<!-- .slide: data-background="img/decorators.jpg" -->

--

### 裝飾器

-   裝飾器是函式的另一種轉換寫法
-   是一個接收函式為參數，然後回傳行為更動後的函式的函式

        @dec
        def func(arg1, arg2, ...):
            pass

-   和以下相同

        def func(arg1, arg2, ...):
            pass
        func = dec(func)


--

### 裝飾器參數

-   一個裝飾器可以傳入多個參數

        @decmaker(argA, argB, ...)
        def func(arg1, arg2, ...):
            pass

-   和以下相同：

        def func(arg1, arg2, ...):
            pass
        func = decmaker(argA, argB, ...)(func)

--
### 裝飾器範例

    import urllib
    from functools import lru_cache

    @lru_cache(maxsize=32)
    def get_pep(num):
        '取得 PEP 文字'
        resource = 'http://www.python.org/dev/peps/pep-{:04d}'.format(num)
        try:
            with urllib.request.urlopen(resource) as s:
                return s.read()
        except urllib.error.HTTPError:
            return '找不到'

--

### 多重裝飾器

    @dec1
    @dec2
    def func(arg1, arg2, ...):
        pass


-   和以下相同：

        def func(arg1, arg2, ...):
            pass
        func = dec1(dec2(func))

