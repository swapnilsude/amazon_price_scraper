from bs4.dammit import html_meta
import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.com/Samsung-Wireless-Cancelling-Charging-Included/dp/B089B658NP/"
head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}

def check_price():

    cookies = dict(cookies_are='working')

    page = requests.get(URL,headers=head,cookies=cookies)
    soup = BeautifulSoup(page.content,features="html.parser")

    price = soup.find(id="priceblock_ourprice").get_text()
    myprice = float(price[1:])

    if myprice < 150:
        print("yo ho ho ho")
        # send_mail()
    else:
        print("not yet")

def send_mail():
    
    server = smtplib.SMTP('smpt.gmail.com',587)
    server.ehlo() 
    server.starttls()
    server.ehlo()

    server.login('<email-id>','<passwd>')
    subject = 'Price below $150'
    body = 'check link' + URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'from',
        'to',
        msg
    )

    server.quit()

while True:
    check_price()
    time.sleep(3600)