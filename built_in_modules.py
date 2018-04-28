# Documentation: https://docs.python.org/3/py-modindex.html


# Print list of all modules (same as in above webpage)
from stdlib_list import stdlib_list
libraries = stdlib_list("3.5")
for i in range(0, len(libraries)):
	if i > 0:
		if libraries[i][0] != libraries[i-1][0]:
			print('')
	print(libraries[i])
print('')


# See functions in specific module (example)
import math
print(dir(math), '\n')


# Specifics of module functions
print(help(math), '\n')


# Short documentation info for module
print(math.__doc__, '\n')
