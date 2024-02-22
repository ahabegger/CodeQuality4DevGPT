"""
Code.py
This file defines a Code class that will be used to store the code objects from the DevGPT Dataset
"""

# Defining the Code class
class Code:
    def __init__(self, code_content, code_language, model_used, title):
        self.code_content = code_content
        self.code_language = code_language
        self.model_used = model_used
        self.title = title

    def __str__(self):
        return f"Title: {self.title}\nModel Used: {self.model_used}\nCode Language: {self.code_language}\nCode Content: {self.code_content}"

    def print_small(self):
        print(f"Title: {self.title}")
        print(f"Model Used: {self.model_used}")
        print(f"Code Language: {self.code_language} \n")

    def is_language(self, language):
        return self.code_language == language


