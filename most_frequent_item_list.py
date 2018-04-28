from collections import Counter # Counter: pass in list, run statistics on it

text = "The first thing to do was to find something to crack: I'd recently downloaded a 			small desktop utility (I'm not going to say which one... but I'll refer to it as 			'Spannr' for the purpose of the article) that pops up a 'BUY ME NOW!' screen when it 		loads, and also at random intervals during use. 'By applying some ol' Fravia 				lessons', I reasoned 'I should be able to get rid of those pesky messages without 			doing the bit where I give my credit card details.'"

# split paragraph into words
words = text.split()

# use Counter class
counter = Counter(words)

# top three
top_three = counter.most_common(3)
print(top_three)
