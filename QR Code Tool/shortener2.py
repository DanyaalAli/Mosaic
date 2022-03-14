import bitly_api
import csv
import time

BITLY_ACCESS_TOKEN = '3feb0fcd690fa99ba826cf9fbac62a54190c7343'
long_links = []
shorty_links = []
names = []

with open('../ppant_data2.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count != 0:
			long_links.append(row[0])
			names.append(row[1])
		line_count += 1

# print(len(long_links), len(names))

# for x in range(5):
# 	print(names[x], long_links[x])

# quit()

con = bitly_api.Connection(access_token=BITLY_ACCESS_TOKEN)
print("connected")

count = 0
for link in long_links:
	print(count)
	if count % 50 == 25 or count == 115:
		time.sleep(30)
	sh = con.shorten(link)
	shorty_links.append(sh['url'])
	count += 1

print("done shortening - onto writing")

with open('../ppant_data2.csv', mode='w') as csv_file:
	fieldnames = ['Long_Link', 'Name', 'Shorty_Link']
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

	writer.writeheader()
	for x in range(len(names)):
		writer.writerow({'Long_Link': long_links[x], 'Name': names[x], 'Shorty_Link': shorty_links[x]})


# with open('../ppant_data2.csv') as csv_file:
# 	csv_reader = csv.reader(csv_file, delimiter=',')
# 	line_count = 0
# 	for row in csv_reader:
# 		if line_count != 0:
# 			print(row[2][0])
# 			quit()
# 		line_count += 1


