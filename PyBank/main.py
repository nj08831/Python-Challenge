#!/usr/bin/env python
# coding: utf-8

# In[33]:


import os
import csv

bankdata = os.path.join('budget_data.csv')

with open(bankdata, 'r') as bank_data:
    # Split the data on commas
    csvreader = csv.reader(bank_data, delimiter=',')
    header = next(csvreader)
    
    #print(header)
    
    from collections import OrderedDict
    from statistics import mean
    from datetime import datetime
    
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
    final_stats= OrderedDict(zip(month_year[1:],change_list))
    
    max_key, max_value = max(final_stats.items(), key=lambda x:x[1])
    min_key, min_value = min(final_stats.items(), key=lambda x:x[1])
    
    #Formatting the Date from MMM-YY to Month Year
    max_key_for = datetime.strptime(max_key,'%b-%y').strftime('%B %Y')
    min_key_for = datetime.strptime(min_key,'%b-%y').strftime('%B %Y')
    
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
    output = (
    f'Financial Analyses \n'
    f'----------------------------- \n'
    f'          \n'
   
    #Counts unique months in the file
    f'Total Months: {len(set(month_year))} \n'
    
    #print Total Amount over all Months
    f'Total Net Amount (Profit/Loss): {formatted[0]} \n'
                    
    #print Average Month over Month Change
    f'Average Month over Month change (Profit/Loss) is: {formatted[1]} \n'
    
    #print(f'Avg Mom change is: {mean(change_list)}')
          
    #print Max Profit and Month
    #f'{datetime.strptime(max_key,'%b-%y').strftime('%b %Y')} \n'
    
    f'Greatest Increase in Profits occurred {max_key_for} in the amount of:  {formatted[2]} \n'
    
    #print Min Profit and Month    
    f'Greatest Decrease in Profits occurred {min_key_for} in the amount of: {formatted[3]} \n'
        
    f'                \n'
    f'                \n'
    f'                \n'

    f'Source: /PyBank/main.py \n'
    f'Owner:  Dee Ann Belsky \n' 
    )
    
    
# Print to terminal
    print(output)
    

# Save the results to text file
    with open("PyBank_Results.txt", "w") as txt_file:
        txt_file.write(output)
        txt_file.close()
    


#NOTES ONLY
#reminders
 #d={'a':'apple','b':'ball'}
 #d.keys()  # displays all keys in list
 #['a','b']
 #d.values() # displays values in list
 #['apple','ball']
 #d.items() # displays pair tuple of key and value
 #[('a','apple'),('b','ball')
 #oldformat = datetime.strptime(max_key,'%b-%y')
 #newformat = oldformat.strftime('%B %Y')
    
        
   
  
    
         
        
        
   


# In[ ]:





# In[ ]:





# In[ ]:




