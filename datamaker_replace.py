import os
import json
import random

# Set the path to the folder containing the images
folder_path = "photos"  # Replace with your folder path

# Get all the files in the folder
files = os.listdir(folder_path)

# Initialize lists for the JSON files
img_source = []
answer_list = []
qna_list = []

# Loop through the files
for file in files:
    if file.endswith(('.jpg', '.png','.webp')):  # Check if the file is an image
        # Split the filename to get the prefix (censor) and the rest (answer + extension)
        prefix, rest = file.split('-', 1)
        answer = os.path.splitext(rest)[0]  # Remove the file extension to get the answer
        
        # Append to the img_source list with 'censor' included
        img_source.append({
            "answer": answer,
            "file": rest,
            "censor": prefix
        })
        
        # Append the answer to the answer_list (only the answer part, without 'censor')
        answer_list.append(answer)

# Save img_source to img_source.json
with open('img_source.json', 'w') as img_source_file:
    json.dump(img_source, img_source_file, indent=4)

# Sort the answer_list alphabetically
answer_list = sorted(answer_list)

# Save answer_list to answer_list.json
with open('answer_list.json', 'w') as answer_list_file:
    json.dump(answer_list, answer_list_file, indent=4)

# Create qna.json by selecting random answers from the answer_list
for entry in img_source:
    answer = entry['answer']
    
    # Generate a random subset of the answer_list, ensuring the answer itself is included
    random_answers = random.sample(answer_list, 4)  # Select 3 random answers
    if answer not in random_answers:  # Ensure the current answer is included
        random_answers[random.randint(0, 2)] = answer
    random.shuffle(random_answers)
    # Append the entry to the qna_list
    qna_list.append({
        "answer": answer,
        "file": entry['file'],
        "censor": entry['censor'],
        "answer_list": random_answers
    })

# Save the qna_list to qna.json
with open('qna.json', 'w') as qna_file:
    json.dump(qna_list, qna_file, indent=4)

print("img_source.json, answer_list.json, and qna.json files created successfully!")
