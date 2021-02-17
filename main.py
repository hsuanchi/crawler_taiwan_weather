import urllib.request
import zipfile
import pandas as pd
from bs4 import BeautifulSoup
import datetime
import os


today = str(datetime.date.today())

url = "http://opendata.cwb.gov.tw/opendataapi?dataid=F-D0047-093&authorizationkey=CWB-3FB0188A-5506-41BE-B42A-3785B42C3823"
urllib.request.urlretrieve(url, "F-D0047-093.zip")
f = zipfile.ZipFile("F-D0047-093.zip")

file = [
    "63_Weekday_CH.xml",
    "64_Weekday_CH.xml",
    "65_Weekday_CH.xml",
    "66_Weekday_CH.xml",
    "67_Weekday_CH.xml",
    "68_Weekday_CH.xml",
    "09007_Weekday_CH.xml",
    "09020_Weekday_CH.xml",
    "10002_Weekday_CH.xml",
    "10004_Weekday_CH.xml",
    "10005_Weekday_CH.xml",
    "10007_Weekday_CH.xml",
    "10008_Weekday_CH.xml",
    "10009_Weekday_CH.xml",
    "10010_Weekday_CH.xml",
    "10013_Weekday_CH.xml",
    "10014_Weekday_CH.xml",
    "10015_Weekday_CH.xml",
    "10016_Weekday_CH.xml",
    "10017_Weekday_CH.xml",
    "10018_Weekday_CH.xml",
    "10020_Weekday_CH.xml",
]

data_list = []

for filename in file:
    try:
        print(filename)
        data = f.read(filename).decode("utf8")
        soup = BeautifulSoup(data, "xml")

        locationsName = soup.locationsName.text
        locations = soup.find_all("location")

        for location in locations:
            
            # 地理資訊
            locationName = location.find("locationName").text
            geocode = location.find("geocode").text
            lat = location.find("lat").text
            lon = location.find("lon").text

            weathers = location.find_all("weatherElement")
            for i in range(0,14):
                T = weathers[0]
                Td = weathers[1]
                MaxT = weathers[3]
                MinT = weathers[4]
                MaxAT = weathers[5]
                MinAT = weathers[6]
                Wx = weathers[12]

                weather_dict = {
                    "locationsName":locationsName,
                    "locationName": locationName,
                    "geocode": geocode,
                    "lat": lat,
                    "lon": lon,
                    "平均溫度": T.find_all("time")[i].find("value").text,
                    "平均露點溫度": Td.find_all("time")[i].find("value").text,
                    "最高溫度": MaxT.find_all("time")[i].find("value").text,
                    "最低溫度": MinT.find_all("time")[i].find("value").text,
                    "最高體感溫度": MaxAT.find_all("time")[i].find("value").text,
                    "最低體感溫度": MinAT.find_all("time")[i].find("value").text,
                    "天氣現象": Wx.find_all("time")[i].find("value").text,
                    "startTime": T.find("startTime").text,
                    "endTime": T.find("endTime").text,
                    "craw_date": today,
                }

                data_list.append(weather_dict)
    except Exception as e:
        print("break", e)
        break
f.close()

save_name = "taiwan_cwb" + today + ".csv"
df = pd.DataFrame(data_list)
df.to_csv(save_name, index=False, encoding="utf_8_sig")
