#pybank

import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))

pybank_data = os.path.join(dir_path, '..', '03-Python_homework_assignment_PyBank_Resources_budget_data.csv')

pybank_data_answer = os.path.join(dir_path,'..', "03-Python_hw_pybank_answer_SPR.csv")

#def print_bank_data(pybank_data):
#    total_months = str(pybank_data[0])
#    total_value = int(pybank_data[1])

#    print(total_months)
#    print(total_value)
    

with open(pybank_data, 'r') as csvfile:

    # Create CSV reader object
    csvreader = csv.reader(pybank_data, delimiter=',')

    print(csvreader)


    # Read/Skip the header
    #header = next(csvreader)
