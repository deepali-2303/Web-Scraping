import requests
from bs4 import BeautifulSoup
from lxml import etree
import sqlite3

most_active = "https://www.google.com/finance/markets/most-active?hl=en"
most_active_response = requests.get(most_active)
soup_most_active = BeautifulSoup(most_active_response.content,"html.parser")
dom_most_active = etree.HTML(str(soup_most_active))

names = (dom_most_active.xpath('//*[@class="ZvmM7"]/text()'))
current_prices = (dom_most_active.xpath('//div[@class="xVyTdb ytSBif"]/span[@class="JLPHhb"]/div[@class="Bu4oXd" and @jsname="ip75Cb"]//*[@class="YMlKec"]/text()'))
print(len(names))
print(len(current_prices))

connection = sqlite3.connect("Google_Finance.db")
c = connection.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS MostActive
             (name TEXT, 
             price TEXT)''')

for name,price in zip(names,current_prices):
  c.execute("INSERT INTO MostActive (name, price) VALUES (?,?)",(name,price))




connection.commit()
connection.close()