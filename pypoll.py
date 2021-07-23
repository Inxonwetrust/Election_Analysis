# Assign a variable for the file to load and the path
file_to_load= 'Resources/election_results.csv'
# open the election results and read the file
election_data= open(file_to_load, 'r')

# To do: perform analysis

#close the file
election_data.close()

# open the election results and read the file
with open(file_to_load) as election_data:

    # To do: perform analysis.
    print(election_data)

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes=0
#candidate options and candidate votes
candidate_options=[]
candidate_votes={}
#Track the winning candidate,vote count and percentage
winning_candidate= ""
winning_count=0
winning_percentage=0
#open the election results and read the file.
with open(file_to_load) as election_data:
    #To do: read and analyze data here.
    file_reader = csv.reader(election_data)
    #print the header row.
    headers = next(file_reader)
    #Print each row in the csv file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes +=1
        # print the candidate name from each row
        candidate_name = row[2]
        #If the candidate does not match any existing cadidate...
        if candidate_name not in candidate_options:
            #Add it to the list of candidates
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name]=0

        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1

# save the results to our text file
with open(file_to_save, "w") as txt_file:

    #Print the final vote count to the terminal
    election_results =(
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes:{total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")
# save final vote count to the text file
    txt_file.write(election_results)
    # Determine the percentage of votes for each candidate by looping through the counts.
        #1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #3. Calculate the percentage of votes.
        vote_percentage= float(votes)/float(total_votes)*100
        #votes to the terminal
        candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate voter count and percentage to terminal
        print(candidate_results)

        #save the candidate results to our text file.
        txt_file.write(candidate_results)
            #Determine winning vote count and candidate
            #Determine if votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                # if true the n set winning_count= votes and winning_percent = 
                # Vote_percentage
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate_name
                

    winning_candidate_summary=(
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"winning Vote Count: {winning_count:,}\n"
        f"winning Percentage: {winning_percentage:.1f}%\n"      
        f"------------------------\n" )
    print(winning_candidate_summary)
    #save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)
    







# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total numver of votes each candidate won
# 5. The winner of the election based on popular vote.
