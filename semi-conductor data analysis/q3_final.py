import csv
import numpy as np 
import matplotlib.pyplot as plt

f = open("WaferLog.csv","r")
csvreader = csv.reader(f)
waferlog = list(csvreader)
stage153 = set()

for items in waferlog:
	if items[3] == '153':
		stage153.add(items)


print(len(sa))
print(len(sg))
