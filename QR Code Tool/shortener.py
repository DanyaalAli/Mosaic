import bitly_api
import csv

BITLY_ACCESS_TOKEN = 'bf3959b97799d614e13a15c408d819f0edd4e2d4'
long_links = []
shorty_links = []
names = []

with open('../ppant_data.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count != 0:
			long_links.append(row[0])
			names.append(row[1])
		line_count += 1

print(len(long_links), len(names))

for x in range(5):
	print(names[x], long_links[x])

quit()

con = bitly_api.Connection(access_token=BITLY_ACCESS_TOKEN)
print("connected")

for link in long_links:
	shorty_links.append(con.shorten(link))

print("done shortening - onto writing")

with open('../ppant_data.csv', mode='w') as csv_file:
    	fieldnames = ['Long_Link', 'Name', 'Shorty_Link']
    	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    	writer.writeheader()
    	for x in range(len(names)):
		writer.writerow({'Long_Link': long_links[x], 'Name': names[x], 'Shorty_Link': shorty_links[x]})


