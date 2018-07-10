# Pycubator

英文原始版的投影片可在 [pycubator.com][pyc] 瀏覽觀看。

Pycubator (Python 孵化器課程) 是由一系列的投影片與練習題所組合而成。
這些投影片希望可以用在教師帶領的教學課程，也希望可以強化學生探索與參與的可能性。

本課程使用 [RevealJS][rjs] 產生漂亮的投影片，且內容其實是使用 Markdown 語法撰寫，所以非常容易搭配版控使用，練習使用 [Jupyter notebooks][jn] 以降低學生需撰寫重複程式碼的狀況。

Pycubator 宗旨如下：

-   少說，多練。
-   真實環境的範例

## 在本機執行
-   執行 `pipenv install` 安裝相依的套件。
-   執行 `pipenv shell` 進入虛擬環境。
-   執行 `python3 build.py` 產生 HTML 檔案。
-   執行 `git submodules init` 將 reveal.js 相依引入。
-   執行 `git submodules update` 同步 reveal.js 的 repo 並放至 `docs/revealjs` 目錄。
-   執行 `cd docs && python3 -m http.server` 並開啟瀏覽器瀏覽！

## 如何貢獻
-   投影片位在 `docs/slides/` 且為 MD 格式，所以非常容易編輯。
-   練習題為 Jupyter (IPython) notebooks ，位在 `docs/exercises` 。
-   若有修改，參照 [running locally](#running-locally) 產生新版內容。

## 貢獻者
* [Noam Elfanbaum](https://twitter.com/noamelf)
* [Udi Oron](https://twitter.com/nonZero)

## 翻譯者
* [William Wu](https://github.com/williamwu0220)

---

[![本課程使用 Creative Commons Attribution-ShareAlike 4.0 International 授權][cc-img]][cc-site]


[cc-img]: https://i.creativecommons.org/l/by-sa/4.0/88x31.png
[cc-site]: http://creativecommons.org/licenses/by-sa/4.0/

[gitter-img]: https://badges.gitter.im/Join%20Chat.svg
[gitter-site]: https://gitter.im/noamelf/pycubator?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

[rjs]: https://github.com/hakimel/reveal.js/
[jn]: http://jupyter.org/
[pyc]: http://pycubator.com

