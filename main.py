import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
from smtplib import SMTP

load_dotenv()
SENDERS_EMAIL = os.getenv("MY_EMAIL")
RECEIVERS_EMAIL = os.getenv("RECEIVERS_EMAIL")
NEEDED_PRICE = <amount>

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
}

source = requests.get(url="<amazon url of needed item>", headers=headers)

soup = BeautifulSoup(source.text, "lxml")
price = int((soup.find("span", class_="a-price-whole").getText()[:-1]).replace(',', ''))

if price < NEEDED_PRICE:
    with SMTP("smtp-mail.outlook.com", 587) as connection:
        connection.starttls()
        connection.login(user=SENDERS_EMAIL, password="knsp2793") #I use outlook accounts since they are easier to work with, use whatever you like and configure the smtp host accordingly
        connection.sendmail(
            from_addr=SENDERS_EMAIL,
            to_addrs=RECEIVERS_EMAIL,
            msg="Subject: The price has dropped!"
                f"\n\nThe price of the <item> has dropped below {NEEDED_PRICE} to {price} \n"
                "Buy it here: <product link>"
        )
