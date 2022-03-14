import pandas as pd
import csv

data = pd.read_excel("Camp 1 Ppant QR Codes.xlsx", sheet_name="Age group breakdown")
data.fillna("0", inplace=True)
names = []
links = []
constant = "https://docs.google.com/forms/d/e/1FAIpQLScF3lnYHSQoGWSVUt5J7TSFuy8veGo1aurq2dWDYqs9EpByZw/viewform?usp=pp_url&"

# print(data.columns.values)
# exit()

for index, row in data.iterrows():	

	unique_id = int(row['ID'])
	name_space = row['FirstName'] + " " + row['LastName']
	name = row['FirstName'] + "+" + row['LastName']
	allergies = row['Allergies']
	age = int(row['Age'])
	group_counselor = row['Group'] + '%20-%20' + row['Counselor']

	parent1 = row['Parent1Name'] + ':%20' + str(row['Parent1Phone'])
	parent2 = row['Parent2Name'] + ':%20' + str(row['Parent2Phone'])
	emergency = str(row['EmergencyName']) + ': ' + str(row['EmergencyPhone'])

	jk_bus = row['JKForBus'] 
	pickup1 = row['AuthName1'] + ':%20' + str(row['AuthPhone1'])
	pickup2 = row['AuthName2'] + ':%20' + str(row['AuthPhone2'])
	pickup3 = row['AuthName3'] + ':%20' + str(row['AuthPhone3'])

	# print(name, allergies, age, counselor, parent_name, parent_phone, jk, bus, pickup_name1, pickup_phone1, pickup_name2, pickup_phone2, pickup_name3, pickup_phone3)
	
	link = 'entry.631608745=' + str(unique_id) + '&entry.566531199=' + name + '&entry.1901477351=' + allergies + '&entry.164228159=' + str(age) + '&entry.1393671381=' + group_counselor
	link += '&entry.1696213448=' + parent1 + '&entry.856383805=' + parent2 + '&entry.292325733=' + emergency
	link += '&entry.76615527=' + jk_bus + '&entry.1192421819=' + pickup1 + '&entry.1867600648=' + pickup2 + '&entry.1306244736=' + pickup3

	# print(pickup_phone)
	names.append(name_space)
	links.append(constant + link) 
	# print(names)
	# print(links)
	# exit()

print("done processing - onto writing")

with open('ppant_data.csv', mode='w') as csv_file:
    fieldnames = ['Link', 'Name']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for x in range(len(names)):
    	if(names[x] != "0 0"):
    		writer.writerow({'Link': links[x], 'Name': names[x]})

#          entry.631608745=1&entry.566531199=2&entry.1901477351=3&entry.164228159=4&entry.1393671381=5&entry.1696213448=6&entry.856383805=7&entry.												76615527=8&entry.1192421819=9&entry.252923518=10&entry.1867600648=11&entry.824891694=12&entry.1306244736=13&entry.1258465733=14
# gglink = entry.631608745=id&entry.566531199=name&entry.1901477351=all&entry.164228159=12&entry.1393671381=counselor&entry.1696213448=par1&entry.856383805=par2&entry.292325733=emergency&entry.76615527=jk&entry.1192421819=pick1&entry.1867600648=pick2&entry.1306244736=pick3
# area = ['ID', 'JK', 'LastName', 'FirstName', 'Age', 'Parent1Name', 'Parent1Phone', 'Parent2Name', 'Parent2Phone', 'EmergencyName', 'EmergencyPhone', 'Allergies', 'JKForBus', 'AuthName1', 'AuthPhone1', 'AuthRelation1', 'AuthName2', 'AuthPhone2', 'AuthRelation2', 'AuthName3', 'AuthPhone3', 'AuthRelation3', 'SubmitDate', 'ConfNum']



