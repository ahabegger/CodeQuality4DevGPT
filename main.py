"""
main.py
This is the main file that will be run to start the program
"""

# Importing the external dependencies
import json
import os

# Importing the internal dependencies
from Extract import extract_data

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
print(f"Python Code Objects: {len(python_code_objects)}")
print(f"Java Code Objects: {len(java_code_objects)}")
print(f"Javascript Code Objects: {len(javascript_code_objects)}")

# Lint the code objects
print(python_code_objects[0])
print(python_code_objects[0].lint_code())


