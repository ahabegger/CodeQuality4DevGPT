"""
Code.py
This file defines a Code class that will be used to store the code objects from the DevGPT Dataset
"""

import json
import subprocess
import os


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

    def get_code_extension(self):
        if self.code_language == "python":
            return "py"
        elif self.code_language == "java":
            return "java"
        elif self.code_language == "javascript":
            return "js"
        else:
            return "txt"

    def lint_code(self):
        # Get the proper bears for the code language
        if self.code_language == "python":
            bears = "PEP8Bear,PyCodeStyleBear"
        elif self.code_language == "java":
            bears = "JavaCheckStyleBear"
        elif self.code_language == "javascript":
            bears = "ESLintBear"
        else:
            return "No linter available for this language"

        # Create a file
        file_path = 'file' + '.' + self.get_code_extension()

        with open(file_path, 'w') as file:
            # Write the code_content to the temporary file
            file.write(self.code_content)

        # Use subprocess.run to execute coala and wait for it to complete
        result = subprocess.run(['coala', '--files=file.py', '--bears=' + bears, '-I', '--json'],
                                capture_output=True, text=True)

        # Remove the temporary file
        os.remove(file_path)

        return json.loads(result.stdout)
