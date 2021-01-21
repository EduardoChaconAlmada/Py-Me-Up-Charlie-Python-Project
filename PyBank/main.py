import os
import csv


csvpath = os.path.join("..", "Resources", "week-3-python_homework_PyBank_Resources_budget_data.csv")
csvpath_output = ("analysis1.txt")

#The total number of months included in the dataset
with open(csvpath, "r")  as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    total = len(list(csvreader))
    print(total)
    
#The net total amount of "Profit/Losses" over the entire period
with open(csvpath, "r")  as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  
    total2 = 0
    for row in csvreader:
        total2 = total2 + int(row[1])
    print(total2)
        
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
with open(csvpath, "r")  as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    before = 0
    changetotal = 0
    y = 0
    for row in csvreader:
        if before != 0:
            change = int(row[1]) - int(before)
            changetotal = int(change) + int(changetotal)
            before = row[1]
            y = y + 1
        else:
            before = row[1]
    averagechange = changetotal / y 
    print(averagechange)

#The greatest increase in profits (date and amount) over the entire period
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    before = 0
    Maxchange = 0
    for row in csvreader:
        if before != 0:
            change = int(row[1]) - int(before)
            if change > Maxchange:
                Maxchange = change
                Maxmonth = row[0]
            before = row[1]
        else:
            before = row[1]
    print(f"{Maxmonth} with ${Maxchange}" )

#The greatest decrease in losses (date and amount) over the entire period

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    before = 0
    Maxloss = 0
    for row in csvreader:
        if before != 0:
            change = int(row[1]) - int(before)
            if change < Maxloss:
                Maxloss = change
                Minmonth = row[0]
            before = row[1]
        else:
            before = row[1]
    print(f"{Minmonth} with ${Maxloss}" )

# Output Files
with open(csvpath_output, "w") as txt_file:
    txt_file.write(str(total))
    txt_file.write("\n")
    txt_file.write(str(total2))
    txt_file.write("\n")
    txt_file.write(str(averagechange))
    txt_file.write("\n")
    txt_file.write(f"{Maxmonth} with ${Maxchange}" )
    txt_file.write("\n")
txt_file.close()