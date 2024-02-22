"""
main.py
This is the main file that will be run to start the program
"""

# Importing the external dependencies
import json

# Importing the internal dependencies
from Extract import extract_data

# Getting data from the DevGPT Dataset
commit_sharings = json.load(open('DevGPT_Dataset/20231012_230826_commit_sharings.json', 'r'))
hn_sharings = json.load(open('DevGPT_Dataset/20231012_232232_hn_sharings.json', 'r'))
pr_sharings = json.load(open('DevGPT_Dataset/20231012_233628_pr_sharings.json', 'r'))
file_sharings = json.load(open('DevGPT_Dataset/20231012_234250_file_sharings.json', 'r'))
issue_sharings = json.load(open('DevGPT_Dataset/20231012_235128_issue_sharings.json', 'r'))
discussion_sharings = json.load(open('DevGPT_Dataset/20231012_235320_discussion_sharings.json', 'r'))

# Define List to store the code objects
code_objects = extract_data(commit_sharings)
code_objects += extract_data(hn_sharings)
code_objects += extract_data(pr_sharings)
code_objects += extract_data(file_sharings)
code_objects += extract_data(issue_sharings)
code_objects += extract_data(discussion_sharings)

# Find the type of code objects
python_code_objects = [code for code in code_objects if code.is_language("python")]
java_code_objects = [code for code in code_objects if code.is_language("java")]
javascript_code_objects = [code for code in code_objects if code.is_language("javascript")]

# Print the number of code objects
print(f"Python Code Objects: {len(python_code_objects)}")
print(f"Java Code Objects: {len(java_code_objects)}")
print(f"Javascript Code Objects: {len(javascript_code_objects)}")

# Lint the code objects
print(python_code_objects[0])
print(python_code_objects[0].lint_code())


