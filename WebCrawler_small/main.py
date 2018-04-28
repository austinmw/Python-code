import requests # one of the ways to get web page info
from bs4 import BeautifulSoup # allows you to go to website and sort through data

def trade_spidder(max_pages):
	page = 1
	while page < max_pages:
		url = 