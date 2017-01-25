import csv
f = open("WaferLog.csv","r")
csvreader = csv.reader(f)
waferlog = list(csvreader)
s = set()
for items in waferlog:
	if items[3] == "153":
		s.add(items[5])
print(s)


