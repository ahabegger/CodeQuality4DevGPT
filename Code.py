"""
Code.py
This file defines a Code class that will be used to store the code objects from the DevGPT Dataset
"""

# Importing the external dependencies
import subprocess
import tempfile
import re


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
        # Create a temporary file
        with tempfile.NamedTemporaryFile(suffix='.' + self.code_language, delete=False) as temp:
            # Write the code_content to the temporary file
            temp.write(self.code_content.encode())
            temp.flush()

            # Run coala on the temporary file
            result = subprocess.run(['coala', '--files', temp.name, '--json'], capture_output=True, text=True)

            # Parse the output of coala to get the number of errors and error types
            output = result.stdout
            error_pattern = re.compile(r'"origin": "(.*?)", "message": "(.*?)"')
            errors = error_pattern.findall(output)

            # Return the number of errors and error types
            return len(errors), {origin: sum(1 for error in errors if error[0] == origin) for origin, _ in errors}
