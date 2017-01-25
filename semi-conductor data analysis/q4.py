import csv

f = open("WaferLog.csv","r")
csvreader = csv.reader(f)
waferlog = list(csvreader)

for items in waferlog:
	if items[1] == "LT0310" and items[3] == "279" :
		#print(items)
		print(items[5])

f = open("ToolLog_Tool_M_1.csv","r")
csvreader = csv.reader(f)
mtool = list(csvreader)

for items in mtool:
	print(items)






