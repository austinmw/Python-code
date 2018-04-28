import matplotlib.pyplot as plt


x = [1, 2, 3]
y = [5, 7, 4]
y2 = [10, 14, 12]
plt.plot(x,y, label='First Line')
plt.plot(x, y2, label='Second Line')
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('My Graph\n Lots of infos')
plt.legend()
plt.show()


v = [2, 4, 6, 8, 10]
w = [6, 7, 8, 2, 4]
v2 = [1, 3, 5, 9, 11] 
w2 = [7, 8, 2, 4, 2]
plt.bar(v, w, label='Bars1', color='c')
plt.bar(v2, w2, label='Bars2')


plt.show()
#histogram
population_ages = [22, 55, 62, 45, 21, 2, 5, 150, 130, 120, 110, 122, 45, 45, 95, 55, 42, 42]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 130]
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8) # optional rwidth
plt.show()


plt.scatter(x, y, label='skitscat', color='k', s=50, marker="x") # most of these optional
plt.show()


#plt.stackplot()
#plt.pie()

#to open from file:
#import csv
#with open('example.txt', 'r') as csvfile:
#	plots = csv.reader(csvfile, delimiter=",")
#	for row in plots:
#		x.append(int(row[0]))
#		y.append(int(row[1]))

# or import numpy as np
#x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)

#can also,
#-get/convert data from internet
#-rotating tables
#-handle unix time
#-colors,fills
#-spines and horizontal lines
#-candlestick OHLC graphs
#-styles
#-live graphs
#-annotations and placing text
#-subplots
#-indicator data
#-cleaning chart, custom fills, pruning
#-sharex axis
#-multi y axis plotting
#-customizing legends
#-basemap
#-3d
#-
#-
#-
#-
#-