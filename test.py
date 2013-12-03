import csv

def lookMode():
	print 'Content-type: text/html\r\n\r'
	file = open('inventory.csv','r')
	ReadData=csv.reader(file)
	for row in ReadData:
		print row


lookMode()