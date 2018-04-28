import sys

if len(sys.argv) < 2:
	sys.exit('Usage: %s database-name' % sys.argv[0])
elif len(sys.argv) >= 4:
	print("WORKS\n")