# 爬取臺灣天氣預報

## 1. 目的
取得「全臺灣各鄉鎮市區天氣預報資料」[爬取來源：政府資料開放平臺](https://data.gov.tw/dataset/9309)

## 2. Demo
<img src="https://github.com/hsuanchi/crawler_taiwan_weather/blob/main/image/demo_csv.jpg">

## 3. 使用套件
* python = "3.7.1"
* pandas = "^1.2.2"
* lxml = "^4.6.2"
* bs4 = "^0.0.1"

## 4. Run crawler
Create your virtual environment
```
$ python3 -m venv venv
```
And enable virtual environment
```
$ . venv/bin/activate
```
Install requirements
```
$ pip install -r requirements.txt 
```
Run crawler
```
$ python3 main.py
```
