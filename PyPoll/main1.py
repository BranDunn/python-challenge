# Dependencies
import pandas as pd

# Load in File from resources
election_file = "election_data.csv"

# Read and display preview with pandas
df_original = pd.read_csv(election_file)
df_original.head()

#find total number of votes cast
#check for empty rows
df_clean = df_original.dropna(how = 'any')
cast_total = df_clean['Voter ID'].count()
print('Total votes cast:', cast_total)

#make list of candidates who received votes
candidate_list_long = df_clean['Candidate']

# intilize a null list 
unique_cand_list = [] 
      
# traverse for all elements 
for x in candidate_list_long: 
        
    # check if exists in unique list or not 
    if x not in unique_cand_list: 
        unique_cand_list.append(x) 
            
print('Candidates who received votes:', unique_cand_list)

#find percentage of votes each candidate won
#get total for Khan
khan_count = 0

for i in candidate_list_long:
    if i == 'Khan':
        khan_count = khan_count + 1

        # percentage for Khan
        khan_share = (khan_count / cast_total) * 100

#get total and percentage for Correy
correy_count = 0

for i in candidate_list_long:
    if i == 'Correy':
        correy_count = correy_count + 1
        
        #percentage for Correy
        correy_share = (correy_count / cast_total) * 100

#get total and percentage for Li
li_count = 0

for i in candidate_list_long:
    if i == 'Li':
        li_count = li_count + 1
        
        #percentage for Li
        li_share = (li_count / cast_total) * 100

#get total and percentage for O'Tooley
otooley_count = 0

for i in candidate_list_long:
    if i == "O'Tooley":
        otooley_count = otooley_count + 1
        
        #percentage for O'Tooley
        otooley_share = (otooley_count / cast_total) * 100
        
print(otooley_share, "%", "of vote is for O'Tooley")
print(li_share, '%', 'of vote is for Li')
print(correy_share, '%', 'of vote is for Correy')
print(khan_share, '%', 'of vote is for Khan')

#find total number of votes each candidate won
print(khan_count, 'total votes for Khan')
print(correy_count, 'total votes for Correy')
print(li_count, 'total votes for Li')
print(otooley_count, "total votes for O'Tooley")

#find winner of the election based on popular vote
popular_vote = max([khan_count, correy_count, li_count, otooley_count])

if popular_vote == khan_count:
    winner = 'Khan'
if popular_vote == correy_count:
    winner = 'Correy'
if popular_vote == li_count:
    winner = "Li"
if popular_vote == otooley_count:
    winner = "O'Tooley"
print(winner, 'wins!')