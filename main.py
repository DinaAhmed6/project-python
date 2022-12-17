import requests
import bs4

h = {
	"user-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

url = 'https://www.ebay.com/sch/i.html?_dcat=111418&_fsrp=1&Release%2520Year=2021%7C2019%7C2020&_from=R40&_nkw=iMac&_sacat=0&rt=nc&_pgn=1'
page = requests.get(url, headers = h)
Cont = bs4.BeautifulSoup(page.content, 'html.parser')

listOfLinksPages = Cont.find_all('a', {'class': "pagination__item"})

listPrint = []

for link in listOfLinksPages:
	page = requests.get(link.get('href'), headers = h)
	Cont = bs4.BeautifulSoup(page.content, 'html.parser')
	list = Cont.find_all('div', {'class': "s-item__wrapper clearfix"})
	listPrint += list

for i in range(len(listPrint)):
	if listPrint[i].find('div', {'class': 's-item__title'}).text == 'Shop on eBay':
		continue
	print(listPrint[i].find('div', {'class': 's-item__title'}).text)
	print(listPrint[i].find('span', {'class': 's-item__price'}).text)

	print()
	print()