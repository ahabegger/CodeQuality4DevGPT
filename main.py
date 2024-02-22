"""
main.py
- This is the main file that will be run to start the program
"""

# Importing the required modules
import json

from Code import Code

# Getting data from the DevGPT Dataset
commit_sharings = json.load(open('DevGPT_Dataset/20231012_230826_commit_sharings.json', 'r'))
hn_sharings = json.load(open('DevGPT_Dataset/20231012_232232_hn_sharings.json', 'r'))
pr_sharings = json.load(open('DevGPT_Dataset/20231012_233628_pr_sharings.json', 'r'))
file_sharings = json.load(open('DevGPT_Dataset/20231012_234250_file_sharings.json', 'r'))
issue_sharings = json.load(open('DevGPT_Dataset/20231012_235128_issue_sharings.json', 'r'))
discussion_sharings = json.load(open('DevGPT_Dataset/20231012_235320_discussion_sharings.json', 'r'))

# Define Empty List to store the code objects
code_objects = []

# Extracting the data from the DevGPT Dataset
for commit in commit_sharings["Sources"]:
    chatgpt_sharings = commit["ChatgptSharing"]
    for chatgpt_sharing in chatgpt_sharings:
        try:
            title = chatgpt_sharing["Title"]
        except KeyError:
            title = "Untitled"
        try:
            model = chatgpt_sharing["Model"]
        except KeyError:
            model = "Unknown"

        print(f"Title: {title}")
        print(f"Model: {model}")

        try:
            conservations = chatgpt_sharing["Conversations"]
        except KeyError:
            conservations = []

        for conservation in conservations:
            code_list = conservation["ListOfCode"]

            for code_object in code_list:
                try:
                    code_type = code_object["Type"]
                except KeyError:
                    code_type = "Unknown"
                try:
                    code = code_object["Content"]
                except KeyError:
                    code = "No Code Found"

                print(f"Code Type: {code_type}")

                code_objects.append(Code(code, code_type, model, title))


python_code_objects = [code for code in code_objects if code.is_language("python")]
java_code_objects = [code for code in code_objects if code.is_language("java")]
javascript_code_objects = [code for code in code_objects if code.is_language("javascript")]


print(f"Python Code Objects: {len(python_code_objects)}")
print(f"Java Code Objects: {len(java_code_objects)}")
print(f"Javascript Code Objects: {len(javascript_code_objects)}")
