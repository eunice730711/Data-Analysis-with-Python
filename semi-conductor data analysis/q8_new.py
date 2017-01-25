import numpy as np 
import csv
import matplotlib.pyplot as plt

#sortedlist = sorted(reader, key=lambda row: row[3], reverse=True)
def check(filename,number):
	f = open(filename,"r")
	csvreader = csv.reader(f)
	#tool = list(csvreader)
	tool = list(sorted(csvreader, key=lambda row: row[7]))

	#number = []
	#maxn = 0
	#start = False
	s = set()
	#tool[0][7] = pre
	pre = np.datetime64(tool[0][7])
	now = 0

	for items in tool[1:]:
		if items[8] == "TOOL_PM_FINISH":
			number.append(len(s))
			s.clear()
		elif items[8] != "TOOL_PM_START":
			now = np.datetime64(items[7])
			if now - pre < 10:
				s.add(items[4][:6])
			pre = now


		#print(s)


arr = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
count = [ 12, 16, 12, 20, 10, 30, 30, 10, 24, 4, 20, 8, 16, 6]
#count = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#count = [ 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#arr = ['A']
#count = [ 12]
idx = 0
for ch in arr:
	print(ch)
	num = []
	for i in range(count[idx]):
		name = "ToolLog_Tool_" + ch + "_" + str(i+1) + ".csv"
		check(name,num)
		
	print(num)
	fig = plt.figure()
	fig.suptitle('Figure_' + ch , fontsize=14, fontweight='bold')
	plt.plot(num)
	plt.xlabel('index')
	plt.ylabel('lot number')
	plt.show()
	idx +=1





