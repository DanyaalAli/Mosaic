import pandas as pd
import csv

data = pd.read_excel("QR Code Sheet.xlsx", sheet_name="Sheet1")
data.fillna("0", inplace=True)
names = []
links = []
constant = "https://docs.google.com/forms/d/e/1FAIpQLSeRQUs-xqIRbKWruPPwtWbsO0xlBQ0i-oIBeb1Ikjy4AnOKaw/viewform?usp=pp_url"

# print(data.columns.values)
# exit()

for index, row in data.iterrows():	

	# unique_id = int(row['ID'])
	name_space = row['First Name'] + " " + row['Last Name']
	name = row['First Name'] + "+" + row['Last Name']
	allergies = row['Allergies']
	age = int(row['Age'])
	group_counselor = row['Group'] + '%20-%20' + row['Counselor']
	jk = row['Jamatkhana'] 
	gender = "Female" if row['Gender'] == "F" else "Male"

	parent1 = row['Parent1Name'] + ':%20' + str(row['Parent1Phone']) + '%20-------%20' + row['Parent1Email']
	parent2 = row['Parent2Name'] + ':%20' + str(row['Parent2Phone']) + '%20-------%20' + row['Parent2Email']
	# emergency = str(row['EmergencyName']) + ': ' + str(row['EmergencyPhone'])

	
	# pickup1 = row['AuthName1'] + ':%20' + str(row['AuthPhone1'])
	# pickup2 = row['AuthName2'] + ':%20' + str(row['AuthPhone2'])
	# pickup3 = row['AuthName3'] + ':%20' + str(row['AuthPhone3'])

	# print(name, allergies, age, counselor, parent_name, parent_phone, jk, bus, pickup_name1, pickup_phone1, pickup_name2, pickup_phone2, pickup_name3, pickup_phone3)
	
	link = '&entry.133934247=' + name + '&entry.640272849=' + allergies + '&entry.121559377=' + str(age) + '&entry.781041298=' + group_counselor
	link += '&entry.309753996=' + jk + '&entry.221070816=' + gender + '&entry.1326915395=' + parent1 + '&entry.179566444=' + parent2

	# print(pickup_phone)
	names.append(name_space)
	links.append(constant + link) 
	# print(names)
	# print(links)
	# exit()

print("done processing - onto writing")

with open('ppant_data2.csv', mode='w') as csv_file:
    fieldnames = ['Link', 'Name']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for x in range(len(names)):
    	if(names[x] != "0 0"):
    		writer.writerow({'Link': links[x], 'Name': names[x]})

# entry.133934247=ame&entry.640272849=aller&entry.121559377=age&entry.781041298=counselor&entry.309753996=jk&entry.221070816=Female&entry.1326915395=par+1&entry.179566444=par2

#          entry.631608745=1&entry.566531199=2&entry.1901477351=3&entry.164228159=4&entry.1393671381=5&entry.1696213448=6&entry.856383805=7&entry.												76615527=8&entry.1192421819=9&entry.252923518=10&entry.1867600648=11&entry.824891694=12&entry.1306244736=13&entry.1258465733=14
# gglink = entry.631608745=id&entry.566531199=name&entry.1901477351=all&entry.164228159=12&entry.1393671381=counselor&entry.1696213448=par1&entry.856383805=par2&entry.292325733=emergency&entry.76615527=jk&entry.1192421819=pick1&entry.1867600648=pick2&entry.1306244736=pick3
# area = ['First Name' 'Last Name' 'Jamatkhana' 'Gender' 'Age' 'Parent1Name' 'Parent1Email' 'Parent1Phone' 'Parent2Name' 'Parent2Email' 'Parent2Phone' 'Allergies' 'Group' 'Counselor']



