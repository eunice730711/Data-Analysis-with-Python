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
		
print(len(s))
idx = 0
stage_list = []

for items in wait_stage:
	items = items/500
	#print(items)
	if items>1000:
		#print(idx)
		stage_list.append(idx)
	idx +=1

ans = set()
ans_list = [0] * 5
for items in stage_list:
	for jtems in newlist:
		if jtems[3] != 'NA' and int(jtems[3]) == items:
			ans.add(jtems[5][:5])
			if jtems[5][:5] == "ToolA":
				ans_list[0] +=1
			elif jtems[5][:5] == "ToolE":
				ans_list[1] +=1
			elif jtems[5][:5] == "ToolJ":
				ans_list[2] +=1
			elif jtems[5][:5] == "ToolN":
				ans_list[3] +=1
			else:
				ans_list[4] +=1

			
#plt.plot(ans_list)
#plt.xlabel('Tool Type')
#plt.ylabel('Tool Using Number')
#plt.show()
print(ans_list)
print(ans)





#if items[7] == "PROCESS_COMPLETE":
		#first = True



		



