import csv
f = open("Berkeley.csv","r")
csvreader = csv.reader(f)
berkeley = list(csvreader)
men = 0
women =0
ad_men =0
ad_women =0
for items in berkeley[1:]:
	if items[1] == "Male":
		men += int(items[3])
		if items[0] == 'Admitted':
			ad_men += float(items[3])
	else:
		women += int(items[3])
		if items[0] == 'Admitted':
			ad_women += float(items[3])
men_rate = ad_men / men
women_rate = ad_women / women
print(men_rate)
print(women_rate)



