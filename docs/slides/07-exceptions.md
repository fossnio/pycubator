# 例外
<!-- .slide: data-background="img/puzzles.jpg" -->

---

# 捕捉例外

--

### Python 使用例外來處理所有的錯誤。

例外是一種用來警示發生錯誤或其他非正常的狀況的機制。

--
### 捕捉例外

    try:
        execute_some_code()
    except SomeException:
        handle_gracefully()

--

### 捕捉所有例外

    try:
        execute_some_code()
    except:
        handle_gracefully()


--

-   不要這樣做。
-   捕捉太廣泛的例外狀況有時候蠻危險的。
-   別的就不先講，這種 "廣泛" 的處理將會捕捉到：
    -   system exit triggers
    -   記憶體錯誤
    -   打錯字
    -   其他你沒想到的狀況

--
###### 練習
### 被 0 除

-   試試看除式 `1/0` 。會發生什麼事？
-   試試看捕捉這個例外並告知使用者不能除以 0。

--
### 捕捉多個例外

用一樣的方式處理它們

    try:
        execute_some_code()
    except (SomeException, AnotherException):
        handle_gracefully()


--

個別處理它們

    try:
        execute_some_code()
    except SomeException:
        handle_gracefully()
    except AnotherException:
        do_another_thing()

---

# LBYL vs. EAFP

--
### LBYL

Look Before You Leap

> \[...\] 在呼叫或查找之前明確的對前提條件做測試。
這種風格跟 EAFP 對比起來，它的特色是會有很多 if 敘述存在。

--

### EAFP
Easier to Ask for Forgiveness than Permission
> \[...\] 假設一切前提條件都是沒問題，若假設是錯誤的，使用例外捕捉處理。
這種乾淨且快速的程式碼風格會出現許多 try 與 except 敘述。
這種程式碼風格和 LBYL 風格形成對比，而後者是其他程式語言中常見的，像是 C。

--

### Examples
-   LBYL:

        import os
        if os.path.exists('tmp.txt'):
            with open('tmp.txt'):
                pass

-   EAFP:

        try:
            with open('tmp.txt'):
                pass
        except IOError as e:
            print(e)

--

### When to use
>"所有的錯誤皆是例外，但並非所有的例外皆是錯誤"

使用例外處理來優雅的處理應用程式的錯誤。
但是：使用例外處理來處理應用程式的控制流程是完全被允許，甚至勢必要的。
比如 EOFError。

---

# 引發例外、取用例外物件、與往外拋出例外 

--

### 引發例外

例外可使用 `raise <exception>` 語法引發，也可以夾帶選用的參數。

    raise RuntimeError()
    raise RuntimeError("錯誤訊息")

--

### 取用例外

使用 "as" 去取用例外物件

    try:
        raise RuntimeError("o hai")
    except RuntimeError as e:
        print(e)


--

### 往外拋出例外

Try 區塊可以是巢狀的；
所有往外拋出的例外若沒有任何攔截，會一路傳遞到最上層的 "root 例外處理常式"。

    try:
        try:
            raise Exception
        except Exception:
            print('Inner')
    except Exception:
        print('Outer')


(預設的) root 例外處理常式會停止 Python 的行程。

--

### 往外拋出例外

往外拋出例外可以使用 raise 不帶任何參數觸發，
這將會重複拋出最近一次的例外。

    try:
        try:
            raise Exception
        except Exception:
            print('Inner')
            raise
    except Exception:
        print('Outer')


這在某些情況下很有用，比如紀錄例外。

--
### 練習

-   讀入檔案 [numbers.txt](content/exercises/numbers.txt)。
-   將檔案中的整數都讀入，並在最後加總並印出。
-   你必須預期有以下的例外，並讓使用者知道：
    - `IOError`：如果開啟檔案發生問題。
    - `ValueError`：如果讀入的該行不是整數。
    - 其他狀況：如果有其他例外被引發，捕捉它並顯示 '未預期的例外發生了'。

---

# Finally 與 Else

--
### Finally
在 `finally` 區塊中的程式碼一定會被執行 (除非 Python 行程整個掛了)。

    try:
        open_file()
    except IOError:
        print('抓到例外')
    finally:
        close_file()

--

### Else
在 `else` 區塊的程式碼若沒有例外被引發時才會執行。

    try:
        open_file()
    except IOError:
        print('抓到例外')
    else:
        print('一切正常沒有例外發生')

---

# 撰寫例外

--
### 繼承
-   例外將被捕捉，如果處理例外時指定例外，則繼承自該例外的子類別皆會被捕捉。
    -   RuntimeError
    -   StandardError
    -   Exception
    -   BaseException

--

### 例外比對
- 例外的繼承關係是可以自行設計的。
- 比如 `OverflowError`, `ZeroDivisionError` 與 `FloatingPointError` 都是繼承自 `ArithmeticError`。
- 只要寫個常式去處理 `ArithmeticError` 就可以一網打盡。

--

### 自己寫一個
這很簡單只要這樣

    class MyException(Exception):
        pass

--
###### 練習
### 寫自己的例外！
-   建立一個函式名為 `guess_my_name`：
    -   處理使用者的輸入
    -   確認使用者是否猜對你的名字
    -   如果沒猜對，拋出 `NotMyName` 例外

-   呼叫這個函式：
    -   在 while 迴圈中，呼叫該函式，
    -   如果 `NotMyName` 例外被捕捉則繼續在迴圈內執行。
    -   否則印出 '成功！' 並離開。
