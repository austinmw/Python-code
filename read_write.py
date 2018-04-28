# Write (and create) file
fw = open('123sample.txt', 'w') #w: open, write; r:open, read
fw.write('Write stuff in text file\n')
fw.close()

# Read file
fr = open('123sample.txt', 'r')
text = fr.read()
fr.close()
print(text)

