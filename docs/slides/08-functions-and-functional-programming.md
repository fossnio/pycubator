<!-- .slide: data-background="img/function.jpg" -->
# 函式與函式編程
### Pycubator

---

# Positional 與 Named Arguments
<!-- .slide: data-background="img/steen_argument_over_a_card_game.jpg" -->
<small>Jan Steen, Argument over a Card Game, Wikimedia Commons.</small>

--

### Positional Arguments

    def func(arg1, arg2, arg3):
        pass

    func(a, b, c)

-   `arg1`, `arg2` 與 `arg3` 就是 positional arguments
-   當呼叫 `func` 時，一定要傳入 3 個 arguments ，錯誤數量的參數會引發 `TypeError` 例外
-   傳入的順序決定它會綁定至哪個參數

--
### Named Arguments

    def say(arg1, named1, named2):
        print(arg1, named1, named2)

    say('make', named2='day', named1='my')

    # output
    make my day

-   因為可以指定名稱，所以順序可以任意


--

### Default Arguments

    def func(arg1, named1=val1, named2=val2):
        pass

    func(a, named2=b, named1=c)

-   Default args 可以接在一般的 args 後面
-   `val1` 與 `val2` 就是那些變數的預設值
-   如果沒有傳入對應的參數，那預設值會被使用

--
##### 進階
### Default Arguments 常見錯誤

-   Default arguments 會在定義函式時被執行
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

# Args 與 KWArgs
<!-- .slide: data-background="img/argument-shadows.jpg" -->

--

### *args

     def func(arg1, *args):
        print(args)
     func(1, 2, 3, 4)

     # 輸出
    (2, 3, 4)

-   任意數量的 positional arguments 可被傳入
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
-   kwargs 的鍵名要對應 keyword args

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
- 它會被展開，就像是 `bar` 的 positional arguments 一樣

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
-   `a,*var_name = range(5)`: `var_name` 是一個含 0 或多個值的 list

--
##### 進階
### Required Keyword Args

-   Python 3 限定
-   任何在 `*args` 之後的參數都是 keyword args
-   如果沒有任何預設值被指定，它們就是 required keyword args
-   `def func(*args, named):`
    - `named` 是 required keyword arg
-   若想實作一定只能用 required keyword args 而不允許 positional args 請用 `*`
-   `def func(arg1, *, named)`
    - named 是 required kwarg
    - func 必須只能傳入一個 pos arg 與一個 kwarg


--
##### 進階
### Annotations

    def func(name: str, hight: float = 1.90)-> int:
        pass

-   函式參數與回傳值可被注釋 (annotated)
-   Python 不會強制任何語意在注釋中
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
-   Closures 是唯讀的： 於 `show()` 執行 `fruits += ['kiwi']` 會觸發 `UnboundLocalError` 例外。

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
#Functional Programming
<!-- .slide: data-background="img/lambda.jpg" -->
--

### Background (1)

-   Functional programming started with lambda(&Lambda;) calculus
-   Alternative to Turning machines for exploring computability
-   Expresses programs as functions operating on other functions
-   Functional programming attempts to make it easier to reason about program behavior
-   No data states allows for easier multi threaded programing

--

### Background (2)
-   Python data is mutable and allows side-effects
-   Has some functional concepts
-   Not an ideal functional programming environment

--

### First Class Functions
-   A **higher order function** is a function that does at least one of the following:
    - Takes a function as one of its inputs
    - Outputs a function

-   You can use functions anywhere you would use a value
-   Functions are immutable so you can use them as dictionary keys
-   Functions can be the return value of another function

--

### &lambda; (lambda) Functions

    f = lambda x: x + 1

-   Anonymous functions are function objects without a name
-   lambdas can have the same arguments as regular functions:
`lambda arg, *args, named=val, **kwargs: ret`
-   lambdas must be one-liners and do not support annotations
-   'syntactic sugar' to pass short functions to other functions.

--

### Higher Order Functions
-   The most common are `map` and `filter`
-   `map(f, seq)` returns an iterator containing each element of `seq` but with `f` applied
-   `filter(f, seq)` returns an iterator of the elements of seq where `bool(f(seq[i]))` is `True`


--

### Functions as Keyword Args

-   Many functions will accept another function as a kwarg `sorted(seq, key=f)`
-   `sorted` will call `f` on the elements to determine order
-   The elements in the resulting list will be the same objects in seq
-   Have the key return a tuple to sort multiple fields
-   `min(seq, key=f)` and `max(seq, key=f)` behave similarly
-   This is a good spot for lambda

--

### Partial Application

    from functools import partial
    def add(x, y):
        return x + y

    add_3 = partial(add, 3)

-   Partial application creates a new function by supplying an existing function with some of its arguments

---

##### advanced
# Decorators
<!-- .slide: data-background="img/decorators.jpg" -->

--

### Decorators

-   Decorators are transformations on functions
-   A function that takes in a function and returns a modified function

        @dec
        def func(arg1, arg2, ...):
            pass

-   Is equivalent to:

        def func(arg1, arg2, ...):
            pass
        func = dec(func)


--

### Decorator Arguments

-   A decorator can take arguments

        @decmaker(argA, argB, ...)
        def func(arg1, arg2, ...):
            pass

-   Is equivalent to:

        def func(arg1, arg2, ...):
            pass
        func = decmaker(argA, argB, ...)(func)

--
### Decorator example

    import urllib
    from functools import lru_cache

    @lru_cache(maxsize=32)
    def get_pep(num):
        'Retrieve text of a Python Enhancement Proposal'
        resource = 'http://www.python.org/dev/peps/pep-{:04d}'.format(num)
        try:
            with urllib.request.urlopen(resource) as s:
                return s.read()
        except urllib.error.HTTPError:
            return 'Not Found'

--

### Multiple Decorators

    @dec1
    @dec2
    def func(arg1, arg2, ...):
        pass


-   Is equivalent to:

        def func(arg1, arg2, ...):
            pass
        func = dec1(dec2(func))

