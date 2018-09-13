# Dependencies
import pandas as pd

# Load in File from resources
budget_file = "budget_data.csv"

## Read and display preview with pandas
df_original = pd.read_csv(budget_file)
df_original.head(13)

#determine if any empty rows are present and remove them
df_original.count()

df_clean = df_original.dropna(how='any')
df_clean.count()

#find total number of months included in the dataset
print('Total number of months included:', df_clean['Date'].count(), 'months')
with open('PyBank.txt', "w") as text_file:
    text_file.write('Total number of months included:', df_clean['Date'].count(), 'months')
#find total net amount of "Profit/Losses" over the entire period
print('Net Profit/Losses over the entire period: $', df_clean['Profit/Losses'].sum())
    text_file.write('Net Profit/Losses over the entire period: $', df_clean['Profit/Losses'].sum())
#find average change in "Profit/Losses" between months over the entire period
#create second column for comparison
df_clean['Value Shift'] = df_clean['Profit/Losses'].shift(1)
df_clean['Difference'] = df_clean['Profit/Losses'] - df_clean['Value Shift']
print('Average change in Profit/Losses between months for entire period: $', df_clean['Difference'].mean())
    text_file.write('Average change in Profit/Losses between months for entire period: $', df_clean['Difference'].mean())
#preview new columns
df_clean.head()

#find greatest increase in profits (date and amount) over the entire period
greatest_gain = df_clean['Difference'].max()

#if greatest_dif value is found in the 'Difference' column, then print the 'Date' column value for that row with the greatest_dif. 
print('Greatest Increase:')
print(df_clean.loc[df_clean['Difference'] == greatest_gain])
    text_file.write('Greatest Increase:')
    text_file.write(df_clean.loc[df_clean['Difference'] == greatest_gain])

#find greatest decrease in losses (date and amount) over the entire period
greatest_decrease = df_clean['Difference'].min()

print('Greatest Decrease:')
print(df_clean.loc[df_clean['Difference'] == greatest_decrease])
    text_file.write('Greatest Decrease:')
    text_file.write(df_clean.loc[df_clean['Difference'] == greatest_decrease])