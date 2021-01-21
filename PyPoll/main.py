import os
import csv


csvpath = os.path.join("..", "Resources", "week-3-python_homework_PyPoll_Resources_election_data.csv")
csvpath_output = ("analysis2.txt")

candidate = []
percetage_list = []



#The total number of votes cast
with open(csvpath, "r")  as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    total = len(list(csvreader))
    print(f"Total Votes: {total}")

#A complete list of candidates who received votes

with open(csvpath, "r")  as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for column in csvreader:
        candidate.append(column[2])
    candidate_list = list(set(candidate))
    print(candidate_list)

#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

with open(csvpath, "r")  as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    Correy = candidate.count('Correy')
    Khan = candidate.count('Khan')
    OTooley = candidate.count("O'Tooley")
    Li = candidate.count('Li')
    Percentage_Correy = round((Correy / total) * 100)
    Percentage_Khan = round((Khan / total) * 100)
    Percentage_OTooley = round((OTooley / total) * 100)
    Percentage_Li = round((Li / total) * 100)

    print(f"Correy has {Correy} votes and got {Percentage_Correy}% of the votes")
    print(f"Khan has {Khan} votes and got {Percentage_Khan}% of the votes")
    print(f"OTooley has {OTooley} votes and got {Percentage_OTooley}% of the votes")
    print(f"Li has {Li} votes and got {Percentage_Li}% of the votes")

    if Khan > Correy and Khan > OTooley and Khan > Li:
        print("Khan won")
    elif Correy > Khan and Correy > OTooley and Correy > Li:
        print("Correy won")
    elif OTooley > Khan and OTooley  > Correy and OTooley > Li:
        print("OTooley won")
    else: 
        print("Li won")
            
# Output Files
with open(csvpath_output, "w") as txt_file:
    txt_file.write(str(total))
    txt_file.write("\n")
    txt_file.write(str(candidate_list))
    txt_file.write("\n")
    txt_file.write(str(f"Correy has {Correy} votes and got {Percentage_Correy}% of the votes"))
    txt_file.write("\n")
    txt_file.write(str(f"Khan has {Khan} votes and got {Percentage_Khan}% of the votes"))
    txt_file.write("\n")
    txt_file.write(str(f"OTooley has {OTooley} votes and got {Percentage_OTooley}% of the votes"))
    txt_file.write("\n")
    txt_file.write(str(f"Li has {Li} votes and got {Percentage_Li}% of the votes"))
    txt_file.write("\n")
    txt_file.write("Khan won")
    txt_file.write("\n")
txt_file.close()
