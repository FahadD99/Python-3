# dependencies
import os
import csv

# join file. Thank you Dan for showing me how to do this.
file = os.path.join('Resources','budget_data.csv')

# open file. Using the delimiter to handle commas in the file.
with open(file, newline = '') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)
# Dan thank you for helping me distinguish between square brackets for a list and curly brackets for a dictionary
# Empty arrays, will populate once for loop is cycled through
    date_list = []
    dollar_list = []
    netprofit_dic = {}

    for row in csvreader:
        date_list.append(row[0])
        dollar_list.append(int(row[1]))
        
    # Dan thank you for showing me how to cycle through a for loop backwards, -1 
    for j in range(1,len(dollar_list)):
        if date_list[j] not in netprofit_dic.keys():
            netprofit_dic[date_list[i]] = dollar_list[j] - dollar_list[j-1]
    #max date, using key, get and a dictionary, thank you Dan    
    maxiumum_date = max(netprofit_dic, key = netprofit_dic.get)
    #min date, using key, get and a dictionary, thank you Dan 
    minimum_date = min(netprofit_dic, key = netprofit_dic.get)
    # Dan thank you for showing me how to use the Sum and round functions
    number_date = len(date_list)
    total_list = sum(dollar_list)
    change_list = round(sum(netprofit_dic.values())/(num_date - 1),2)

    text_file = open("Summary Table.txt","w")

    # Dan thank you for showing me how to writelines. Creating custom functions using appended lists and using computations
    text_file.writelines(f"Financial Analysis\n******************\n")
    text_file.writelines(f"Total Months: {number_date}\nTotal: ${total_list}\nAverage Change: ${change_list}\n")
    text_file.writelines(f"Largest Increase in Profits: {maximum_date} (${netprofit_dic[maximum_date]})\n")
    text_file.writelines(f"Largest Decrease in Profits: {minimum_date} (${netprofit_dic[minimum_date]})")
    text_file.close()

# print results
    print(f"Financial Analysis\n**************************")
    print(f"Total Months: {number_date}\nTotal: ${total_list}\nAverage Change: ${change_list}")
    print(f"Largest Increase in Profits: {max_date} (${netprofit_dic[max_date]})")
    print(f"Largest Decrease in Profits: {min_date} (${netprofit_dic[min_date]})")
