
# 標準函式庫

---

# Time

--

-   `time.time` epoch 至今的秒數，以浮點數回傳之。

        import time
        t0 = time.time()
        for i in range(10000000):
            pass
        t1 = time.time()
        print(t1 - t0)

        # 輸出：
        1.1572110652923584

--

-   `time.sleep` 暫停執行傳入的秒數>

        import time
        print('處理中，請等待...')
        time.sleep(2)
        print('完成。')

        # 輸出：
        處理中，請等待...
        完成。

---

# Logging

--
### Logging

-   我們需要更完整的傾印機制以用在大型且長時間執行的程式中。
-   ogging 套件讓我們更容易的在程式中紀錄目前的狀態與時間戳記。

--

-   基本用法：

        logging.debug('Alltems operational')
        logging.info('Airspeed knots')
        logging.warn('Lowfuel')
        logging.error('Nol. Trying to glide.')
        logging.critical('Glide attempt failed. About to crash.')

        # 輸出：
        WARNING:root:Lowfuel
        ERROR:root:Nol. Trying to glide.
        CRITICAL:root:Glide attempt failed. About to crash.

-   為何我們看不到 `debug` 與 `warning` 訊息？

--

-   我們可以使用 `setLevel` 來設定紀錄的傾印等級

        logging.root.setLevel(logging.DEBUG)
        logging.debug('Alltems operational')
        logging.info('Airspeed knots')

        # 輸出：
        DEBUG:root:Alltems operational
        INFO:root:Airspeed knots

--

-   我們可以使用 `basicConfig` 來客製化紀錄以符合我們的需求。
-   比如我們可以讓紀錄提供更多資訊：

        logging.basicConfig(format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d]  %(message)s',
                            level=logging.DEBUG)
        logging.debug("你現在會看到更多的資訊了...")

        # output
        [DEBUG 2015-07-14 22:59:59,160 <ipython-input-60-8bd2b8d57226>:5]  你現在會看到更多的資訊了...

--

-   或是紀錄到檔案中：

        logging.basicConfig(filename='example.log',level=logging.DEBUG)
        logging.debug('這行訊息會紀錄到檔案中')

--

-   資源：
    -   [Logging module docs](https://docs.python.org/3.5/library/logging.html)
    -   [Logging howto](https://docs.python.org/3.5/howto/logging.html)
    -   [Become a Logging Expert in 30 Minutes](https://youtu.be/24_4WWkSmNo), Gavin M. Roy, PyCon 2013

---

# OS

--
### OS
-   `os.listdir` 回傳指定目錄下所有檔案與目錄的 list：

        import os

        for filename in os.listdir('.'):
            print(filename)

        # 輸出
        The-standard-library.ipynb
        example.log
        unit-tests.ipynb

--

-   `os.path.join` 連結路徑 (根據 OS 決定)：

        import os

        home = '/home/user'
        os.path.join(home, 'Downloads')

        # 輸出
        '/home/user/Downloads'

-   `os.path.splitext` 依據檔案延伸副檔名分割路徑：

        os.path.splitext('/home/noam/Downloads/xom.csv')

        # 輸出
        ('/home/noam/Downloads/xom', '.csv')

--

-   `os.path.getsize`

        os.path.getsize('The-standard-library.ipynb')

        # 輸出
        8440



-   `os.path.isdir`

        os.path.isdir('The-standard-library.ipynb')

        # 輸出
        False

---

# Sys 與 argparse

--
### Sys
- `sys.argv[0]` 包含本身檔名
- `sys.argv[1:]` 包含命令列參數（如果有的話）

--

#### 範例
-   test.py:

        import sys

        def main(argv):
            a = int(argv[1])
            b = int(argv[2])
            return a + b

        if __name__ == '__main__':
            print(main(sys.argv))

-   命令列：

        $ python test.py 5 10
        15

--

### argparse
-   標準函式庫中用來處理指令稿的命令列參數
-   產生求助訊息Generates help messages
-   強固且清晰
-   更多資訊請參考 [argparse tutorial](https://docs.python.org/3/howto/argparse.html)
--

### argparse 範例
-   test.py:

        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument("二次方",
                            help="顯示參數的二次方運算結果",
                            type=int)
        args = parser.parse_args()
        print(args.square**2)

-   命令列：

        $ python3 test.py 4
        16

--

###### 練習

[The standard library](http://lms.10x.org.il/item/144/)

---

# Subprocess

--

Subprocess 模組提供了一致性的介面以用來建立與協同其他的行程。

--
### 簡單呼叫
-   若要呼叫外部指令且不與其互動，則使用 `call()` 函式。

        import subprocess

        subprocess.call(['ls', '-1'], shell=True)

--

-   `call()` 的回傳值就是程式執行結束的 exit code。
-   呼叫者有責任去確認回傳值以檢驗是否有錯誤發生。

--
### 錯誤處理

-   `check_call()` 函式運作跟 `call()` 相同，並會額外檢查回傳值，若有錯誤則引發 `CalledProcessError` 例外。

        import subprocess

        subprocess.check_call(['false'])

--
### 取得輸出
-   因 `call()` 而被呼叫的子行程，其標準輸入輸出會綁定在父行程的輸入和輸出。
-   使用 `check_output()` 以取得輸出以便於後續處理。

        import subprocess

        output = subprocess.check_output(['ls', '-1'])
        print('輸出共有 {} 位元組'.format(len(output)))
        print(output)

---

# Threading

--

-   使用 Thread 最簡單的方法就是傳入要執行的函式並實體化它，然後呼叫 `start()` 使其開始運作。

        import threading

        def worker(num):
            """thread worker function"""
            print('Worker: {}'.format(num))
            return

        for i in range(5):
            t = threading.Thread(target=worker, args=(i,))
            t.start()

--

-   很多時候我們會執行眾多個執行序，並希望主行程可以蒐集它們的執行結果，那可以用 `join` 方法：

        import threading, random, time

        def worker(num, sleep):
            print('Worker #{} 開始休眠 {} 秒 '.format(num, sleep))
            time.sleep(sleep)
            print('Worker #{} 醒來 '.format(num))
            return

        threads = []
        for i in range(5):
            sleep_time = random.randint(1,5)
            t = threading.Thread(target=worker, args=(i, sleep_time,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

---

### 參考連結
-   [pymotw](https://pymotw.com/2/) - Python module of the week
-   Standard Library [documentation](https://docs.python.org/3/library)
