#dependcies
import os, csv

#file path
dir_path = os.path.dirname(os.path.realpath(__file__))
pypoll_data_path = os.path.join(dir_path, 'election_data.csv')

#make dictionarys & lists
votes = {}
total_votes = 0
win_votes = []

#open file
with open(pypoll_data_path, 'r') as pypoll_data:
    csvreader = csv.reader(pypoll_data, delimiter=',')
    
    #loop through and count
    for rows in csvreader:

        if 'Candidate' in rows[2]:
            pass

        elif rows[2] not in votes.keys():
            votes[rows[2]] = 1
            total_votes +=1
        else:
            votes[rows[2]] += 1
            total_votes +=1

pypoll_results_path = os.path.join(dir_path, 'SPR_election_results.txt')
with open(pypoll_results_path,'w') as pypoll_results:
#newline
    print('\n\n')
    #actual answer
    print('Election Results')
    print('---------------------------------')
    print('Total Votes: ' + str(total_votes))
    print('---------------------------------')

    pypoll_results.write('Election Results')
    pypoll_results.write('\n---------------------------------\n')
    pypoll_results.write('Total Votes: ' + str(total_votes))
    pypoll_results.write('\n---------------------------------\n')

    #loop again
    for key in votes.keys():

        #multiply and compute decimals/percent
        percent = 100 * (int(votes[key]) / (total_votes))

        #print strings and format to percent
        print(str(key) + ': ' + "{0:.3f}%".format(percent) + ', ' +\
            str(votes[key]) +' votes')

        pypoll_results.write(str(key) + ': ' + "{0:.3f}%".format(percent) + ', ' +\
            str(votes[key]) +' votes')
        
        win_votes.append(votes[key])

    print('---------------------------------')

    pypoll_results.write('\n---------------------------------\n')
    #compage max of votes to keys in dictionary
    for key, value in votes.items():

        if value == max(win_votes):

            print(key + ' won the election!')
            print('---------------------------------')

            pypoll_results.write(key + ' won the election!')
            pypoll_results.write('\n---------------------------------\n')