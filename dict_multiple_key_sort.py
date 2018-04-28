from operator import itemgetter

# usually would be a bunch of custom objects rather than dictionaries
users = [
	{'fname': 'Bucky', 'lname': 'Roberts'},
	{'fname': 'Tom', 'lname': 'Roberts'},
	{'fname': 'Bernie', 'lname': 'Zunks'},
	{'fname': 'Jenna', 'lname': 'Hayes'},
	{'fname': 'Sally', 'lname': 'Jones'},
	{'fname': 'Amanda', 'lname': 'Roberts'},
	{'fname': 'Dean', 'lname': 'Hayes'},
	{'fname': 'Bernie', 'lname': 'Sanders'},
	{'fname': 'Tom', 'lname': 'Williams'},
	{'fname': 'Tom', 'lname': 'Jones'},
]

# sort by first name
for x in sorted(users, key=itemgetter('fname')):
	print(x)
	
# sort by first name, then by last name	
print ('------')	
for x in sorted(users, key=itemgetter('fname', 'lname')):
	print(x)


# Remember, items in individual dictionaries are unsorted




# sort() vs sorted():
	
# sort() is a method of list.  As explained, it sorts the list in place and it does not return the list as a reminder of that fact.

# sorted() is a builtin function, not a method on list, because it's more general taking any iterator as its first argument (for example an open file), not just a list.  It of course does return a list.