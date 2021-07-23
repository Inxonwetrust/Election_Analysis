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
# Open the election results and read the file
with open(file_to_load) as election_data:
    #print the file object.
    print(election_data)

# create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# using the open() function witht the "w" mode we will write data to the file.
open(file_to_save, "w")

#create a filename variable to a direct or indirect path to the file
file_to_save=os.path.join("analysis","election_analysis.txt")

#Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file
outfile.write("Hello World")

#close the file
outfile.close()

#create a filename variable to a direct or indirect path to the file
file_to_save= os.path.join("analysis", "election_analysis.txt")

#Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:


    # Write three counties to the file
    txt_file.write("Arapahoe\nDenver\nJefferson")

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load= os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.
file_to_save=os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze data here.
    file_reader = csv.reader(election_data)

    #print the header row.
    headers = next(file_reader)
    print(headers)


# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total numver of votes each candidate won
# 5. The winner of the election based on popular vote.
