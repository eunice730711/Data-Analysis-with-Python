import csv
import numpy as np
def check(filename):
	f = open(filename,"r")
	csvreader = csv.reader(f)
    #tool = list(csvreader)
	tool = list(sorted(csvreader, key=lambda row: row[7]))

	start = 0
	total = 0
	number = 0
	for items in tool:
		if items[8] == "TOOL_CLEAN_START":
			start = np.datetime64(items[7])
			
		if items[8] == "TOOL_CLEAN_FINISH":
			end = np.datetime64(items[7])
			total += (end - start)
			number += 1

	if number > 0:
		return total,number
	else:
		return 0, 0


arr = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
count = [ 12, 16, 12, 20, 10, 30, 30, 10, 24, 4, 20, 8, 16, 6]
idx = 0
for ch in arr:
	all_total = 0
	all_number = 0
	for i in range(count[idx]):
		name = "ToolLog_Tool_" + ch + "_" + str(i+1) + ".csv"
		#print(name)	
		total, number = check(name)
		all_total += total
		all_number += number
		

	if all_total >0 :
		print(ch)
		print(all_total/all_number)
	idx += 1

	
#if check("ToolLog_Tool_A_1.csv"):
#	print('A')
#if check("ToolLog_Tool_A_")


 

     	
	




	
    

