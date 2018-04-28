
# Printing binary and hex values
print("binary:", bin(8))
print("hex: ", hex(10))


# AND
a = 50 # 110010
b = 25 # 011001
c = a & b
print('\n', "AND: ", bin(c),' ',c, sep='')


# OR
d = a | b
print('\n',"OR: ", bin(d),' ',d, sep='')

# Shift
x = 240 # 11110000
y = x >> 2
print('\n',"Shift: ", bin(y),' ',y, sep='')