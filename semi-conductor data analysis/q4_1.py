import csv
import numpy as np
f = open("ToolLog_Tool_M_1.csv","r")
csvreader = csv.reader(f)
mtool = list(csvreader)
newlist = []

for items in mtool:
	if items[4][:6] == "LT0310":
		newlist.append(items)

for items in newlist:
	ans = []
	start = 0
	end = 0
	if items[2] == "Chamber1" and items[6] == "279" and items[8] == "LOGOUT_CHB":
		wafer_id = items[4]
		start = np.datetime64(items[7])
		for items in newlist:
			if items[4] == wafer_id and items[2] == "Chamber2" and items[6] == "279" and items[8] == "LOGIN_CHB":
				end = np.datetime64(items[7])
				print(wafer_id + ': ' + str(end-start))
				#print(end-start)
				break
	
