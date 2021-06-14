import requests 
from bs4 import BeautifulSoup 
import time 

URL = 'https://www.flipkart.com/mi-30000-mah-power-bank-18-w-fast-charging-delivery-3-0/p/itma19cc9efdc33f?pid=PWBG2ZY9ZYYYG963&lid=LSTPWBG2ZY9ZYYYG963CB5IBR&marketplace=FLIPKART&q=mi+power+bank+30000&store=tyy%2F4mr%2Ffu6&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_4_7_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_4_7_na_na_na&fm=SEARCH&iid=309557b1-6a30-42a6-b546-feee780052ef.PWBG2ZY9ZYYYG963.SEARCH&ppt=pp&ppn=pp&ssid=a3qih6hrts0000001622911197060&qH=5745d1bcac752a45'
url_telegram = "https://api.telegram.org/bot1896367564:AAFbhNbi8Rkvwl8EVaJ-kk-VDPRgjfXqWOA/sendMessage?chat_id=@flipkarprice&text="



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
		    time.sleep(700)
		time.sleep(10)
if __name__ == "__main__":
	priceflipkar()
