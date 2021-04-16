# Autoclimb

## Change log
### Version:
#### Upgrade Method
```bash
Step 1: 更新最新程式碼
    git pull  或者是到 https://github.com/jing-tw/autoclimb 下載最新的程式, 更新你的 local 程式碼 
Step 2: 切到程式執行環境 (如果你不知道, 請到安裝環境)
    conda activate venv_climbing
Step 3: 更新你的執行環境
    pip install openpyxl
Step 4: 執行主程式
    python autoclimb.py
```

#### Change
##### 1. 隊員資料檔
- [fixed] 解決因為第三方套件不支援 xlsx 導致讀取失敗的問題. Act: 新增支援套件. pip install openpyxl 
- [fixed] 解決資料內容全部是空的問題, 導致自動程序中斷問題. Act: 空的資料視為無資料.

##### 2. 玉山國家公園
- [updated] 追加玉山國家公園申請網頁, 新增首頁自動勾選: 4 項
- [updated] 修正玉山國家公園形成安排的變動. Pseudo Plan: 登山口排雲登山服務中心→登山口塔塔加登山口→一般玉山前峰→登山口塔塔加登山口→登山口排雲登山服務中心

##### 3. 太魯閣國家公園
- [new] 追加太魯閣國家公園申請網頁, 新增首頁自動勾選: 1 項

##### 4. 流程優化
- [remove] 移除討厭的對話視窗


### Version: 489c6a8b4c253d8e33a2ab15e14647eaffc58c93
- [add] 新增 team sheet: 可以在 Excel 中, 加入登山隊隊名 (感謝 stanleyatlinc 新增此功能)
- [fix] 修正 日期選項 (感謝 stanleyatlinc 修正此功能)
### Version: older
- [add] 新冠病毒防疫警示自動勾選
- [modify] 使用 PyQt5

## 國家公園入山入園證 成員資料自動填寫工具
[![N|Solid](https://4.bp.blogspot.com/-DAIv22gkCfc/XKG1TTMJ0UI/AAAAAAAAeE4/qddEt243nTwt-7AgdTKqJzb0R897nOG4wCLcBGAs/s1600/Screenshot%2Bfrom%2B2019-04-01%2B14-50-36.png)](https://4.bp.blogspot.com/-DAIv22gkCfc/XKG1TTMJ0UI/AAAAAAAAeE4/qddEt243nTwt-7AgdTKqJzb0R897nOG4wCLcBGAs/s1600/Screenshot%2Bfrom%2B2019-04-01%2B14-50-36.png)

這個工具協助你自動填寫線上申請單的領隊與隊員的資料, 對於經常登山的你, 不用再一次又一次的填寫隊員資料.

## 先看 video
https://www.youtube.com/watch?v=yR8WyEA48cw

## 支援功能
- 玉山國家公園自動填表
- 太魯閣國家公園自動填表
- 雪霸國家公園自動填表

## 台灣國家公園入園入山線上申請服務網 (國家公園伺服器網址)
https://npm.cpami.gov.tw/apply_1.aspx

## 版權
- 歡迎任意散佈自由使用工具, 但請加註來源與作者
- 商業用途之原始碼修改: 遵循 GPL 規範

## 領隊與成員資料檔
sample_9_people.xlsx   (建議另存新檔, 每一次登山活動都存一個 xlsx 檔)

[![N|Solid](https://2.bp.blogspot.com/-CCmP-Ghkuo0/XKF5UameYrI/AAAAAAAAeBQ/aDO1JYJzIFkxmNJLtYCZAFw9i--oNOqMwCLcBGAs/s1600/Screenshot%2Bfrom%2B2019-04-01%2B10-33-49.png)](https://2.bp.blogspot.com/-CCmP-Ghkuo0/XKF5UameYrI/AAAAAAAAeBQ/aDO1JYJzIFkxmNJLtYCZAFw9i--oNOqMwCLcBGAs/s1600/Screenshot%2Bfrom%2B2019-04-01%2B10-33-49.png)

## 安裝環境
### Step 1: Install Chrome (確定安裝最新版)
https://www.google.com/chrome/
```sh
for Linux
# 直接使用下面的指令, 就會直接升級你的 chrome browser
$ sudo apt-get --only-upgrade install google-chrome-stable
```
```sh
for Windows or MacOS
# 直接到下面網址, 升級你的 chrome browser
https://www.google.com/chrome/
```

### Step 2: 安裝 git ###
```sh
for Windows
```
https://git-scm.com/download/win (下載 64-bit Git for Windows Setup).

```sh
for Linux
$ sudo apt-get install git

for MacOS
# brew install git
```

### Step 3: 安裝與設定 Python
#### ( a ) Insatll Anaconda (選擇安裝 Python 3.x 64-bit 版本)
https://www.anaconda.com/distribution/

#### ( b ) Setup Virtual Environment
```sh
for Windows
Step 1: Launch the Anaconda Prompt
    [開始] -> [Anaconda Prompt (anaconda 3)]
Step 2: setup the virtual environment
> conda create --name venv_climbing python=3.6
> conda activate venv_climbing

for Linux
$ conda create --name venv_climbing python=3.6
$ source activate venv_climbing

for MacOS
$ conda create --name venv_climbing python=3.6
$ conda activate venv_climbing
```

#### ( c ) Install the Packages
```sh
(venv_climbing) $ conda install -c conda-forge selenium pyqt xlrd pandas openpyxl
(venv_climbing) $ pip install webdriver-manager
(venv_climbing) $ pip install pytest-qt   # Optional: If you are a developper.
```

## 下載 source code
```sh
for Windows
> git clone https://github.com/jing-tw/autoclimb.git

for Linux/MacOS
$ git clone https://github.com/jing-tw/autoclimb.git
```

## 執行
```sh
for Windows
> cd autoclimb
> conda activate env_climbing
(env_climbing) $ python autoclimb.py

for Linux
$ cd autoclimb
$ source activate venv_climbing
(env_climbing) $ python autoclimb.py

for MacOS
$ cd autoclimb
$ conda activate venv_climbing
(env_climbing) $ python autoclimb.py
```

## for Developer
### Tool
- Visual Code, https://code.visualstudio.com/

### Documents
- [Design Document](https://docs.google.com/spreadsheets/d/1zBzCCGJZ_3ZbQgUl_GSnXP8J3mQQUV7dGDGVw76bHoM/edit?usp=sharing)
- [Python Tutorial](https://docs.google.com/document/d/1U1DZayMw3cEL8ZdOzN_gHTSscGgNYd_E1NKMIRDAXzY/edit?usp=sharing)
- [Excel 設定技巧](https://docs.google.com/document/d/1AG0J3jg4ULTDfpDM3BD9i5ZeutwTJr4b7w9iTzz-DEM/edit?usp=sharing)

### Auto Test
```sh
# 做了修改後, 請執行自動測試. 它會自動執行三個國家公園的檢查 (你可以去咖啡)
$ pytest -s
```

## 問題回報
https://github.com/jing-tw/autoclimb/issues

License
----
GPL


Enjoy!
by Jing.
