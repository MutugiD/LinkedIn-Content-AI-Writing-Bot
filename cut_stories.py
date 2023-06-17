import pandas as pd
import numpy as np 
import os 

data = pd.read_csv("stories.csv")
df = data[['ShareCommentary']].dropna()

stories = df['ShareCommentary'].str.split('\n').str[0].str.strip().tolist()
directory = 'files'
os.makedirs(directory, exist_ok=True)

# Specify the range of row indices you want to extract (from 0 to n-1)
start_index = 0
end_index = len(df) - 1

for row_index in range(start_index, end_index + 1):
    # Extract the desired row
    story = df['ShareCommentary'].iloc[row_index]
    file_path = os.path.join(directory, f'story_{row_index}.txt')
    with open(file_path, 'w') as file:
        file.write(story)
    print(f'Saved story {row_index} to {file_path}')
