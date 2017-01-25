import csv
import numpy as np
f = open("ToolLog_Tool_L_1.csv","r")
csvreader = csv.reader(f)
l1tool = list(sorted(csvreader, key=lambda row: row[7]))
newlist = []

#print(l1tool)
lotset = set()
for items in l1tool:
	lotset.add(items[4])

print(lotset)




	
