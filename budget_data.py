import os
import csv

csvpath = os.path.join('budget_data.csv')
# open file
with open (csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')
# ignore first row
	next(csvreader, None)
# set up
	first_row = next(csvreader)
	start = first_row[1]
	max = start
	min = start
	months = 1
	month_start = 0
	total = int(start)
# for loop
	for row in csvreader:
# calculate month gap
		month_end = int(row[1])
		month_gap = month_end - month_start
# count total months
		months += 1
# count total profit
		total += int(row[1])
		end = row[1]
# find largest increase and decrease
		if month_gap > int(max):
			max_month = row[0]
			max = month_gap
		if month_gap < int(min):
			min_month = row[0]
			min = month_gap
		month_start = month_end
# calculate average change after for loop
	average = (int(end) - int(start)) / (months - 1)
# print result to terminal
	print('Financial Analysis')
	print('----------------------')
	print('Total Months: ' + str(months))
	print('Total: $' + str(total))
	print('Average Change: $' + str(round(average, 2)))
	print('Greatest Increase in Profits: ', max_month, ' ($', max, ')')
	print('Greatest Decrease in Profits: ', min_month, ' ($', min, ')')
# write result to a text file
with open('bugdet_data.txt', 'w') as text:
	text.write('Financial Analysis\n')
	text.write('----------------------\n')
	text.write('Total Months: ' + str(months) + '\n')
	text.write('Total: $' + str(total) + '\n')
	text.write('Average Change: $' + str(round(average, 2)) + '\n')
	text.write('Greatest Increase in Profits: ' + max_month + ' ($' + str(max) + ')'+ '\n')
	text.write('Greatest Decrease in Profits: ' + min_month + ' ($' + str(min) + ')')
