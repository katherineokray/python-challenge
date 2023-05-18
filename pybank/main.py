import os
import csv 

input_path = os.path.join(os.path.dirname(__file__), 'Resources', 'budget_data.csv')
#print(input_path)

with open(input_path, 'r') as csvfile: 
    csvreader = csv.DictReader(csvfile)

    Total_months = 0
    Net_total = 0 
    x=-1 
    Change = []
    
    for row in csvreader:
        Total_months += 1 
        #print(row)
        
        Net_total += int(row['Profit/Losses'])
        #print(Net_total)
        
        if x != -1:
            Change.append(int(row['Profit/Losses'])-x)
        x= int(row['Profit/Losses'])
#print(Change)

Sum = sum(Change)
#print(Sum)

Average = Sum/len(Change)
#print(Average)
        
greatest_increase = max(Change)
#print(greatest_increase)

greatest_decrease = min(Change)
print(greatest_decrease)
        
        
        
output_path = os.path.join(os.path.dirname(__file__), 'Analysis', 'Financial Analysis.txt')
#print(output_path)
with open(output_path, 'w') as F_A_file: 
    F_A_file.write("Financial Analysis\n")
    F_A_file.write("----------------------------\n")
    F_A_file.write(f"Total Months: {Total_months}\n")
    F_A_file.write(f"Total: $ {Net_total}\n")
    F_A_file.write(f"Average Change: $ {Average}\n")
    F_A_file.write(f"Greatest Increase in Profits: $ {greatest_increase}\n")
    F_A_file.write(f"Greatest Decrease in Profits: $ {greatest_decrease}\n")  