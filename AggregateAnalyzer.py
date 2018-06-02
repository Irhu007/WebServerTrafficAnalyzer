import sys

for line in sys.stdin:
	fields = line.split(",")
	if fields[1][13:15].isdigit():
		print "LongValueSum:" + fields[1][13:15] +"\t"+ "1"
