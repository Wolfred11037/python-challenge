import csv

def analyze_votes(filename):
    # Initialize variables
    total_votes = 0
    candidate_votes = {}
  
    # Read the CSV file
    filename = r"C:\Users\Wolfred\Documents\Data Analysis Boot Camp\Week 3\python-challenge\PyPoll\Resources\election_data.csv"
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        
        # Skip header row
        next(csvreader)
        
        # Loop through each row
        for row in csvreader:
            # Count the total number of votes
            total_votes += 1
            
            # Get the candidate's name from the row
            candidate_name = row[2]
            
            # Add the candidate to the dictionary and update the vote count
            if candidate_name in candidate_votes:
                candidate_votes[candidate_name] += 1
            else:
                candidate_votes[candidate_name] = 1
  
    # Calculate the percentage of votes each candidate won
    candidate_percentages = {}
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percentage = (votes / total_votes) * 100
        candidate_percentages[candidate] = round(percentage, 2)
  
    # Find the winner based on popular vote
    winner = max(candidate_votes, key=candidate_votes.get)
  
    # Print the analysis results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percentage = candidate_percentages[candidate]
        print(f"{candidate}: {percentage}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

# Run the analysis on the provided file
analyze_votes('election_data.csv')
