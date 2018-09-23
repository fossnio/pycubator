# 單元測試
### Pycubator

--
### 為何？

-   愈早修正錯誤成本愈低。
-   在單元測試所找到的錯誤，其成本比功能測試階段才找到的錯誤低 10 倍
-   比在系統或整合測試階段才找到錯誤的成本低 40 倍

--

### 什麼是單元測試？


-   針對程式的某部份行為做的隔離單元測試
-   測試單一行為
-   對於任何原因所產生的錯誤可簡明的確認其發生原因
-   可作為程式預期行為的文件
-   執行快速

--

### 如滿足以下條件之一，則該測試就不算是單元測試：

*   它存取資料庫
*   它存取網路
*   它存取檔案系統
*   它不能跟其他單元測試同時執行
*   你必須針對運行環境做一些特殊調整 (比如編輯設定檔) 才能運行它

來源： [Michael Feathers' blog](http://www.artima.com/weblogs/viewpost.jsp?thread=126923) (2005)

---

# 單元測試展示

--

### 聯集

-   我們來寫一個可將兩個 lists 聯集的函式
-   其中一個 list 長度比另一個長是沒問題的
-   在我們開始寫程式碼以前，我們應該要知道這個函式應該會滿足以下行為：

        interleave([], []) # -> []
        interleave([1,5,3], ["hello"]) # -> [1,"hello",5,3]
        interleave([True], [[], 8]) # -> [True, [], 8]

--

-   先寫測試， `interleave_test.py`:

        from interleave import interleave
        import unittest

        class TestGettingStartedFunctions(unittest.TestCase):
            def test_interleave(self):
                cases = [
                    ([], [], []),
                    ([1], [9], [1, 9]),
                    ([2], [7, 8, 9], [2, 7, 8, 9]),
                ]

                for a, b, expected in cases:
                    self.assertEqual(interleave(a, b), expected)

        if __name__ == '__main__':
            unittest.main()


--

-   寫一個 stub `interleave.py`:

        def interleave(a, b):
            return None

--

-   執行測試

        $ python interleave_test.py
        F
        ======================================================================
        FAIL: test_interleave (__main__.TestGettingStartedFunctions)
        ----------------------------------------------------------------------
        Traceback (most recent call last):
          File "interleavetest.py", line 15, in test_interleave
            self.assertEqual(interleave(a, b), expected)
        AssertionError: None != []

        ----------------------------------------------------------------------
        Ran 1 test in 0.000s

        FAILED (failures=1)

--

-   現在來寫程式碼

        def interleave(a, b):
            """Return the interleaving of two sequences as a list."""
            return [y for x in izip_longest(a, b) for y in x if y is not None]

--

-   再測試一次

        $ python interleave_test.py
        E
        ======================================================================
        ERROR: test_interleave (__main__.TestGettingStartedFunctions)
        ----------------------------------------------------------------------
        Traceback (most recent call last):
          File "interleavetest.py", line 15, in test_interleave
            self.assertEqual(interleave(a, b), expected)
          File "/Users/raytoal/scratch/interleave.py", line 3, in interleave
            return [y for x in izip_longest(a, b) for y in x if y is not None]
        NameError: global name izip_longest is not defined

        ----------------------------------------------------------------------
        Ran 1 test in 0.000s

        FAILED (errors=1)
--

-   修正程式碼

        from itertools import izip_longest

        def interleave(a, b):
            """Return the interleaving of two sequences as a list."""
            return [y for x in izip_longest(a, b) for y in x if y is not None]

--

-   重跑測試

        $ python interleave_test.py
        .
        -------------------------------------------------------------
        Ran 1 test in 0.000s

        OK

---
# 資源與練習

--
### 資源
-   Ray Toal, [unittest in 5 minutes](http://www.slideshare.net/raytoal/unittest-in-5-minutes)
-   Python stdlib [documentation](https://docs.python.org/3/library/unittest.html#module-unittest)


--
###### 練習
[Unit testing](http://lms.10x.org.il/item/47/)
