# 物件導向
<!-- .slide: data-background="img/3D-Object-Pictures.jpg" -->

--

### class 陳述式

    class Foo:        #python2 Foo(object):
        pass

- `class Foo` &srarr; `class Foo(object)`
- 類別是用來定義一個新物件的方法
- 建立一個新類別物件，名稱叫作 Foo
- 類別定義會產生一個新的命名空間 (scope)
- 定義在類別內的變數為 *類別參數*
- 定義在類別內的函式為 *實體方法*

--
### 建構子

    class Circle:
        def __init__(self, radius):
            self.r = radius

- `__init__` 初始化一個類別實體
- `x = Circle()`
    - 建立一個類別為 `Circle` 的物件
    - 呼叫 `Circle.__init__(self, radius)`
    - 將 self 綁定至名稱 x

--

### 實體方法

    class Circle:
        def __init__(self, radius=5):
            self.r = radius
        def get_perimter(self, a, b):
            return 2 * math.pi * self.r

-   實體方法的定義必須使用 self 作為第一個參數

--
### 私有方法的慣例語法

-   開頭為底線的 `_` 變數名稱意思是：若要直接使用它風險自負
-   "We're all adults here"：你可以存取任何你想存取的變數，但請自律

        class Circle:
            _pi = 3.14
            ...

            def get_perimter(self):
                return 2 * self._pi * self.r

--
###### 練習
[Python Classes](http://lms.10x.org.il/item/46/)

---

# 繼承
<!-- .slide: data-background="img/William_Hogarth_Inheritance.jpg" -->
From William Hogarth's [A Rake's Progress](http://en.wikipedia.org/wiki/A_Rake%27s_Progress).
"The Young Heir Takes Possession Of The Miser's Effects".
--

### 單一繼承

    class Circle(Shape):
        def __init__(self):
            super().__init__()     # python2 super(Circle, self).__init__()
            self.new_var = default

- 父類別是 `class` 陳述式中作為參數傳入的
- `object` 是預設的父類別 (base class)
- `class Circle(Shape)`：繼承 Shape 類別
- 記得要呼叫父類別的 `__init__` 方法

--

```python
class Animal:
    sound = None
    def make_sound(self):
        print(self.sound)

class Cat(Animal):
    sound = "meow"

class Duck(Animal):
    sound = "quack"

c = Cat()
c.make_sound()

d = Duck()
d.make_sound()
```

--

```python
class TitleRenderer:
    def render(self, s):
        return "* {} *".format(s)


class UppercaseTitleRenderer(TitleRenderer):
    def render(self, s):
        return super().render(s).upper()
        # in python2:
        # return super(UppercaseTitleRenderer, self).render(s).upper()


t = TitleRenderer()
print(t.render("hello"))

u = UppercaseTitleRenderer()
print(u.render("hello"))
```

--

##### 進階
## 多重繼承

    class Circle(Shape, Drawable):
        def __init__(self):
            super().__init__(self)

- 你可以繼承多個父類別
- 參數查找將會使用 MRO (Method Resolution Order) 順序，先找到的先用
- `Circle.mro()`

--

###### 練習
[Class inheritance](http://lms.10x.org.il/item/116/)

---

##### 進階
# Python 魔法！ (方法)
<!-- .slide: data-background="img/magic_mist.jpg" -->

--
## Magic Methods

- *語法糖衣* 是使用 magic methods 達成
- 凡方法名稱是命名為 `__method_name__` 皆是 "magic"
- 像是 `f()` 與 `seq[i]` 都是 magic method 呼叫

--

## __new__, __init__, __call__
- `x = C()` &srarr; `x = C.__init__(C.__new__())`
    - `__new__` 建立新實體
    - `__init__` 初始化該實體
- `x(arg,...)` &srarr; `x.__call__(arg,...)`

--

## __str__, __repr__
- `str(x)` &srarr; `x.__str__()`
    - 回傳人類易讀易懂的字串
- `repr(x)` &srarr; `x.__repr__()`
    - 回傳該物件的字面語法


--

## 比較
- `x < y` &srarr; `x.__lt__(y)`
- `x > y` &srarr; `x.__gt__(y)`
- `x <= y` &srarr; `x.__le__(y)`
- `x >= y` &srarr; `x.__ge__(y)`
- `x == y` &srarr; `x.__eq__(y)`
- `x != y` &srarr; `x.__ne__(y)`

--

## 數學運算子
- 所有數學運算子都有 magic methods
- `__add__, __sub__, __mod__, __xor__, ...`
- 對於 += 與其他額外的運算子也有對應的 magic methods

---

##### 進階
# 進階主題

--
### 參數查找
- `Foo.__dict__` 是一個存放類別參數的 dictionary
- `Foo.val` 會轉譯成 `Foo.__dict__['val']`
- 當執行 `x = Foo()` 後 `x.__dict__` 會存放實體參數
- x.val 轉譯成：
    - `x.__dict__['val']` 如果 val 是一個實體參數
    - `Foo.__dict__['val']` 如果沒有名為 val 的實體參數，但存在名為 val 的類別參數

--

### 靜態方法

    class Circle:
        @staticmethod
        def radius_to_perimeter(r):
            return 2 * math.pi * r

-   讓方法依附至類別本身 (with similar context)
-   靜態方法不需傳入 self 參數
-   靜態方法不該相依於任何類別參數

--

### 類別方法

    class Circle:
        @classmethod
        def from_circumference(cls, circ):
            return cls(circ/(2 * math.pi))

- 一個類別方法將類別物件視做第一個參數傳入
- 可用來實作另一種建構子。
- 呼叫第一個參數 cls。

--

### 私有參數

- `__`
    - 開頭為 __ 是用來避免繼承的類別意外的覆蓋掉父類別同名的參數
    - 它觸發以下的名稱變動 (*name mangling*) 以避免上述意外：
        - `__some_var` &srarr; `_classname__some_var`
        - classname 是類別名稱，附加在原定義的 `__some_var` 參數名稱之前
    - 如果你知道類別名稱與變數名稱，也可以自己實作這行為

--

## 沒有 getters 與 setters？？？
- Python 的 `@property` 與 `@attr.setter` 取代了 getters 與 setters 的需求
- 使用 `@property` 裝飾方法來取代 attribute getter
    - 執行 `x.attr` 時會被呼叫
- 使用 `@attr.setter` 裝飾方法來取代 attribute setter
    - 執行 `x.attr = val` 時會被呼叫

--

```
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return self.radius ** 2 * math.pi

c = Circle(2)
print(c.area)
```

--
## `Super` - 深入研究

- `super(cls, obj)` &srarr; `super(C, self)`
    - 如果你想要在類別外呼叫 super 時可以使用此語法，傳入類別名稱與對應的實體。
    - 被呼叫的類別將是該實體物件的 MRO 順序最前的那一個
    - 它是被綁定的 &srarr; 實體物件將會被插入方法呼叫
- `super()`
    - 可用在該類別的實體方法中，可調用其父類別。

--
## getattr
- `x.value` &srarr; `getattr(x, 'value')`
- 當參數名稱是在 runtime 時產生時很有用
- `getattr(self, name)` 呼叫 `__getattribute__(self, name)`，若不存在則再呼叫 `__getattr__(self, name)`
- 定義 `__getattr__` 在需要指定預設值時很有用
- `getattr(x, 'value', default)` 讓你在所有呼叫都失敗時仍然有個預設值
