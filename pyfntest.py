import math


def sumtest(x, y):
    sum = x + y
    output = 'The sum is {}.' .format(sum)
    print output

"""
With the -c (command) argument (assuming your file is named foo.py):

$ python -c 'import foo; print foo.hello()'
Alternatively, if you don't care about namespace pollution:

$ python -c 'from foo import *; print hello()'
And the middle ground:

$ python -c 'from foo import hello; print hello()'

"""


#i=-2.0
#q=3.0

#print "Cartesian: (%.1f,%.1f)" %(i,q)



#print "Polar: r = %.1f" %math.sqrt(math.pow(i,2) + math.pow(q,2)) + ", Theta = %.1f" %math.degrees(math.atan(q/i)) + " degrees"


