# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Initialize Variables
Total_Votes = 0
Vote_Dict = {}
Winner_Value = 0
Winner_Name = ""
Print_String = ""


#Open cvs file and analyze
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        Total_Votes += 1
        name = row[2]

        if name in Vote_Dict:
            Vote_Dict[name]+=1

        else:
            Vote_Dict[name] = 1

Print_String = (
    "Election Results\n" 
    "-------------------------\n"
    "Total Votes: " 
    + str(Total_Votes) + "\n")

for key, value in Vote_Dict.items() :
    Print_String = (
        Print_String
        + f"{key}: %3.3f%% ({value})\n" % (value/Total_Votes*100))
   
    if value > Winner_Value:
        Winner_Value = value
        Winner_Name = key

Print_String = (
    Print_String
    + "-------------------------\n" 
    + f"Winner: {Winner_Name}\n"
    "-------------------------")
    
print(Print_String)

with open("./output.txt",'w') as textfile:
    textfile.write(Print_String)