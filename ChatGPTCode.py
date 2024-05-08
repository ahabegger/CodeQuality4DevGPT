"""
ChatGPTCode.py
This is the main file that will be run to start the program
"""

# Importing the external dependencies
import json
import os

# Importing the internal dependencies
from Extract import extract_data
from WriteToCSV import write_python_to_csv, write_java_to_csv, write_javascript_to_csv

# Define List to store the code objects
code_objects = []

# Getting data from the DevGPT Dataset
for file in os.listdir("DevGPT_Dataset"):
    if file.endswith(".json"):
        with open(os.path.join("DevGPT_Dataset", file), "r") as f:
            code_objects += extract_data(json.load(f))

# Find the type of code objects
python_code_objects = [code for code in code_objects if code.is_language("python")]
java_code_objects = [code for code in code_objects if code.is_language("java")]
javascript_code_objects = [code for code in code_objects if code.is_language("javascript")]

# Print the number of code objects
python_total_code = len(python_code_objects)
java_total_code = len(java_code_objects)
javascript_total_code = len(javascript_code_objects)
print(f"Python Code Objects: {python_total_code}")
print(f"Java Code Objects: {java_total_code}")
print(f"Javascript Code Objects: {javascript_total_code}")

# Lint Python Code Objects
print('-' * 50)
print("ChatGPT Python Code Linting")
print(f"Attempting to lint {python_total_code} Python Code Objects")
print('-' * 50)

count = 1
linting_failure = 0
for code in python_code_objects:
    print(f"({count}/{python_total_code}) {code.title}")
    try:
        code.lint()
    except Exception as e:
        print(f"Failure Linting: {code.title} - Action Aborted - {e}")
        linting_failure += 1
        continue

print('-' * 50)
print("ChatGPT Python Code Linted")
print(f"Failure Rate: {linting_failure}/{python_total_code}")
print('-' * 50)

# Write the Python Code Objects to a CSV file
print('-' * 50)
print("ChatGPT Python Code Writing to CSV")
print('-' * 50)

write_python_to_csv(python_code_objects, "ChatGPT")

# Lint Java Code Objects
print('-' * 50)
print("ChatGPT Java Code Linting")
print(f"Attempting to lint {java_total_code} Java Code Objects")
print('-' * 50)

count = 1
linting_failure = 0
for code in java_code_objects:
    print(f"({count}/{java_total_code}) {code.title}")
    try:
        code.lint()
    except Exception as e:
        print(f"Failure Linting: {code.title} - Action Aborted - {e}")
        linting_failure += 1
        continue

print('-' * 50)
print("ChatGPT Java Code Linted")
print(f"Failure Rate: {linting_failure}/{java_total_code}")
print('-' * 50)

# Write the Java Code Objects to a CSV file
print('-' * 50)
print("ChatGPT Java Code Writing to CSV")
print('-' * 50)

write_java_to_csv(java_code_objects, "ChatGPT")

# Lint Javascript Code Objects
print('-' * 50)
print("ChatGPT Javascript Code Linting")
print(f"Attempting to lint {javascript_total_code} Javascript Code Objects")
print('-' * 50)

count = 1
linting_failure = 0
for code in javascript_code_objects:
    print(f"({count}/{javascript_total_code}) {code.title}")
    try:
        code.lint()
    except Exception as e:
        print(f"Failure Linting: {code.title} - Action Aborted - {e}")
        linting_failure += 1
        continue

print('-' * 50)
print("ChatGPT Javascript Code Linted")
print(f"Failure Rate: {linting_failure}/{javascript_total_code}")
print('-' * 50)

# Write the Javascript Code Objects to a CSV file
print('-' * 50)
print("ChatGPT Javascript Code Writing to CSV")
print('-' * 50)

write_javascript_to_csv(javascript_code_objects, "ChatGPT")
