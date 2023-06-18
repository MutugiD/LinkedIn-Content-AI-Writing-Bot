import os
import json
import openai
from time import time,sleep
from dotenv import load_dotenv
import json

import os 
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

completions_dir = "completions/"

if not os.path.exists(completions_dir):
    os.makedirs(completions_dir)

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

def save(content, file):
    with open(file, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

def gpt3_completion(prompt, engine='text-davinci-003', temp=1.0, 
                    top_p=1.0, tokens=1000, freq_pen=0.0, pres_pen=0.0, stop=['<<END>>']):
    max_retry = 5
    retry = 0
    while True:
        try:
            response = openai.Completion.create(
                engine=engine,
                prompt=prompt,
                temperature=temp,
                max_tokens=tokens,
                top_p=top_p,
                frequency_penalty=freq_pen,
                presence_penalty=pres_pen,
                stop=stop)
            text = response['choices'][0]['text'].strip()
            filename = '%s_gpt3.txt' % time()
            with open('gpt3_logs/%s' % filename, 'w') as outfile:
                outfile.write('PROMPT:\n\n' + prompt + '\n\n==========\n\nRESPONSE:\n\n' + text)
            return text
        except Exception as oops:
            retry += 1
            if retry >= max_retry:
                return "GPT3 error: %s" % oops
            print('Error communicating with OpenAI:', oops)
            sleep(1)

if __name__ == '__main__':
    files = os.listdir('prompts/')
    for file in files:
        prompt = open_file('prompts/' + file)
        completion = gpt3_completion(prompt)
        print('\n\n###########################\n\n', file, completion)
        save(completion, 'completions/' + file)
