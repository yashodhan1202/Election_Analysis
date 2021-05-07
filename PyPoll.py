import csv
import os

# Assign variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")

# Assign variable to save the path
file_to_save = os.path.join("analysis","election_analysis.txt")

# Initialize the total vote counter to zero
total_votes = 0

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

print(total_votes)
