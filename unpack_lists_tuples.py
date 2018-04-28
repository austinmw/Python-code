# Unpacking a list into variables
date, name, price = ['December 23, 2015', 'Bread Gloves', 8.51]

print(name)


# Unpacking with mismatched size variables & arguments
def drop_first_last(grades):
	first, *middle, last= grades
	avg = sum(middle) / len(middle)
	print(avg)
	
drop_first_last([65, 76, 98, 54, 21])