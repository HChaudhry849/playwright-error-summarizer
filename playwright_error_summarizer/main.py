import re
import itertools
import openai
import os
from dotenv import load_dotenv

load_dotenv() 
openai.api_key = os.getenv("OPENAI_API_KEY")
ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

def read_file():
    master_list = []
    with open("playwright-errors.txt", 'r', encoding='utf-16') as f:
        for line in f:
            master_list.append(line)
    return master_list

def clean_line(line):
    return ansi_escape.sub('', line).lstrip()
           
def find_error_start_indices(master_list):
    index_list = []
    counterr = 0
    pattern = re.compile(r"^\s*\d+\)")
    boundaryi = None
    for i, x in enumerate(master_list):
        clean = clean_line(x)
        if pattern.match(clean):
            counterr+=1
            index_list.append(i)
    boundaryi = i
    return counterr, index_list, boundaryi

def extract_error_blocks(counterr, index_list,master_list,boundaryi):
    block_list = []
    boundaryh = None  
    if counterr <2:
        for j in index_list:
            c = master_list[j:boundaryi]  
            block_list.append(c)
    elif counterr >1:
        boundaryh = 0
        for j,h in itertools.pairwise(index_list):
            c = master_list[j:h]  
            block_list.append(c)
        boundaryh = h

    if len(block_list) >=1 and counterr >1:
        ml = master_list[boundaryh:boundaryi]  
        block_list.append(ml)
    return block_list
   
def send_to_model(block_list):
    if not block_list:
        print("No errors to process.")
        return

    block_strings = ["".join(block) for block in block_list]
    prompt = (
        "I am getting the following errors in Playwright. "
        "I want you to summarise each error in less than 30 words and give me a hint which will help me fix them:\n"
        + "\n\n".join(block_strings)
    )

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7
    )
    reply = response.choices[0].message.content
    print("GPT response:\n", reply)
 

def main():
    try:
        master_list = read_file()
        counterr, index_list, boundaryi = find_error_start_indices(master_list)
        block_list = extract_error_blocks(counterr, index_list, master_list, boundaryi)
        send_to_model(block_list)
    except FileNotFoundError:
        print("The file does not exist.")
    except IOError:
        print("An error occurred while working with the file.")

if __name__ == "__main__":
    main()