# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Initialize Variables
TotalMonths = 0
NetPL = 0.0
G_Inc = -1000.0
G_Inc_Name = ""
G_Dec = 1000.0
G_Dec_Name = ""

#Open cvs file and analyze
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        TotalMonths += 1
        compare = float(row[1])
        NetPL += compare
        if compare > G_Inc:
            G_Inc = compare
            G_Inc_Name = row[0]
        if compare < G_Dec:
            G_Dec = compare
            G_Dec_Name = row[0]

with open("./output.txt",'w') as textfile:
    textfile.write("Financial Analysis\n")
    print("Financial Analysis")
    textfile.write("----------------------------\n")
    print("----------------------------")
    textfile.write(f"Total Months: {TotalMonths}\n")
    print(f"Total Months: {TotalMonths}")
    textfile.write(f"Total: $%10.2f\n" % (NetPL))
    print(f"Total: $%10.2f" % (NetPL))
    textfile.write(f"Average  Change: $%10.2f\n" % (NetPL/TotalMonths))
    print(f"Average  Change: $%10.2f" % (NetPL/TotalMonths))
    textfile.write(f"Greatest Increase in Profits: {G_Inc_Name} ($%10.2f)\n" % (G_Inc))
    print(f"Greatest Increase in Profits: {G_Inc_Name} ($%10.2f)" % (G_Inc))
    textfile.write(f"Greatest Decrease in Profits: {G_Dec_Name} ($%10.2f)\n" % (G_Dec))
    print(f"Greatest Decrease in Profits: {G_Dec_Name} ($%10.2f)" % (G_Dec))

