#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

##################################################################
def grab_data(to_find, ticker):

	if  ticker != "EVRGRN" and ticker != "unkn":
		page = requests.get("https://finance.yahoo.com/quote/" + ticker + "?p=" + ticker)
		data = BeautifulSoup(page.content, "html.parser")
		if to_find == "get_current_price":
			current = data.find(class_ = "Fw(b) Fz(36px) Mb(-4px)").get_text()
			index = current.index('.')
			dollars = current[:index]
			cents =  current[index+1:]
			dollars = ''.join(map(str, dollars))
			cents = ''.join(map(str, cents))
			return "Current Price: " + dollars + " dollars and " + cents + " cents"
		elif to_find == "get_high" or to_find =="get_low":
			classes= data.find_all(class_ = "Ta(end) Fw(b)")
			stock_range = list(classes[4].get_text())
			stock_range = [x.encode('UTF8') for x in stock_range]
			if to_find == "get_high":
				high = ""
				for letter in stock_range:
					if letter == '-':
						high = stock_range[stock_range.index(letter)+2:]
						index = high.index('.')
						dollars = high[:index]
						cents =  high[index+1:]
						dollars = ''.join(map(str, dollars))
						cents = ''.join(map(str, cents))
						return "Todays high:  " +  dollars + " dollars and " + cents + " cents"
			elif to_find == "get_low":
				low = ""
				for letter in stock_range:
					if letter == '-':
						low = stock_range[:stock_range.index(letter)-1]
						index = low.index('.')
						dollars = low[:index]
						cents =  low[index+1:]
						dollars = ''.join(map(str, dollars))
						cents = ''.join(map(str, cents))
						return "Todays low:  $" +  dollars + " and " + cents + " cents"

	elif ticker == "EVRGRN":
		if to_find == "get_current_price":
			price = "over 9000"
			return price
		elif to_find == "get_high" or to_find =="get_low":
			return "ask Tristan"

	else:
		raise ValueError("Company does not exist in current database")
##################################################################
def get_ticker_code(ticker_name):
	return{
		'alphabet': 'GOOGL', 
		'alphabet': 'GOOG',
		'apple': 'AAPL',
		'amazon':'AMZN', 
		'tesla':'TSLA', 
		'oracle':'ORCL', 
		'irobot':'IRBT',
		'microsoft':'MSFT', 
		'facebook':'FB',
		'intel':'INTC',
		'ibm':'IBM', 
		'evergreen robotics': 'EVRGRN'
	}.get(ticker_name, "unkn")
##################################################################
def get_value(to_find):
	return{
		'get current price': 'get_current_price', 
		'current price': 'get_current_price',
		'price':'get_current_price', 
		'current': 'get_current_price',
		'high':'get_high', 
		'get high':'get_high', 
		'low':'get_low',
		'get low':'get_low', 
	}.get(to_find, "unkn")
##################################################################
def main():
	stock_name = raw_input('Input name of company: ')
	to_find = raw_input('What info do you wish to find: ')
	print grab_data(get_value(to_find.lower()), get_ticker_code(stock_name.lower()))

if __name__ == '__main__':
	main()