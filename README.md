# Autoclimb
## 台灣國家公園入山入園證- 成員名單自動填表工具
這個工具協助你自動填寫線上申請單的領隊與隊員的資料, 對於經常登山的你, 不用再一次又一次的填寫隊員資料.
[![N|Solid](https://4.bp.blogspot.com/-DAIv22gkCfc/XKG1TTMJ0UI/AAAAAAAAeE4/qddEt243nTwt-7AgdTKqJzb0R897nOG4wCLcBGAs/s1600/Screenshot%2Bfrom%2B2019-04-01%2B14-50-36.png)](https://4.bp.blogspot.com/-DAIv22gkCfc/XKG1TTMJ0UI/AAAAAAAAeE4/qddEt243nTwt-7AgdTKqJzb0R897nOG4wCLcBGAs/s1600/Screenshot%2Bfrom%2B2019-04-01%2B14-50-36.png)


## 領隊與成員資料檔
sample.xlsx

[![N|Solid](https://2.bp.blogspot.com/-CCmP-Ghkuo0/XKF5UameYrI/AAAAAAAAeBQ/aDO1JYJzIFkxmNJLtYCZAFw9i--oNOqMwCLcBGAs/s1600/Screenshot%2Bfrom%2B2019-04-01%2B10-33-49.png)](https://2.bp.blogspot.com/-CCmP-Ghkuo0/XKF5UameYrI/AAAAAAAAeBQ/aDO1JYJzIFkxmNJLtYCZAFw9i--oNOqMwCLcBGAs/s1600/Screenshot%2Bfrom%2B2019-04-01%2B10-33-49.png)


## 安裝 Python
### Step 1: Insatll Anaconda
https://www.anaconda.com/distribution/
### Step 2: Install the package
  ```sh
  $ conda install -c conda-forge selenium, pyside2, xlrd, pandas
  $ pip install webdriver-manager
  ```

## 命令列執行
```sh
$ python autoclimb.py -gui 0 -list sample.xlsx
```
## 視窗執行
```sh
$ python autoclimb.py
```

## task ##
[![N|Solid](https://docs.google.com/spreadsheets/d/1zBzCCGJZ_3ZbQgUl_GSnXP8J3mQQUV7dGDGVw76bHoM/edit?usp=sharing)](https://docs.google.com/spreadsheets/d/1zBzCCGJZ_3ZbQgUl_GSnXP8J3mQQUV7dGDGVw76bHoM/edit?usp=sharing)

License
----

MIT
