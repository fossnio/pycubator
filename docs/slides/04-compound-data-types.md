# 資料型別的組合技
<!-- .slide: data-background="img/puzzles.jpg" -->

--

### 綜觀
- 有些資料型別是由更小的元素所組成的，例如：一個字串是由多個單一字元所組成。
- 這類資料型別支援一些通用性的方法操作，雖然彼此之間仍有一些細節行為不太一樣。
- 這些資料型別為：string, tuple, list, dictionary, set。

---

# 更多有趣的字串操作！
<!-- .slide: data-background="img/string.jpg" -->

--
### 切片 (Slicing)
- 語法類似 `range` 的參數
- 中括號包住索引：`s[1]`
- 反向索引可從尾部取得元素：`s[-1]`
- 切片:
  - 基本語法為 `s[start:end]`: `s[1:4]`
  - 從字串最開始進行切片至指定位置：`s[:5]`
  - 從字串指定位置進行切片至結尾：`s[3:]`
  - 反向索引也可用在切片：`s[-3:-1]`

--
### 範例

    s = 'hello world'

    # slicing (含頭不含尾)
    s[1:4]  # -> 'ell'

    # 從頭至指定索引
    s[:4]  # -> 'hell'

    # 從指定索引至結尾
    s[3:]  # -> 'lo world'

--

    # 也可用反向索引
    s[2:-2]  # -> 'llo wor'

    # step
    s[::2]  # -> 'hlowrd'
    s[1::2]  # -> 'el ol'

    # 反向的 step
    s[::-1]  # -> 'dlrow olleh'

--

### split(), join() 與 list 資料型別
*   根據值的內容切割字串

        'hello world'.split()  # -> ['hello', 'world']

        'hello, and ,welcome'.split(',', maxsplit=1) # -> ['hello', ' and ,welcome']

* `['hello', 'world']` 是 list 資料型別。我們很快會再遇到！

--

*   使用指定的字串組合 list 的元素

        ' '.join(['hello', 'world'])  # -> 'hello world'

        ','.join(['first line', 'second line'])  # -> 'first line,second line'

