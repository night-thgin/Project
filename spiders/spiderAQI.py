import csv
import time
import requests
import bs4




class AqiSpider:
    def  __init__(self,cityname,realname):
        self.cityname = cityname
        self.realname = realname
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
        }

    def send_request(self):

        url = "https://www.weather.com.cn/textFC/hb.shtml"

        response = requests.get(url,headers = self.headers,timeout=60)
        time.sleep(2)

        print(response.text)

if __name__=='__main__':

    AS = AqiSpider('beijing','北京')
    AS.send_request()