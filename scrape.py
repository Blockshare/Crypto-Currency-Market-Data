#!/usr/bin/env python3
# Loading Developer Libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import sys


def ethereum_market_price():
	""" 
	Scrape coinmarketcap website using Beautiful Soup and return data in json format. 

	Input: url = "https://coinmarketcap.com/currencies/<currency>/
	Ouput:
	{
		'name': 'currency name',
		'symbol': 'currency symbol',
		'price': 'currency price',
		'market_cap': 'market capitalization',
		'volume': 'volume',
		'supply': 'supply'
	}

	"""

	eth_url = "https://coinmarketcap.com/currencies/ethereum/"
	data = urlopen(eth_url)
	soup = BeautifulSoup(data, 'html.parser')

	symbol = soup.findAll(attrs={"class": "bold"})
	symbol = symbol[0].string

	ether = soup.findAll(attrs={"class": "text-large"})
	price = ether[1].string

	table = soup.find('table')
	cols = table.findAll('td')

	market_cap = cols[0].find('small').string
	volume = cols[1].find('small').string
	supply = cols[2].find('small').string

	data = {
		'name': 'ethereum',
		'symbol': symbol,
		'price': price,
		'market_cap': market_cap,
		'volume': volume,
		'supply': supply
	}

	return data

def bitcoin_market_price():
	""" 
	Scrape coinmarketcap website using Beautiful Soup and return data in json format. 

	Input: url = "https://coinmarketcap.com/currencies/<currency>/
	Ouput:
	{
		'name': 'currency name',
		'symbol': 'currency symbol',
		'price': 'currency price',
		'market_cap': 'market capitalization',
		'volume': 'volume',
		'supply': 'supply'
	}

	"""

	url = "https://coinmarketcap.com/currencies/bitcoin/"
	data = urlopen(url)
	soup = BeautifulSoup(data, 'html.parser')

	symbol = soup.findAll(attrs={"class": "bold"})
	symbol = symbol[0].string

	bitcoin = soup.findAll(attrs={"class": "text-large"})
	price = bitcoin[1].string

	table = soup.find('table')
	cols = table.findAll('td')

	market_cap = cols[0].find('small').string
	volume = cols[1].find('small').string
	supply = cols[2].find('small').string
	
	data = {
		'name': 'bitcoin',
		'symbol': symbol,
		'price': price,
		'market_cap': market_cap,
		'volume': volume,
		'supply': supply
	}

	return data

def litecoin_market_price():
	""" 
	Scrape coinmarketcap website using Beautiful Soup and return data in json format. 

	Input: url = "https://coinmarketcap.com/currencies/<currency>/
	Ouput:
	{
		'name': 'currency name',
		'symbol': 'currency symbol',
		'price': 'currency price',
		'market_cap': 'market capitalization',
		'volume': 'volume',
		'supply': 'supply'
	}

	"""

	url = "https://coinmarketcap.com/currencies/litecoin/"
	data = urlopen(url)
	soup = BeautifulSoup(data, 'html.parser')

	symbol = soup.findAll(attrs={"class": "bold"})
	symbol = symbol[0].string

	litecoin = soup.findAll(attrs={"class": "text-large"})
	price = litecoin[1].string

	table = soup.find('table')
	cols = table.findAll('td')

	market_cap = cols[0].find('small').string
	volume = cols[1].find('small').string
	supply = cols[2].find('small').string

	data = {
		'name': 'litecoin',
		'symbol': symbol,
		'price': price,
		'market_cap': market_cap,
		'volume': volume,
		'supply': supply
	}

	return data

if __name__=='__main__':
	data = ethereum_market_price(), bitcoin_market_price(), litecoin_market_price()
	market_data = json.dumps(data, indent=4, sort_keys=True)
	print(market_data)
