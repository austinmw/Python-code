ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
# list 
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print("Adding: ", next_one)
	stuff.append(next_one)
	print("There are %d items now." % len(stuff))

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
print('#'.join(stuff[3:5])) # super stellar!


# List: Ordered, allows duplicates, search takes longer than sets


# LIST vs. SET

# A list keeps order, dict and set don't: when you care about order, therefore, you must use list (if your choice of containers is limited to these three, of course;-).

# dict associates with each key a value, while list and set just contain values: very different use cases, obviously.

# set requires items to be hashable, list doesn't: if you have non-hashable items, therefore, you cannot use set and must instead use list.

# set forbids duplicates, list does not: also a crucial distinction. (A "multiset", which maps duplicates into a different count for items present more than once, can be found in collections.Counter -- you could build one as a dict, if for some weird reason you couldn't import collections, or, in pre-2.7 Python as a collections.defaultdict(int), using the items as keys and the associated value as the count).

# Checking for membership of a value in a set (or dict, for keys) is blazingly fast (taking about a constant, short time), while in a list it takes time proportional to the list's length in the average and worst cases. So, if you have hashable items, don't care either way about order or duplicates, and want speedy membership checking, set is better than list.

# When you want to store some values which you'll be iterating over, Python's list constructs are slightly faster. However, if you'll be storing (unique) values in order to check for their existence, then sets are significantly faster.

# You may want to consider Tuples as they're similar to lists but can’t be modified. They take up slightly less memory and are faster to access. They aren’t as flexible but are more efficient than lists. Their normal use is to serve as dictionary keys.


