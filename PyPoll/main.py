#!/usr/bin/env python
# coding: utf-8

import os
import csv

input_file = os.path.join('election_data.txt')

with open(input_file, 'r') as election_data:
    csvreader = csv.reader(election_data, delimiter = ',')
    header = next(csvreader)
    #print(header)

    #create lists and zip them together into a dictionary
    voter_id =   []
    county   =   []
    candidates = []
    
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
        
    #validate that voter_ids are unique in the data set
    unique_voter_ids = list(set(voter_id))
    
    from collections import Counter
    
    #Frequency Distribution of the Candidates
    cnt = Counter()
    for candidate in candidates:
        cnt[candidate] = cnt[candidate]+1
    
    #find winner
    #print(cnt)
    winner_name = max(cnt, key=cnt.get)

    
    output = (
        f' \n '
        f'Election Results \n '
        f'----------------------------------------------- \n '
        f' \n '
        f'Total Votes: \t {"{:,}".format(len(unique_voter_ids))} \n '
    #print(len(voter_id))
        f'----------------------------------------------- \n '
        f' \n '
        "{0:<10} {1:>15} {2:>20} \n".format("Candidates","Total Votes","% of Total Votes" )
     )
    #print(f'{key} \t \t {value}')
    
    output2 = (
        f' \n '
        f'-----------------------------------------------\n '
        f'  \n '
        f'Winner: \t {winner_name}\n '
        f'   \n '
        f'-----------------------------------------------\n '
        f'   \n'
        f'   \n'
        f'Source file: /PyPoll/main.py \n'
        f'Owner:       Dee Ann Belsky'
     )
        
# Print all of the results (to terminal)
    print(output)
    for key,value in cnt.items():
        perc_tot = value / (len(unique_voter_ids))
        print(" {0:<10} {1:>15}".format(key,"{:,}".format(value)) + f" {perc_tot:>20.1%}".format(perc_tot))
    print(output2)

# Save the results to text file
    with open("PyPoll_Results.txt", "w") as txt_file:
        txt_file.write(output)
        for key,value in cnt.items():
            perc_tot = value / (len(unique_voter_ids))
            txt_file.write(" {0:<10} {1:>15}".format(key,"{:,}".format(value)) + f" {perc_tot:>20.1%} \n".format(perc_tot))
        txt_file.write(output2)
        txt_file.close()
    
    
    #NOTES/MISC only
    #print(cnt)
    #"{:,}".format(value)
    #print(len(county))
    #print(len(candidates))
    #check each list inputed
    #print(voter_id[4:7],county[4:7],candidates[4:7])
   