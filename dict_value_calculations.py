stocks = {
	'GOOG': 434,
	'AAPL': 325,
	'FB': 54,
	'AMZN': 623,
	'F': 32,
	'MSFT': 549
}

# min value
print(min(stocks.values()))

# or
min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)