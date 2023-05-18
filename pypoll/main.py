import os
import csv 

input_path = os.path.join(os.path.dirname(__file__), 'Resources', 'election_data.csv')
#print(input_path)

#def candidates(candidate_votes):
    

with open(input_path, 'r') as csvfile: 
    csvreader = csv.DictReader(csvfile)
    print(csvreader)

    
    Total_votes = 0
    Candidates_list = {}
    
    
    for row in csvreader:
        Total_votes += 1 
        #print(Total_votes)
        candidate = row["Candidate"]
       
       #if can exists in this dict, and its the 1st can(never existed before), start at one, otherwise keep counting 
        if candidate not in Candidates_list:
            Candidates_list[candidate] = 1
        else: 
            Candidates_list[candidate] +=1
            #printing inside for-loop will loop through whole file dict(declared above in reader) and show all that mess in terminal
#printing outside for-loop will just give simple final result
    print(Candidates_list)
        
output_path = os.path.join(os.path.dirname(__file__), 'analysis', 'Election Results.txt')
with open(output_path, "w") as E_R_file:
    E_R_file.write("Election Results\n")
    E_R_file.write("----------------------------\n")
    E_R_file.write("Total Votes: " + str(Total_votes))
    E_R_file.write("\n----------------------------\n")
    
                           
    for candidate, votes in Candidates_list.items():
        percent = votes/Total_votes * 100
        percent = round(percent, 3)
        E_R_file.write(candidate + ": " + str(percent) + "% (" + str(votes) + ")\n")

    winner= max(Candidates_list, key=Candidates_list.get)
    print(winner)
    E_R_file.write("----------------------------\n")
    E_R_file.write(winner + "\n")
    E_R_file.write("----------------------------\n")