--
###### 練習
[Slicing Joining and More](http://lms.10x.org.il/item/30/)

---

# Lists
<!-- .slide: data-background="img/list.jpg" -->
--
### 基礎
- 有序的值的集合
- 建立一個空的 list：

        >>> l = list()
        >>> type(l)
        list
        >>> l = []
        >>> type(l)
        list

--
### 修改內容

-   附加值至 list 尾部：

        >>> l.append('apple')
        >>> l
        ['apple']
        >>> l.append('orange')
        >>> l
        ['apple', 'orange']

-   直接建立一個 list：

        >>> l = ["orange", "apple", "strawberry", "banana", "apricot"]
        >>> l
        ['orange', 'apple', 'strawberry', 'banana', 'apricot']

--

-   加入一個值至指定索引處：

        >>> l.insert(3, 'melon')
        >>> l
        ['orange', 'apple', 'strawberry', 'melon', 'banana', 'apricot', 'grapes']

-   刪除指定索引處的值：

        >>> del l[0]
        >>> l
        ['apple', 'strawberry', 'melon', 'banana', 'apricot', 'grapes']

--

-   pop 一個元素 (移除並回傳該值)：

        >>> l.pop() # 預設是最後一個元素
        'grapes'
        >>> l
        ['apple', 'strawberry', 'melon', 'banana', 'apricot']
        >>>l.pop(0) # 指定索引處
        'apple'
        >>> l
        ['strawberry', 'melon', 'banana', 'apricot']

--
### 更多操作

- `lst[i] = v`: 就地修改取代原值
- `lst.extend(l)`: 展開一個可疊代的物件至尾部
- `lst.remove(v)`：移除第一個符合的值

--

### List 的序列操作

-   所有序列操作在 list 上都合法：

        >>> l = ['orange', 'apple', 'strawberry', 'melon', 'banana', 'apricot', 'grapes']
        >>> len(l)
        7

-   在 list 上使用 for 迴圈：

        >>> for x in l:
        ...     print(x)
        ...
        orange
        apple
        strawberry
        banana
        apricot

--

-   使用索引、反向索引與切片以取得值：

        >>> l[0]
        'apple'
        >>> l[8]
        ...
        IndexError: list index out of range
        >>> l[-1]
        'grapes'
        >>> l[2:4]
        ['strawberry', 'melon']
        >>> [10,20,30,40][::-1]
        [40, 30, 20, 10]

--

-   `in` 運算子會掃描所有元素並回傳 `True` 或 `False`：

        >>> 'apple' in l
        True
        >>> 'basketball' in l
        False

-   Lists can be concatenated with `+` and multiplied by `*`:

        >>> [25,3,14] + [5,4] + [101, 2]
        [25, 3, 14, 5, 4, 101, 2]
        >>> ["foo", "bar"] * 4
        ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar']

--

### List 的就地操作 (會影響 list 本身)

-   `.reverse()` 方法會就地變動 list 本身元素的順序並回傳 `None`：

        >>> fruit = ["orange", "apple", "strawberry", "banana", "apricot"]
        >>> fruit.reverse()  # 就地反向排序！
        >>> fruit
        ['apricot', 'banana', 'strawberry', 'apple', 'orange']

--

-   `.sort()` 方法會就地排序 list 本身的元素並回傳 `None`：

        >>> fruit = ["orange", "apple", "strawberry", "banana", "apricot"]
        >>> fruit.sort()  # 就地排序！
        >>> fruit
        ['apple', 'apricot', 'banana', 'orange', 'strawberry']
        >>> fruit.sort(reverse=True)
        >>> fruit
        ['strawberry', 'orange', 'banana', 'apricot', 'apple']

--

### List 與參照

當使用賦值運算子 (`=`) 於 list，一個參照將會建立並指向回原 list：

    >>> l = [10, 5, 25, 100, 250, 1, 8]
    >>> l
    [10, 5, 25, 100, 250, 1, 8]
    >>> l2 = l
    >>> l2
    [10, 5, 25, 100, 250, 1, 8]
    >>> l.append("BOOM!")
    >>> l
    [10, 5, 25, 100, 250, 1, 8, 'BOOM!']
    >>> l2
    [10, 5, 25, 100, 250, 1, 8, 'BOOM!']

--

根據前面範例所展示，`l2` 不是 `l` 的副本, 而是一個指向原 `l` 的參照。
若要建立一個 list 的副本，要使用切片運算子 (`[:]`)：

    >>> l3 = l[:]
    >>> l3.append(9876)
    >>> l3
    [10, 5, 25, 100, 250, 1, 8, 'BOOM!', 9876]
    l
    >>> [10, 5, 25, 100, 250, 1, 8, 'BOOM!']

--

記得這種語法所產生的副本是屬於淺層副本：

    >>> numbers = [10,20,30]
    >>> l = [numbers, "x", "y"]
    >>> l
    [[10, 20, 30], 'x', 'y']
    >>> l2 = l[:]
    >>> l2
    [[10, 20, 30], 'x', 'y']
    >>> l2.append("z")
    >>> l2
    [[10, 20, 30], 'x', 'y', 'z']
    >>> l
    [[10, 20, 30], 'x', 'y']
    >>> # 問題來了：
    >>> numbers.append(9999)
    >>> l
    [[10, 20, 30, 9999], 'x', 'y']
    >>> l2
    [[10, 20, 30, 9999], 'x', 'y', 'z']


(請使用 `copy.deepcopy` 建立深層副本以避免上述問題)

--
###### 練習

[Lists exercises](http://lms.10x.org.il/item/148/)

---

# Tuple
<!-- .slide: data-background="img/tulips.jpg" -->

--
### 綜觀
- **不可改變**
- Tuples 用來群組有序性的資料
- 支援索引與切片語法
- 強大的賦值語法 (packing/unpacking)
- 建立的速度比 list 快
- 可做來雜湊！ (這個我們晚點再談)

--
### 建立一個 tuple
    >>> t = tuple()
    >>> type(t)
    tuple

    >>> t = (1, 2, 'hi')
    >>> type(t)
    tuple

    >>> t = 1, 2, 'hi' # 要小心
    >>> type(t)
    tuple

    >>> t = tuple([1,2,'yo'])
    >>> t
    (1, 2, 'yo')

--

### 強大的賦值語法

    x, y = 'hi', 'man'
    x, y = y, x
    print(x, y)

    # output
    man hi
---

# Dictionary
<!-- .slide: data-background="img/dictionary.jpg" -->

--
### 基礎
- 一個 dictionary 是一個雜湊對照表:
  - 它會雜湊 key 的值，用來查找對應的 value 值
  - Key 必須是不可變動的，這樣它的雜湊也才不會變動
- `dict()` 與 `{}` 是空的 dictionaries
- `d[k]` 存取 `k` 這個 key 所對應的 value 值
- `d[k] = v` 更新 `k` 這個 key 所對應的 value 值

--
### 方法
- `len()`, `in`, 與 `del` 運作皆跟 list 一樣
- `d.keys()` 與 `d.values()`回傳 keys 與 values 的列表
- `d.items()` 產生 tuple `(k,v)` 的列表
- `d.get(k, x)` 查找 `k` 這個 key 所對應的 value 值。若有找到則回傳該 value 值，否則回傳 `x`
- `d[k] = x` 建立該 key `k` 與 value `x`；若該 key 存在則直接修改對應的 value 為 `x`
- `d.pop(k, x)` 回傳並移除 key `k` 與對應的 value 值；若該 key 不存在則回傳 `x`

--
### 取代 switch 陳述式
- Python 並沒有 `switch(x)` 陳述式, dictionary 可用來實作其行為
- 可用 dictionary 查找取代冗長的 `if x = a: elif x = b: elif...`

--
###### 練習

[Dictionaries exercises](http://lms.10x.org.il/item/37/)


---

# Set
<!-- .slide: data-background="img/set.png" -->

--
### 基礎
- 沒有順序，不能重複
- 每個元素皆需為不可變動的型別
- 建立一個空的 set: `set()` 而不是 `{}` (這意思是建立一個空的 dictionary)
- `{1, 'blah', 5, -1}`
- 轉換成 list 即可重複： `list(set(lst))`

--
### 方法
- `s.add(v)`: 新增 `v` 至 set 中
- `s.remove(v)`：移除 `v`。若 `v` 不存在於 `s` 中則 **會** 引發例外
- `s.discard(v)`：移除 `v`。若 `v` 不存在於 `s` 中則 **不會** 引發例外
- `s.difference(s2)` 或 `s - s2`：存在於 `s` 但不存在於 `s2` 的所有元素
- `s.union(s2)` 或 `s | s2`：存在於 `s` 或 `s2` 的所有元素
- `s.intersection(s2)` 或 `s & s2`：存在於 `s` 與 `s2` 的所有元素
- `s.update(s2)` 或 `s = s | s2`: 將 `s2` 的元素新增至 `s` 中，重複者取代之

--
##### 進階練習

[Sets vs. Lists](http://lms.10x.org.il/item/90/)

---

# Comprehensions!
<!-- .slide: data-background="img/sequences.jpg" -->

--
### List Comprehensions
- 使用一行語法來對可疊代的物件做處理。
- `[expr for v in iter]`
- `[expr for v in iter if cond]`
- 這個：

        res = []
        for v1, v2 in lst:
            if v1 > v2:
                res.append(v1 * v2)

- 變成這個：

        res = [v1 * v2 for v1, v2 in lst if v1 > v2]


--
### 巢狀的 List Comprehensions
- 這個：

        res = []
        for y in lst2:
            inter = []
            for x in lst1:
                inter.append(x)

- 變成這個：

        [[x for x in lst1] for y in lst2]


--
### Dictionary Comprehensions
- 語法像 list，只是將 `[]` 換成 `{}`。
- 這個：

        d = dict()
        for k, v in lst:
            d[k] = v

- 變成這個：

        {k: v for k,v in lst}


--
### Set Comprehensions
-   語法像 dictionary 但沒有 `:`
-   這個：

        s = set()
        for x in lst:
            s.add(x)

- 變成這個：

        {x for x in lst}


--
### Tuple Comprehensions？

        tup = (x for x in lst)
        type(tup)
        <class 'generator'>

- 我們晚點會談到 generators

---

# 模組 builtins 中可用於疊代物件的方法

--

- `len(x)`: 元素數量
- `sum(x)`: 加總所有元素
- `a in x`: 檢查是否存在
- `all(x)/any(x)`: 若 所有/任一 元素為真則回傳 True

--

- `max(x)/min(x)`: 最大/最小 元素
- `reversed(x)`: 回傳一個新的可疊代物件，元素順序是 `x` 的反序 (不能用在 set，為何？)
- `zip(x,y)`: 將 `x` 和 `y` 的元素依序組成多個 tuple 的 list
- `sorted(x)`: 回傳一個新的 list，其元素順序已排序

--
###### 練習

[Comprehensions exercises](http://lms.10x.org.il/item/41/)
