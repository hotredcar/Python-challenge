import os
import csv

#create lists 
votes = []
candidates = []
unique_candidates = []

#read and store data____________________________________________________________________

#specify file to read 
election_csv = os.path.join(".", "Resources", "election_data.csv")

# read file
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#read header/skip 
    csv_header = next(csv_file)

    #loop through each row 
    for row in csv_reader:

        #store candidates/votes 
        candidates.append(row[2])

#perform analysis_______________________________________________________________________

#calculate total votes
total_votes = len(candidates)
        
#add unique candidates 
for x in candidates:
    if x not in unique_candidates:
        unique_candidates.append(x)
        
#calculate votes for each candidate
for i in unique_candidates:
    votes.append(candidates.count(i))

#find winning candidate (with the most votes)
most_votes = max(votes)
winning_candidate = unique_candidates[votes.index(most_votes)]

#display analysis____________________________________________________________________

print(f'Election Results')
print(f'______________________________________________________________________________')
print(f'Total Votes: {total_votes}')
print(f'______________________________________________________________________________')

#display each candidate, percentage and total votes gathered 
for j in range(len(unique_candidates)):
    print(f'{unique_candidates[j]}: {round(votes[j]/total_votes*100,3)}% ({votes[j]})')

print(f'______________________________________________________________________________')
print(f'Winner: {winning_candidate}')
print(f'______________________________________________________________________________')

#export analysis as a text file___________________________________________________________

#specify file to write
output_path = os.path.join(".", "analysis.txt")

#write file
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['_______________________________________________________________________________________'])
    csvwriter.writerow(['Total Votes:' , str(total_votes)])
    csvwriter.writerow(['_______________________________________________________________________________________'])

    #write each candidate, percentage and total votes gathered 
    for j in range(len(unique_candidates)):
        csvwriter.writerow([unique_candidates[j], str(round(votes[j]/total_votes*100,3)) + '%', '(' + str(votes[j]) +')'])

    csvwriter.writerow(['_______________________________________________________________________________________'])
    csvwriter.writerow(['Winner:' , winning_candidate])
    csvwriter.writerow(['_______________________________________________________________________________________'])

    #end_________________________________________________________________________________