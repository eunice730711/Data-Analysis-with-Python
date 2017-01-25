import numpy as np 
import csv

def check(filename):
	f = open(filename,"r")
	csvreader = csv.reader(f)
	tool = list(sorted(csvreader, key=lambda row: row[7]))
	#tool = list(csvreader)
	number = 0
	maxn = 0
	s = set()
	for items in tool:
		if items[8] == "TOOL_PM_START":
			number = len(s)
			s.clear()
			if number > maxn:
				maxn = number
		elif items[8] != "TOOL_PM_FINISH":
			s.add(items[4][:6])
	print(maxn)
	return maxn	

ans = 0
for i in range(4):
	name = "ToolLog_Tool_J_" + str(i+1) + ".csv"
	n = check(name)
	if n > ans:
		ans = n

print(ans)