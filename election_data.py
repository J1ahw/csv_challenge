import os
import csv

csvpath = os.path.join('election_data.csv')
# open file
with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')
# forget first row	
	next(csvreader, None)
	first_row = next(csvreader)
# set up
	Charles_Casper_Stockham = 1
	Diana_DeGette = 0
	Raymon_Anthony_Doane = 0
	total = 1
	for row in csvreader:
# calculate total votes
		total += 1
# use if condition to calculating persons' votes
		if row[2] == 'Charles Casper Stockham':
			Charles_Casper_Stockham += 1
		elif row[2] == 'Diana DeGette':
			Diana_DeGette += 1
		else:
			Raymon_Anthony_Doane += 1
# calculate percentage
	c = round(Charles_Casper_Stockham / total, 5)
	d = round(Diana_DeGette / total, 5)
	r = round(Raymon_Anthony_Doane / total ,5)
# compare to find winner	
	max = c
	winner = 'Charles Casper Stockham'
	if max < d:
		max = d
		winner = 'Diana DeGette'
	elif max < r:
		max = r
		winner = 'Raymon Anthony Doane'
# make percentage format
	c = '%.3f%%' %(c *100)
	d = '%.3f%%' %(d *100)
	r = '%.3f%%' %(r *100)
# print result to terminal
	print('Election Results\n--------------')
	print('Total Votes:' + str(total) + '\n-------------\nCharles Casper Stockham: '+ str(c) + '(' + str(Charles_Casper_Stockham) + ')')
	print('Diana DeGette: '+ str(d) + '(' + str(Diana_DeGette) + ')')
	print('Raymon Anthony Doane: '+ str(r) + '(' + str(Raymon_Anthony_Doane) + ')')
	print('-----------------\nWinner:'+ winner + '\n--------------------')
# wirte result to a text file
with open('election_data.txt', 'w') as text:
	text.write('Election Results\n--------------\n')
	text.write('Total Votes:' + str(total) + '\n-------------\nCharles Casper Stockham: '+ str(c) + '(' + str(Charles_Casper_Stockham) + ')')
	text.write('\nDiana DeGette: '+ str(d) + '(' + str(Diana_DeGette) + ')')
	text.write('\nRaymon Anthony Doane: '+ str(r) + '(' + str(Raymon_Anthony_Doane) + ')')
	text.write('\n-----------------\nWinner:'+ winner + '\n--------------------')
