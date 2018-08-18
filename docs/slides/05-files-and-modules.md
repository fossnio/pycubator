# 檔案與模組
### Pycubator

---

# 檔案操作
<!-- .slide: data-background="img/files.jpg" -->
The National Archives UK

--
### 開啟檔案

- `open(name, mode)` 回傳一個檔案物件
- `name` 是要開啟的檔案路徑
- `mode`：
    - `'r'` (read): 檔案以唯讀模式開啟
    - `'w'` (write): 檔案以唯寫模式開啟，且檔案內容整個清空重頭開始
    - `'a'` (append): 類似 'w' 但內容不清空，繼續從檔案尾端繼續寫入
    - `'x'`: 類似 'w' 但檔案必須不存在
- `open(name)` 預設為唯讀模式開啟檔案： `open(name, 'rt')`

--
### 關閉檔案
- `f.close()`:
    - 釋放該檔案物件所佔用的資源
    - 將暫存尚未寫入的內容寫入硬碟
- 可配合 `with` 陳述式使用:

        with open('example.txt') as f: # 離開此區塊就自動釋放資源
            print(f.read())

--
### 讀取
- `f.read()` 讀取整個檔案內容 (讀到 `EOF`)
- `f.read(size)` 讀取檔案內容 `size` 個字元

        # 印出每一行內容
        with open('example.txt') as f:
            for l in f:
                print(l)

--
### 寫入
- `f.write(string)` 寫入字串 (沒有 `\n`)
- `f.writelines(sequence)` 寫入序列性的內容 (一樣沒有 `\n`)

        fruits = ['Bannana', 'Melon', 'Peach']
        with open('example.txt', 'w') as f:
            f.writelines(fruits)

--
###### 練習

[Working with files](http://lms.10x.org.il/item/35/)

---

# 模組與套件

--
### import 陳述式

- 可使用其他 python 的檔案與函式庫
- Imports: `import math`
- Named imports: `import math as m`
- Specific imports: `from math import pow`
- Import all: `from math import *` (危險！只用在特別狀況！)

--

### 模組

    # utensils.py
    def eat_soup():
        return 'spoon'

    # main.py (option 1)
    import utensils
    print(utensils.eat_soup())

    # main.py (option 2)
    from utensils import eat_soup
    print(eat_soup())

--
### 套件

-   套件是命名空間，其下可再包含多個套件與模組
-   套件其實就是目錄，但有個地方比較特別：每個套件/目錄下 **必須** 有個檔案叫作 `__init__.py`
-   在 Python 3 中套件目錄下可以不要有 `__init__.py` 但那是 [另一個故事](https://www.python.org/dev/peps/pep-0420/)

--
```python
# fruits/__init__.py
# -- 空的 -- 我是空的 -- 我真的是空的 -- 我真的是一個什麼內容都沒有的空檔案

# fruits/apple.py
def print_it():
    print('apple')

# main.py
from fruits import apple
apple.print_it()
```
--

-   如果一個目錄中有一個 `__init__.py` 檔案，那麼該目錄名稱就可以當作是套件名稱可用來被 import。

        # foo/__init__.py
        def greeting():
            return "Hello World!"

        # main.py
        from foo import greeting
        print(greeting())

--
##### 進階
### 模組是 singletons

    # stuff.py
    fruits = ['Pineapple']

    # module_a.py
    import stuff
    def foo():
        stuff.fruits.append('Apple')

    # module_b.py
    import stuff
    def foo():
        stuff.fruits.append('Banana')

--

    # program.py
    import module_a, module_b, stuff
    module_a.foo()
    module_b.foo()
    print(stuff.fruits)

    # output
    ['Pineapple', 'Apple', 'Banana']

