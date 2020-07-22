# dependencies 
import os
import csv

#joining file
file = os.path.join('Resources','election_data.csv')

# open file, using the delimiter option to handles the commas - thank you for showing us this Dan
with open(file, newline = '') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)

# empty arrays arrays. Will append data into empty arrays through a for loop
# Dan thank you for showing me this skill set for my dataset as well- very valuable skill.
    voter_lst = []
    short_lst = []
    candidate_lst = []
    empty_dic = {}

    for row in csvreader:
     
        voter_lst.append(row[0])
        candidate_lst.append(row[2])
        if row[2] not in short_lst:
            short_lst.append(row[2])
    
  # get complete vote count based on the voter list appended arrray
  # Total_vote_count is that length of the voter_lst - thank you for showing us this Dan
  # Success is the winner from the voting
    total_vote_count = len(voter_lst)

    for j in short_lst:
        empty_dic[j] = int(candidate_lst.count(j))
    
   # Dan thank you for showing me how to use get
    success = max(empty_dic, key = empty_dic.get)

# writing to the summary table, a text file
# Thank you Dan for showing me how to use the ****** to seperate the data on visual perspective
    file_txt = open("Summary Table.txt","w")
   
    file_txt.writelines(f"Election Results\n****************************\n")
    file_txt.writelines(f"Total Votes:{total_vote_count}\n*************************\n")
    for j in short_lst:
        # Thank you for showing me how to round Dan.
        file_txt.writelines(f"{j}: {round(empty_dic[j]/total_vote_count*100,2)}% ({empty_dic[j]})\n")
    file_txt.writelines(f"***********************\nWinner: {success}\n**********************")
    file_txt.close()


# print results
print(f"Election Results\n****************************")
print(f"Total Votes:{total_vote_count}\n**********************")
for j in short_lst:
    # print and round to 2 decimal places
    print(f"{j}: {round(empty_dic[j]/total_vote_count*100,2)}% ({empty_dic[j]})")
print(f"*********************\nWinner: {winner}\n************************")
