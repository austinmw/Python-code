# The difference between import module and from module import foo is mainly subjective. Pick the one you like best and be consistent in your use of it. Here are some points to help you decide.

import module

# Pros:
# Less maintenance of your import statements. Don't need to add any additional imports to start using another item from the module
# Cons:
# Typing module.foo in your code can be tedious and redundant (tedium can be minimized by using import module as mo then typing mo.foo)
from module import foo

# Pros:
# Less typing to use foo
# More control over which items of a module can be accessed
# Cons:
# To use a new item from the module you have to update your import statement
# You lose context about foo. For example, it's less clear what ceil() does compared to math.ceil()
# Either method is acceptable, but don't use from module import *.

# For any reasonable large set of code, if you import * you will likely be cementing it into the module, unable to be removed. This is because it is difficult to determine what items used in the code are coming from 'module', making it easy to get to the point where you think you don't use the import any more but it's extremely difficult to be sure.


# --------------------------
# What's the difference between "import foo" and "from foo import *"?
#1)
import sys 
# This brings the name “sys” into your module.
# (Technically, it binds the name “sys” to the object that is the sys module.)
# It does not give you direct access to any of the names inside sys itself (such as exit for example). To access those you need to prefix them with sys, as in
sys.exit()

#2)
from sys import * 
# This does NOT bring the name “sys” into your module, instead it brings all of the names inside sys (like exit for example) into your module. Now you can access those names without a prefix, like this:
exit()

# So why not do that instead of import sys?
# The reason is that the second form will overwrite any names you have already declared — like exit say.

exit = 42
from sys import *   # hides my exit variable.

# OR more likely, the other way round 
from sys import *
exit = 42   # now hides the sys.exit function so I can't use it.

#Of course some of these are obvious but there can be a lot of names in a module, and some modules have the same name in them, for example: 
from os import *
from urllib import *

open(foo)   # which open gets called, os.open or urllib.open or open?

#Can you see how it gets confusing?

