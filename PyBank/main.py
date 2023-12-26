import os
import csv

#create lists 
date = []
profit_losses = []
changes = []

#read and store data____________________________________________________________________

#specify file to read 
budget_csv = os.path.join(".", "Resources", "budget_data.csv")

# read file
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#read header/skip 
    csv_header = next(csv_file)

    #loop through each row 
    for row in csv_reader:

        #add date
        date.append(row[0])
      
        #add profit_losses
        profit_losses.append(int(row[1]))

#loop through each row
for row in range(len(profit_losses)-1):
   
   #add changes 
   changes.append(profit_losses[row+1] - profit_losses[row])

#perform analysis________________________________________________________________________
   
number_of_months = len(date)

net_total = sum (profit_losses)

average_change = round((profit_losses[len(date)-1] - profit_losses[0])/(len(date)-1),2)

greatest_increase = max(changes)
date_of_greatest_increase = date[changes.index(greatest_increase)+1]

greatest_decrease = min(changes)
date_of_greatest_decrease = date[changes.index(greatest_decrease)+1]


#print analysis___________________________________________________________________________

print(f'Financial Analysis')
print(f'______________________________________________________________________________')
print(f'Total month: {number_of_months}')
print(f'Total: ${net_total}')
print(f'Average change: ${average_change}')
print(f'Greatest Increase in Profits: {date_of_greatest_increase} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {date_of_greatest_decrease} (${greatest_decrease})')

#export analysis as a text file___________________________________________________________

#specify file to write
output_path = os.path.join(".", "Analysis", "analysis.txt")

#write file
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['_______________________________________________________________________________________'])
    csvwriter.writerow(['Total month:' , '$' + str(number_of_months)])
    csvwriter.writerow(['Total', ('$' + str(net_total))])
    csvwriter.writerow(['Average change', ('$' + str(average_change))])
    csvwriter.writerow(['Greates Increase in Profit', date_of_greatest_increase, ('$' + str(greatest_increase))])
    csvwriter.writerow(['Greates Increase in Profit', date_of_greatest_decrease, ('$' + str(greatest_decrease))])

#end_______________________________________________________________________________________