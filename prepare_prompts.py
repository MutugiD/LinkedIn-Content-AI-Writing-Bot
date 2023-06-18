import os


prompts_dir = "prompts/"

if not os.path.exists(prompts_dir):
    os.makedirs(prompts_dir)
    
def read(file):
    with open(file, 'r', encoding='utf-8') as infile:
        return infile.read()

def save(content, file):
    with open('prompts/%s' % file, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

files = os.listdir('stories/')
for file in files:
    content = read('stories/' + file)
    if len(content) > 5000:
        content = content[0:5000] + '\n\n #### STORY TRUNCATED DUE TO LENGTH #### '
    prompt = read('prompt.txt').replace('<<STORY>>', content)
    save(prompt, file)