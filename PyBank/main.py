#!/usr/bin/env python
# coding: utf-8


import os
import csv

bankdata = os.path.join('budget_data.csv')


with open(bankdata, 'r') as bank_data:
    # Split the data on commas
    csvreader = csv.reader(bank_data, delimiter=',')
    header = next(csvreader)
    
    #print(header)
    
    #define lists to store data for analyses
    month_year = []
    profit_loss = []
    total_profit_loss = 0
    
    #create the lists, and builds counter for the sum
    for row in csvreader:
        month_year.append(row[0])
        profit_loss.append(int(row[1]))
        total_profit_loss = total_profit_loss + int(row[1])
    
    #creates dictionary of key,value pairs to iterate thru
    #collections enables the data to stay ordered
    
    from collections import OrderedDict
    from statistics import mean
    
    #create a list to find the $ change between month i and month i-1
    change = 0
    change_list=[]
    
    # calculate the change between month i and month i-1
    dictionary = (zip(profit_loss,profit_loss[1:]))
    for x,y in dictionary:
        change_list.append(y-x)
        
    #calculate the average change
    avg_changes = sum(change_list)/len(change_list)
    
    # find the max and min amounts and their associated month-year    
    final_stats= OrderedDict(zip(month_year,change_list))
    
    max_key, max_value = max(final_stats.items(), key=lambda x:x[1])
    min_key, min_value = min(final_stats.items(), key=lambda x:x[1])
    
    
    #format the values - use a list to iterate thru the values
    format_values = [total_profit_loss,avg_changes,max_value,min_value]
    formatted = []
       
    
    for value in format_values:
        if value >= 0:
            value = '${:,.0f}'.format(value) 
            formatted.append(value)
            #print(value)
        else:
            value = '-${:,.0f}'.format(-value)
            formatted.append(value)
            #print(value)

    #OUTPUT RESULTS
    #print (formatted[0])
    
    print(f'Financial Analyses')
    print(f'-----------------------------')
    print(f'            ')
   
    #Counts unique months in the file
    print(f'Total Months: {len(set(month_year))}')
    
    #print Total Amount over all Months
    print(f'Total Net Amount (Profit/Loss): {formatted[0]}')
                    
    #print Average Month over Month Change
    print(f'Average Month over Month change (Profit/Loss) is: {formatted[1]}')
    
    #print(f'Avg Mom change is: {mean(change_list)}')
          
    #print Max Profit and Month
    print(f'Greatest Increase in Profits occurred {max_key} in the amount of:  {formatted[2]}' )
    
    #print Min Profit and Month    
    print(f'Greatest Decrease in Profits occurred {min_key} in the amount of: {formatted[3]}' )
    
#Create an output text file
# write data in a file. 
output_file = open("PyBank_Results.txt","w") 

output_file.write(f'                \n')
output_file.write(f'Financial Analyses \n')
output_file.write(f'-----------------------------')
output_file.write(f'            \n')
output_file.write(f'Total Months: {len(set(month_year))} \n')
output_file.write(f'Total Net Amount (Profit/Loss): {formatted[0]} \n')
output_file.write(f'Average Month over Month change (Profit/Loss) is: {formatted[1]} \n')
output_file.write(f'Greatest Increase in Profits occurred {max_key} in the amount of:  {formatted[2]} \n'  )
output_file.write(f'Greatest Decrease in Profits occurred {min_key} in the amount of: {formatted[3]} \n' )

output_file.write(f'                \n')
output_file.write(f'                \n')
output_file.write(f'                \n')

output_file.write(f'source:     PyBank.py \n')
output_file.write(f'programmer: Dee Ann Belsky \n' )
output_file.close() #to change file access modes 


#NOTES ONLY
#reminders
 #d={'a':'apple','b':'ball'}
 #d.keys()  # displays all keys in list
 #['a','b']
 #d.values() # displays values in list
 #['apple','ball']
 #d.items() # displays pair tuple of key and value
 #[('a','apple'),('b','ball')
    
        