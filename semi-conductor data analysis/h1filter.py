import csv
import numpy as np 
import matplotlib.pyplot as plt

f = open("ToolLog_Tool_H_1.csv","r")
csvreader = csv.reader(f)
lot = list(sorted(csvreader, key=lambda row: row[7]))


#wafer = []
myfile = open('htool_sort.csv', 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)


for items in lot:
	wr.writerow(items)


#wr.writerow(wafer)


