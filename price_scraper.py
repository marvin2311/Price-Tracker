import requests
import smtplib
import time
from bs4 import BeautifulSoup

#example of the new adidas Supercourt sneakers
URL = 'https://www.adidas.de/supercourt-schuh/EE6031.html' #change to your product page

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'} #change to your user agent

def check_price():
    page = requests.get(URL,headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find('h1', {'class': 'gl-heading--m gl-vspacing-s'}).get_text() #check the id or class of the title-container on your product page

    price = soup.find('span', {'class':'gl-price__value'}).get_text() #check the id or class of the price-container on your product page
    price_int = int(price[2:4]) #range depends on displayed price

    if price_int <= 70:
        send_mail()

    print(title)
    print(str(price_int)+" EUR")

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #you have to allow less secure apps: https://myaccount.google.com/lesssecureapps
    server.login('username', "password") #use your username and password

    subject = "Price felt down!"
    body = "Quickly check the link: "+URL
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('from', 'to', msg) #put in your address and the one which should receive the mail
    print("E-Mail has been send")

    server.quit()

while(True):
    check_price()
    time.sleep(3600) #checks every hour
