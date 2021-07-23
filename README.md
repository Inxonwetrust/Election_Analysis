# Election Analysis with Python
Click here to view the Python file: [Election Analysis](https://github.com/Inxonwetrust/Election_Analysis/blob/main/PyPoll_Challenge.py)

## Overview of Election Audit
The purpose of this project was to complete an election audit of a recent local congressional election. The follow tasks included:
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote. 

### The Data
The data presented includes three columns: ballot ID, county, and candidate name. Through this data we were able to provide dictionaries to the data and define the votes for each candidate. After the votes were casted to determine the amount of votes for each candidate I wrote a code script that gathered a percentage of the votes. In most elections there needs to be a majority vote to win as well as satisfying the percentage minimum in order to win an election typically greater than 50%. After the script runs it was able to pick the winner based on the vote count of the participant.

## Election Audit Results

The total amount of votes that were cased in the congressional election was 369,711. Diana Degete received the most votes within this election, winning 82.8% of the total votes. Jefferson won 10.5% of the total votes, whereas Arapahoe only won 6.7% of the total votes.

As for the candidates, Diana DeGette received the most votes, which was 73.8% of all votes or  272,892 votes. The second place candidate, Charles Casper Stockham, received 23% of the total votes. Finally, the third candidate, Raymon Anthony Doane, only received 3.1% of the overall votes. 

## Election Audit Summary
This script can be modified to find the most number of votes for different filters other than candidates and county. If the data included other characteristics, such as demographics and geography, the script can be modified to include these characteristics and the analysis can be broken down even further.

This script can also be modified to determine patterns among the characteristics. We could test the percentage of voters by county against each candidate. This would allow us to see which candidate was the most popular within a county or geographical area. 
