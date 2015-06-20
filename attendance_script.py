import csv
import random

presence = ['P','A',"P" , 'P','A']

members = ['Adisha Porwal', 'Aditi Thakur', 'Akshay Verma',
           'Dhaval Purohit', 'Fatema Saifee', 'Kajol Maheshwari',
           'Madhuri Sharma', 'Pulkit Vaishnav','Rahul Satal',
           'Rohini Chaudhary', 'Sachin Tanwar', 'Shaifali Agrawal',
           'Shiv Dangi', 'Swati Jaiswal']

months = ['January','Febuary','March','April','May','June','July','Augest' , 'September' , 'October' , 'November' , 'December']

cols = []
cols.append("Months")
cols.append("Dates")

for i in range(1,len(members)+1):
	cols.append(members[i-1])

rows = []
rows.append(cols)


for year in range(2014,2015):
	for month in months:
		new_row = []
		new_row.append(month)
		rows.append(new_row)
		for date in range(1,32):
			new_date = str(date)
			new_row = []
			new_row.append(' ')
			new_row.append(new_date)
			for member in range(1,len(cols)):
				new_row.append(random.choice(presence))
			rows.append(new_row)

#for writing in new csv
csv_file = open('2015.csv','w', newline='')
csv_writer = csv.writer(csv_file, delimiter=',')

for row in rows:
	print(row)
	csv_writer.writerow(row)
	
csv_file.close()
