import csv
import numpy as np 
import matplotlib.pyplot as plt

f = open("Lot.csv","r")
csvreader = csv.reader(f)
lot = list(csvreader)

f = open("WaferLog.csv","r")
csvreader = csv.reader(f)
waferlog = list(csvreader)

#wafer = []
myfile = open('wafers.csv', 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

for items in lot:
	for jtems in waferlog:
		if jtems[2] == items[0]:
			#wafer.append(jtems)
			#print(jtems)
			wr.writerow(jtems)



#wr.writerow(wafer)


