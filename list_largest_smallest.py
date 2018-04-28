# custom object sorting
import heapq # allows easy sorting

# basic example
nums = [32, 43, 1005, 4, 203, 305]
print(heapq.nlargest(3, nums))


# More complicated example
# list of dictionaries
stocks = [
	{'ticker': 'AAPL', 'price': 201},
	{'ticker': 'GOOG', 'price': 800},
	{'ticker': 'F', 'price': 54},
	{'ticker': 'MSFT', 'price': 313},
	{'ticker': 'TUNA', 'price': 68}
]

# print smallest 2 (sorted by price)
print(heapq.nsmallest(2, stocks, key=lambda stock: stock['price']))