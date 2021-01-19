
import requests
from bs4 import BeautifulSoup
import os

import urllib.request

import time


#import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


# 파일의 위치


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('http://jskim20.koreacentral.cloudapp.azure.com/board_VefN51')
req.encoding = 'utf-8'

html = req.text
soup = BeautifulSoup(html, 'html.parser')
posts = soup.select('td.title')
number = soup.select('td.no')
latest = posts[0].text


numbers = soup.select('td.no')

while True:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    req = requests.get('http://jskim20.koreacentral.cloudapp.azure.com/board_VefN51')
    req.encoding = 'utf-8'

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.select('td.title')
    number = soup.select('td.no')
    latest = posts[0].text
    #print(number)
    if number == numbers:
        print("there are no new posting")
    else:
        url = "http://jskim20.koreacentral.cloudapp.azure.com/board_VefN51"
        req = urllib.request.Request(url)
        sourcecode = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(sourcecode, "html.parser")

        abc = soup.select('td.title')[0]


        #print(a)

        k = "http://jskim20.koreacentral.cloudapp.azure.com" + abc.find("a")["href"]
        print(k)

        url = k
        req = urllib.request.Request(url)
        sourcecode = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(sourcecode, "html.parser")
        abc = soup.find("div", class_="read_body").find("p")
        message = Mail(
            from_email='kim_daewoo@daum.net',
            to_emails='jjjskim062@gmail.com',
            subject='새로운글이 올라왔습니다',
            html_content=latest + str(abc))
        try:
            sg = SendGridAPIClient('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')
            #sg = sendgrid.SendGridAPIClient(apikey='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')
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)        
        #print(latest)
        url = "http://jskim20.koreacentral.cloudapp.azure.com/board_VefN51"
        req = urllib.request.Request(url)
        sourcecode = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(sourcecode, "html.parser")

        numbers = soup.select('td.no')
    time.sleep(20)
