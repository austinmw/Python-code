# https://www.quora.com/What-are-some-interesting-things-to-do-with-Python-I-want-to-make-something-related-to-big-data-or-machine-learning

# Function decorators are particularly neat in Python. They allow you to enhance the functionality of existing functions.
# Let me demonstrate with a simple example of calculating the factorial of a number recursively:
# One way to speed up this function is to use Memoization. Using decorators, this can be easily achieved:


def memoize(f):
	cache = {}
 
	def inner(n):
		if n not in cache:
			cache[n] = f(n)
		return cache[n]
 
	return inner
 
@memoize
def factorial(n):
	if n == 0:
		return 1
	return n * factorial(n - 1)
	
print(factorial(10))

# One call to factorial results in the cache building up for all numbers < n. 
# Next time you invoke factorial for a number < n, the result is not computed but fetched from the cache. 
# This makes it easy to separate out the cache maintaining logic from the function being decorated.
# @memoize is syntactic sugar for:
# factorial = memoize(factorial)

# To make the memoize function more general (the way I use it often):

def memoize(f):
	cache = {}
 
	def inner(*args, **kwargs):
		if args not in cache:
			cache[args] = f(*args, **kwargs)
		return cache[args]
 
	inner.__name__ = 'memoized_' + f.__name__
	return inner

