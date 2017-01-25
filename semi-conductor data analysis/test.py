import csv
import operator
#sortedlist = sorted(reader, key=lambda row: row[3], reverse=True)
#def check(filename,number):
f = open("ToolLog_Tool_A_1.csv","r")
csvreader = csv.reader(f)
#sortlist = sorted(csvreader, key=lambda row: row[3], reverse=True)
    
tool = list(sorted(csvreader, key=lambda row: row[7]))


for items in tool:
    print(items)