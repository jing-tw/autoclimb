# Auto-climb


## 國家公園入山入園證 成員資料自動填寫工具
[![N|Solid](https://4.bp.blogspot.com/-DAIv22gkCfc/XKG1TTMJ0UI/AAAAAAAAeE4/qddEt243nTwt-7AgdTKqJzb0R897nOG4wCLcBGAs/s1600/Screenshot%2Bfrom%2B2019-04-01%2B14-50-36.png)](https://4.bp.blogspot.com/-DAIv22gkCfc/XKG1TTMJ0UI/AAAAAAAAeE4/qddEt243nTwt-7AgdTKqJzb0R897nOG4wCLcBGAs/s1600/Screenshot%2Bfrom%2B2019-04-01%2B14-50-36.png)

這個工具協助你自動填寫線上申請單的領隊與隊員的資料, 對於經常登山的你, 不用再一次又一次的填寫隊員資料.
## 支援功能
- 玉山國家公園自動填表
- 太魯閣國家公園自動填表
- 雪霸國家公園自動填表

## 台灣國家公園入園入山線上申請服務網 (自動填寫的目標系統)
https://npm.cpami.gov.tw/apply_1.aspx

## 版權
- 歡迎任意非商業或商業自由使用工具, 但請加註來源與作者
- 商業用途之原始碼修改: 遵循 GPL 規範

## 先看 video
https://www.youtube.com/watch?v=yR8WyEA48cw

## 領隊與成員資料檔
sample_9_people.xlsx   (建議另存新檔, 每一次登山活動都存一個 xlsx 檔)

[![N|Solid](https://2.bp.blogspot.com/-CCmP-Ghkuo0/XKF5UameYrI/AAAAAAAAeBQ/aDO1JYJzIFkxmNJLtYCZAFw9i--oNOqMwCLcBGAs/s1600/Screenshot%2Bfrom%2B2019-04-01%2B10-33-49.png)](https://2.bp.blogspot.com/-CCmP-Ghkuo0/XKF5UameYrI/AAAAAAAAeBQ/aDO1JYJzIFkxmNJLtYCZAFw9i--oNOqMwCLcBGAs/s1600/Screenshot%2Bfrom%2B2019-04-01%2B10-33-49.png)

## 安裝執行環境
### Install Chrome (確定安裝最新版)
https://www.google.com/chrome/
```sh
for Linux
# 直接使用下面的指令, 就會直接升級你的 chrome browser
$ sudo apt-get --only-upgrade install google-chrome-stable
```

### 安裝與設定 Python
#### ( a ) Insatll Anaconda
https://www.anaconda.com/distribution/

#### ( b ) Setup Virtual Environment
```sh
$ conda create --name venv_climbing python=3.6

for Linux
$ source activate venv_climbing

for Windows
> conda activate env_climbing
```

#### ( c ) Install Packages
```sh
(venv_climbing) $ conda install -c conda-forge selenium pyside2 xlrd pandas
(venv_climbing) $ pip install webdriver-manager
```

## 下載
```sh
$ git clone git clone git@github.com:jing-tw/autoclimb.git

or 
https://github.com/jing-tw/autoclimb/archive/master.zip

```

## 執行
```sh
Step 1: 切進執行環境
for Linux
$ source activate venv_climbing

for Windows
> conda activate env_climbing

Step 2: 
(env_climbing) $ python autoclimb.py
```

## for Developer
- [Task](https://docs.google.com/spreadsheets/d/1zBzCCGJZ_3ZbQgUl_GSnXP8J3mQQUV7dGDGVw76bHoM/edit?usp=sharing)
- [Programming skill](https://docs.google.com/document/d/1U1DZayMw3cEL8ZdOzN_gHTSscGgNYd_E1NKMIRDAXzY/edit?usp=sharing)
- [Excel 設定技巧](https://docs.google.com/document/d/1AG0J3jg4ULTDfpDM3BD9i5ZeutwTJr4b7w9iTzz-DEM/edit?usp=sharing)

## 問題回報
https://github.com/jing-tw/autoclimb/issues or mqjing@gmail.com

License
----
GPL


Enjoy!
by Jing.
