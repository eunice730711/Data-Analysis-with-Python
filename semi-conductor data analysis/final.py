import csv
import numpy as np
f = open("ToolLog_Tool_H_1.csv","r")
csvreader = csv.reader(f)
tool = list(sorted(csvreader, key=lambda row: row[7]))
newlist = []

#print(l1tool)

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


lotset = set()
for items in tool:
	lotset.add(items[4])

#print(lotset)
lotlist = []
ans = []
total = 0
end =0
start =0

for items in lotset:
	lotlist.append(items)
print(len(lotlist))

for items in lotlist[:200]:
	login = False
	logout = False
	time = 0
	for jtems in tool:
		if jtems[4] == items and jtems[2] == "Chamber2" and jtems[8] == 'LOGIN_CHB':
			start = np.datetime64(jtems[7])
			login = True
		if jtems[4] == items and jtems[2] == "Chamber2" and jtems[8] == 'LOGOUT_CHB':
			end = np.datetime64(jtems[7])
			time = end - start
			logout = True
		if login == True and logout == True:
			total += end - start
			ans.append(time)
			break
print(total.item().total_seconds())
print(len(ans))
print(total.item().total_seconds()/len(ans))






	
