<!-- .slide: data-background="img/monty-python.jpg" -->
# 簡介

### Pycubator

---

## Python？

--

* 動態型別
* 多種範式
* 直覺的語法
* 直譯式
* 高階的資料類型
* 折衷於 shell script 與 C++/Java 程式語言？！？

--

### 為何要學 Python？

* 簡單易學 (參考 [Python 現在已是全美頂尖大學最受歡迎的入門程式語言][usage])
* 非常成熟的程式語言與開發社群，目前被 Google、Facebook(Instagram)、Microsoft、Dropbox 等大型企業使用。
* 活躍於各種領域 - 網站開發、資料科學、系統管理維運、自動化、人工智慧，族繁不及備載。

[usage]: http://cacm.acm.org/blogs/blog-cacm/176450-python-is-now-the-most-popular-introductory-teaching-language-at-top-us-universities/fulltext

--

### 一些歷史

--

![](img/guido.jpg)

這位就是 Guido Van-Rossum，Python 創造者 ^^

--

"讓我自我介紹一下。我是一位宅宅，一位技客。搞不好我有某種程度上的自閉。
我也是屬於大器晚成型的。我於 26 歲時大學畢業，45 歲時結婚。
現在我 60 歲了，有個 14 歲的小孩... 我不是 Steve Jobs 也不是 Mark Zuckerberg。但我在 35 歲時
我創造了一個程式語言並引起了一些關注。之後的發展讓人驚奇不已..."

Guido 的 [king's day 演說][speech]

[speech]: http://neopythonic.blogspot.co.il/2016/04/kings-day-speech.html

--

### Python 是如何發展的？
* [自願開發者][core-dev] 社群，也被稱作核心開發者 ([你也可以成為一員][be-core-dev])
* 經由公開透明的 Python Enhancement Proposals ([PEPs][PEPs])

[PEPs]: https://www.python.org/dev/peps/
[core-dev]: https://hg.python.org/committers.txt
[be-core-dev]: https://docs.python.org/devguide/coredev.html

---

## Python 之禪

--

* 美麗優於醜陋，明講好過暗喻。
* 簡潔者為上，複雜者次之，繁澀者為下。
* 平舖善於層疊，勻散勝過稠密；以致輕鬆易讀。

--

### Java

    public class Hello{
      public static void main(String[] args){
        System.out.println("哈囉，世界！");
      }
    }

--

### C++

    #include <iostream>

    int main(){
      std::cout << "哈囉，世界！" << std::endl;
      return 0;
    }
--

### Python

    print('哈囉，世界！')

--

### 其他 Python 之禪
* 最好只有一種明確的寫法
* 清晰優於速度
* 我們都是深思熟慮的開發者

---

## 重要的分歧
#### Python2 vs. Python3

--
### 時間軸

* 1989 年 12 月：Guido Van Rossum 開始 Python 實作
* 1994 年 01 月：1.0 版釋出
* 2000 年 10 月：2.0 版釋出
* 2008 年 12 月：3.0 版釋出
* 2009 年 06 月：3.1 版釋出
* 2010 年 07 月：2.7 版釋出 (含 backports)
* 2018 年 07 月：目前的 Python 版本為 2.7.15 與 3.7.0

--

###  為何要 Python 3？
* Guido 想要更動一些語言上的設計 (主要是字串編碼)
* Google 提供贊助
* (某種程度上的) 新的語言因此誕生

--

### Python 3 沒有向後相容！

* `print` 與 `exec` 變成函式
* 大量使用 generators 取代 lists
* 所有 text (str) 使用 Unicode 編碼，encoded text (bytes) 是二進位編碼
* 其他標準函式庫較小的變動

--

### 所以為何使用 Python 3？

* 更適切的編碼
* 非同步程式設計 (`async/await`)
* 標準函式庫內建虛擬環境
* `__pycache__` 目錄
* 限定關鍵字參數

還有很多很多功能，但我們稍候再來了解...

---
## 撰寫程式工具

---

## The REPL
(Read Evaluate Print Loop)

--
### The REPL

    $ python3
    Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
    [GCC 6.3.0 20170118] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> print('哈囉世界！')
    哈囉世界！

* 在 *nix 系統中，執行 `ctrl+d` 離開，在 Windows 上則執行 `ctrl+z`。

--

### 為何我該用它？？

* 快速！
* 可用來確認 Python 的行為
* 但... 在寫多行程式時支援度不是很好 (比如類別、函式)

--

###### 練習
### 將 Python 當作計算機

* 試試在 python shell 中執行以下指令：

        >>> 10 + 10
        20
        >>> 50 * 2
        100
        >>> 10 + 20 * 3
        70
        >>> (10 + 20) * 3
        90

* `**` 的用途是什麼？
* `%` 的用途是什麼？
* `import this` 的用途是什麼？

---

## IPython
### (強化版 REPL)

--
```bash
$ ipython
Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 
```

--

### 酷炫的功能

* 使用 `tab` 自動補全。
* 在變數、函式、類別名稱等末端加上 `?` 可取得說明。
* 可在 IPython 裡面執行一般的 shell 命令：`!ls`
* `%magic`指令很酷。試試`%history`、`%save`以及`%pastebin`。


---

## .py 檔案

--

* Python 原始檔案
* (不需要編譯)

--

### .py 檔案

![gedit](img/gedit-hello-world.png)

    $ python /tmp/example.py
    hello world!

---

## IDE

--

### PyCharm

-   [PyCharm 網站](https://www.jetbrains.com/pycharm/)
-   可以混用 python 2 與 python 3。
-   有提供商業版與社群版可供下載。

--

### Pycharm 快捷鍵
-   使用 `Alt+Enter` 來快速修正，包含 *自動加入 import 敘述* (這很好用)。
-   使用 `Ctrl+Shift+A` 尋找任何指令或是設定！
-   使用 `Ctrl+Alt+L` 重新編排程式。

--

-   使用 `Ctrl+Shift+F10` 執行現在的檔案。
-   使用 `Shift+F10` 再次執行上次最後編輯的檔案。
-   使用 `Ctrl+Space` 自動補全函式/變數等。

---

## 語法風格指南

--

-   Python 社群非常重視可讀性
-   這也是為何 [PEP 8][pep8] 規範被提出
-   這份規範定義了 Python 程式碼 **看起來應該長怎樣**

[pep8]: https://www.python.org/dev/peps/pep-0008/


---

##### 進階議題
## 來點理論

--

### 什麼是直譯？

* "直譯"程式語言是什麼意思？
* "直譯"與"編譯"指的是實作方式，不是語言本身
* 最被廣泛被使用的 Python 實作 (CPython) 混合了上述兩個階段：
    * 將原始碼編譯成位元組碼 (.pyc 檔案)
    * 直譯位元組碼，一步一步的執行
    * 不需編譯成機器碼
    * 當然，也可以直接執行原始碼
