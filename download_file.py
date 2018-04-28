# Example of pulling csv data from web and saving to spreadsheet

from urllib import request 

goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=5&e=15&f=2016&g=d&a=7&b=19&c=2004&ignore=.csv'

def download_stock_data(csv_url):
	response = request.urlopen(csv_url) # tell program to connect to a webpage
	csv = response.read()
	csv_str = str(csv)
	lines = csv_str.split("\\n") # split breaks up a string
	dest_url = r'goog.csv'  # r means raw, good when working with file paths (no escapes)
	fx = open(dest_url, "w")
	for line in lines:
		fx.write(line + '\n')
	fx.close()
	
download_stock_data(goog_url)	