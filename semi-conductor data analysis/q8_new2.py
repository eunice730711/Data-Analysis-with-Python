import numpy as np 
import csv
import matplotlib.pyplot as plt

#sortedlist = sorted(reader, key=lambda row: row[3], reverse=True)
def check(filename,number):
	f = open(filename,"r")
	csvreader = csv.reader(f)
	#tool = list(csvreader)
	tool = list(sorted(csvreader, key=lambda row: row[7]))


	for items in tool[:len(tool)-1]:
		if items[7] != '' and items[7] != 'NA' and items[7].find('-') == -1:
			tmp = items[7].split(' ')
			tmp[0] = tmp[0].split('/')
			if int(tmp[0][1]) < 10 and int(tmp[0][2]) < 10:
				items[7] = tmp[0][0] + '-0' + tmp[0][1] + '-0' + tmp[0][2] + ' ' + tmp[1]
			elif int(tmp[0][1]) < 10:
				items[7] = tmp[0][0] + '-0' + tmp[0][1] + '-' + tmp[0][2] + ' ' + tmp[1]
			elif int(tmp[0][2]) < 10:
				items[7] = tmp[0][0] + '-' + tmp[0][1] + '-0' + tmp[0][2] + ' ' + tmp[1]
			else:
				items[7] = tmp[0][0] + '-' + tmp[0][1] + '-' + tmp[0][2] + ' ' + tmp[1]


	tool = sorted(tool, key = lambda x : x[7]) 

	#for items in tool:
	#	print(items[7])

	#number = []
	#maxn = 0
	#start = False
	s = set()
	times = []
	pre = 0
	now = 0
	#print("\n\n\n\n\nAAAAAAAAAAAA\n\n\n\n\n")

	for items in tool:
		if items[8] == "TOOL_PM_START":
			#print(times)
			if len(s)>50:
				number.append(len(s))
			#del times[:len(times)]
			#print("\n\n\n\n\nPPPPPPPPPPPP\n\n\n\n\n")
			#start = True
			s.clear()
		elif items[8] == "LOGIN_TOOL" or items[8] == "LOGOUT_TOOL" or items[8] == "LOGIN_CHB" or items[8] == "LOGOUT_CHB":
			
			if len(s) == 0:
				pre = np.datetime64(items[7])
			else:
				now = np.datetime64(items[7])
				#print(pre)
				#print(now)

				duration = now - pre
				pre = now
					
				if duration > 10000:
					#print(duration)
					s.clear()
					del times[:len(times)]
					#start = False
					#print("\n\n\n\n\nAAAAAAAAAAAAAA\n\n\n\n\n")
			s.add(items[4][:6])
			#times.append(items[7])

		#print(s)


arr = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
count = [ 12, 16, 12, 20, 10, 30, 30, 10, 24, 4, 20, 8, 16, 6]

#arr = ['A','B','C','D','E','F','G','H','I','K']
#count = [ 12, 16, 12, 20, 10, 30, 30, 10, 24, 20]
#count = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#count = [ 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#arr = ['C']
#count = [ 1]
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





