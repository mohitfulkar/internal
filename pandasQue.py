import pandas as pd 
# Specify the file path 
csv_file_path = r'D:\MCA SEM-2\Python\mtcars.csv' 
# Read the CSV file into a DataFrame 
df = pd.read_csv(csv_file_path) 
# Print the column names 
print(df.columns) 

#----------------------------------------------------------------
#average of a column
import pandas as pd 
 
# Read the CSV file into a DataFrame 
df = pd.read_csv(r'D:\MCA SEM-2\Python\cricket.csv') 
 
# Calculate the average of catches taken by all cricketers 
average_catches = df['catches'].mean() 
 
# Print the average catches taken 
print(f'Average catches taken by all cricketers: {average_catches:.2f}') 


#----------------------------------------------------------------
#highest number of matches

import pandas as pd 
 
# Read the CSV file into a DataFrame 
df = pd.read_csv(r'D:\MCA SEM-2\Python\cricket.csv') 
 
# Find the index of the row with the highest number of matches played 
highest_matches_index = df['matches'].idxmax() 
 
# Get the name of the bowler with the highest matches played 
highest_matches_bowler = df.loc[highest_matches_index, 'name'] 
 
# Print the name of the bowler with the highest matches played 
print(f'The bowler who played the highest number of matches is: 
{highest_matches_bowler}') 




#----------------------------- ----------------------------------------------------------------
#barchart
import pandas as pd 
import matplotlib.pyplot as plt 
# Read the CSV file into a DataFrame 
df = pd.read_csv(r'D:\MCA SEM-2\Python\cricket.csv') 
# Extract 'Matches' and 'Runs' columns 
matches = df['matches'] 
runs = df['runs'] 
# Plotting the bar chart 
plt.figure(figsize=(10, 6))  # Set the figure size 
plt.bar(matches, runs, color='skyblue')  # Plot the bar chart 
plt.xlabel('Matches')  # Set the x-axis label 
plt.ylabel('Runs Scored')  # Set the y-axis label 
plt.title('Matches vs Runs Scored')  # Set the title 
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility 
plt.tight_layout()  # Adjust layout to prevent clipping of labels 
plt.show()  # Display the plot 

#----------------------------------------------------------------
#ascending order of runs
import pandas as pd 
# Read the CSV file into a DataFrame 
df = pd.read_csv(r'D:\MCA SEM-2\Python\cricket.csv') 
# Sort the DataFrame by 'runs' column in ascending order 
sorted_df = df.sort_values(by='runs', ascending=True) 
# Print the sorted DataFrame 
print(sorted_df) 