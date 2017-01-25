import csv
import numpy as np 
import matplotlib.pyplot as plt

f = open("WaferLog.csv","r")
csvreader = csv.reader(f)
waferlog = list(csvreader)
sj = set()
sg = set()

for items in waferlog:
	if items[5] == 'ToolJ1':
		sj.add(items[3])
	

print(len(sj))

