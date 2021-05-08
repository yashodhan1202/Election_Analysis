import csv
import os

# Assign variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")

# Assign variable to save the path
file_to_save = os.path.join("analysis","election_analysis.txt")

# Initialize the total vote counter to zero
total_votes = 0

#Candidate option variable declared
candidate_options = []

# Declare an empty dictionary for combination of candidate and its corresponding votes
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Print the header row
    headers = next(file_reader)
    
    # Print each row under the header
    for row in file_reader:
        # Add 1 to total votes
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # if candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add candidate name from each row
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to the count if candidate name appears 
        candidate_votes[candidate_name] += 1
    
    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
         # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
             # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    winning_candidate_summary = (f'---------------\n'
                                f'Winner: {winning_candidate}\n'
                                f'Winning vote count: {winning_count:,}\n'
                                f'Winning percentage: {winning_percentage:.1f}%\n'
                                f'----------------\n')
    print(winning_candidate_summary)    

