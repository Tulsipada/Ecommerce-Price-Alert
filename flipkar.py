import requests 
from bs4 import BeautifulSoup 
import time 

URL = ''
url_telegram = "https://api.telegram.org/botcode/sendMessage?chat_id=@flipkarprice&text="



def priceflipkar():
	headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' }
	while(True):
		page = requests.get(URL, headers=headers)
		soup = BeautifulSoup(page.content, 'html.parser')
		title = soup.find("span", {"class": "B_NuCI"}).get_text()
		price = float(soup.find("div", {"class": "_30jeq3 _16Jk6d"}).get_text()[1:].replace(',',''))
		print("price" +" "+str(price))
		if( price <= 2299.0 ):
		    response = requests.get(url_telegram + title + str(price))
		    time.sleep(70)
		time.sleep(10)
if __name__ == "__main__":
	priceflipkar()
