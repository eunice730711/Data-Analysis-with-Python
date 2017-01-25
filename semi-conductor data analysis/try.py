import csv
import numpy as np 
import matplotlib.pyplot as plt

f = open("WaferLog.csv","r")
csvreader = csv.reader(f)
new1 = sorted(csvreader, key=lambda row: row[6])
new2 = sorted(new1, key=lambda row: row[1])

waferlog = list(new2)
newlist = []
for items in waferlog:
	if items[2][7:] == "01":
		newlist.append(items)


process_stage = [0] * 305

for items in newlist:
	if items[7] == "LOGIN_TOOL":
		stage = int(items[3])
		start = np.datetime64(items[6])
	elif items[7] == "LOGOUT_TOOL" and stage == items[3]:
		end = np.datetime64(items[6])
		process_stage[stage] += end-start


j1 = []
j2 = []
j3 = []
j4 = []

for items in newlist:
	if items[5]=='ToolL1':
		j1.append(items[3])
	elif items[5]=='ToolL2':
		j2.append(items[3])
	elif items[5]=='TooM3':
		j3.append(items[3])
	elif items[5]=='ToolI4':
		j4.append(items[3])



