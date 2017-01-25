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

print(newlist)

for items in newlist:
	s.add(items[1])
	if items[7] == "LOGOUT_TOOL":
		stage = int(items[3])
		start = np.datetime64(items[6])
	elif items[7] == "LOGIN_TOOL" and stage+1 == int(items[3]):
		end = np.datetime64(items[6])
		wait_stage[stage+1] += end-start
print(wait_stage)

j1 = []
j2 = []
j3 = []
j4 = []

for items in newlist:
	if items[5]=='ToolI1':
		j1.append(items[3])
	elif items[5]=='ToolI2':
		j2.append(items[3])
	elif items[5]=='ToolI3':
		j3.append(items[3])
	elif items[5]=='ToolI4':
		j4.append(items[3])


		
print(len(j1))
print(len(j2))
print(len(j3))
print(len(j4))

#idx = 0
#stage_list = []
time =0
time1 =0
time2 =0
time3 =0
time4 =0

for items in j1:
	time += wait_stage[int(items)]
time1=time/len(j1)

time=0
for items in j2:
	time += wait_stage[int(items)]
time2=time/len(j2)


time=0
for items in j3:
	time += wait_stage[int(items)]
time3=time/len(j3)

time=0
for items in j4:
	time += wait_stage[int(items)]
time4=time/len(j4)

print(time1)
print(time2)
print(time3)
print(time4)






