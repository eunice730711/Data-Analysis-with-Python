import csv
import numpy as np

for i in range(1):
	fname = "ToolLog_Tool_H_" + str(i+1) + ".csv"
	f = open(fname,"r")
	csvreader = csv.reader(f)
	htool = list(sorted(csvreader, key=lambda row: row[7]))

s = set()
recipe = []
for items in htool:
	if items[3] != 'NA':
		recipe.append(items)
		s.add(items[3])
		#print(items)

recipe_list = []
s.discard('')
process_time = {}

for items in s:
	recipe_list.append(items)

start = 0
end = 0

for items in recipe_list:
	process_time[items] = 0
	for jtems in recipe:
		if items == jtems[3]:
			start = jtems[7]
			break
	for jtems in reversed(recipe):
		if items == jtems[3]:
			end = jtems[7]
			break;
			
	







	



	