# Dictionary
stocks = {
	'GOOG': 520.54,
	'FB': 76.45,
	'YHOO': 39.28,
	'AMZN': 306.21,
	'AAPL': 99.76
}

# No built-in way to sort a dictionary, but can sort a zipped list
# Use zip function
# Sorts by first argument
print(min(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))
