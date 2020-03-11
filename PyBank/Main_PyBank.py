#dependcies
import os, csv
import numpy as np

#file path
dir_path = os.path.dirname(os.path.realpath(__file__))
pybank_data_path = os.path.join(dir_path, 'budget_data.csv')

#make dictionarys & lists
trade_months = []
trade_values = []
trade_diff = []
total_value = 0

#open file
with open(pybank_data_path, 'r') as pybank_data:
    csvreader = csv.reader(pybank_data, delimiter=',')

    #loop and count
    for rows in csvreader:
        
        if 'Date' in rows[0] and 'Profit/Losses' in rows[1]:
            pass
        
        elif rows[0] not in trade_months and rows[1] not in trade_values:
            trade_months.append(rows[0])
            trade_values.append(int(rows[1]))

        else:
            pass

#CHECK
#print(trade_months)
#print(trade_values)

#totals
total_months = len(trade_months)
total_value = sum(trade_values)

#CHECK
#print(total_months)
#print(total_value)

#get average
trade_diff = np.diff(trade_values)
trade_diff_avg = np.round(sum(trade_diff) / len(trade_diff), 2)

#convert numpy to list
trade_diff = trade_diff.tolist()

#get max & min
trade_diff_max = np.max(trade_diff)
trade_diff_min = np.min(trade_diff)

#CHECK
#print(trade_diff)
#print(trade_diff_avg)
#print(trade_diff_max)
#print(trade_diff_min)

#convert numpy to list

#find index of max and min, add 1 and then use index to find which month
trade_max_index = trade_diff.index(trade_diff_max) + 1
trade_min_index = trade_diff.index(trade_diff_min) + 1

trade_max_month = trade_months[trade_max_index]
trade_min_month = trade_months[trade_min_index]
#check values
#print(trade_max_index)
#print(trade_months[trade_max_index])
#print(trade_min_index)
#print(trade_months[trade_min_index])

#create write file
pybank_analysis_path = os.path.join(dir_path, 'SPR_Pybank_Analysis.txt')
with open(pybank_analysis_path, 'w') as pybank_analysis:

#newline

    print('\n')
    print('Financial Analysis')
    print('---------------------------------')
    #totals
    print('Total Months: ' + str(total_months))
    print('Total Profit/Losses: $' + str(total_value))
    print('Average Change: $' + str(trade_diff_avg))
    print('Greatest Increase in Profits: ' + str(trade_max_month) + ' ($' + str(trade_diff_max) + ')')
    print('Greatest Decrease in Profits: ' + str(trade_min_month) + ' ($' + str(trade_diff_min) + ')')

    #write to file
    pybank_analysis.write('Financial Analysis\n')
    pybank_analysis.write('---------------------------------\n')
    pybank_analysis.write('Total Months: ' + str(total_months) +'\n')
    pybank_analysis.write('Total Profit/Losses: $' + str(total_value) + '\n')
    pybank_analysis.write('Average Change: $' + str(trade_diff_avg) + '\n')
    pybank_analysis.write('Greatest Increase in Profits: ' + str(trade_max_month) + ' ($' + str(trade_diff_max) + ')\n')
    pybank_analysis.write('Greatest Decrease in Profits: ' + str(trade_min_month) + ' ($' + str(trade_diff_min) + ')')