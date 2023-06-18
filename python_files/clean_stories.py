import pandas as pd
import numpy as np 
import os 
import os
import re
import nltk
from nltk.corpus import stopwords


data = pd.read_csv("stories.csv")
df = data[['ShareCommentary']].dropna()
stories = df['ShareCommentary'].str.split('\n').str[0].str.strip().tolist()
directory = 'clean_files'
os.makedirs(directory, exist_ok=True)

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

start_index = 0
end_index = len(df) - 1

# Custom list of words to remove
custom_words = ['and', 'but']

# Function to remove URLs from text
def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub('', text)

# Iterate through the desired range of row indices and save each row as a separate text file
for row_index in range(start_index, end_index + 1):
    # Extract the desired row
    story = df['ShareCommentary'].iloc[row_index]
    
    # Remove URLs
    story = remove_urls(story)
    words = story.lower().split()
    words = [word for word in words if word not in custom_words and word not in stop_words]
    cleaned_story = ' '.join(words)
    file_path = os.path.join(directory, f'story_{row_index}.txt')
    with open(file_path, 'w') as file:
        file.write(cleaned_story)

    print(f'Saved story {row_index} to {file_path}')