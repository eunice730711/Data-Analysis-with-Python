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


wait_stage = [0] * 305
s = set()
stage = -1
start = 0

for items in newlist:
	s.add(items[1])
	if items[7] == "LOGOUT_TOOL":
		stage = int(items[3])
		start = np.datetime64(items[6])
	elif items[7] == "LOGIN_TOOL" and stage+1 == int(items[3]):
		end = np.datetime64(items[6])
		wait_stage[stage+1] += end-start
		
print(wait_stage)
idx = 0
stage_list = []

for items in wait_stage:
	items = items/500
	#print(items)
	if items>1000:
		#print(idx)
		stage_list.append(idx)
	idx +=1
