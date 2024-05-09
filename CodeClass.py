"""
CodeClass.py
This file defines a Code class that will be used to store the code objects from the DevGPT Dataset
"""

# Importing the external dependencies
import os
import subprocess
import re

# Ensure the environment includes the PATH
env = os.environ.copy()
env['PATH'] = os.getenv('PATH')


def array_to_frequency_dict(arr):
    freq_dict = {}
    for item in arr:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict


def extract_text_in_parentheses(s):
    return re.findall(r'\((.*?)\)', s)


def remove_items_with_numbers(arr):
    new_arr = []
    for item in arr:
        if not any(char.isdigit() for char in item):
            new_arr.append(item)
    return new_arr


def extract_rule_titles(lint_output):
    # Regex to find rule titles and their context in the linting output
    rule_pattern = re.compile(r'temp.java:\d+:\s+(.*?):\s+')

    # Try to extract rule titles using the regex pattern
    try:
        titles = rule_pattern.findall(lint_output)
        return titles
    except UnicodeEncodeError as e:
        print(f"Encoding error: {e}")
        # Optionally, handle the error or re-encode the input if necessary
        # For simplicity, this example just returns an error message
        return ["Error handling encoding in the input."]


def extract_js_rule_titles(lint_output):
    output = []
    for line in lint_output.split("temp.js:"):
        title = str(line).split(",")
        if len(title) > 1:
            output.append(title[2])
    return output


def remove_unwanted_items(report):
    report = [item for item in report if "available in ES6" not in str(item) and "Mozilla JS extensions" not in str(
        item) and "use 'esversion:" not in str(item)]
    return report


def classifying_errors(report):
    new_report = []
    for code in report:
        item = str(code).lower()
        if "missing semicolon" in item:
            new_report.append("missing semicolon")
        elif "unexpected comma" in item:
            new_report.append("unexpected comma")
        elif "unnecessary semicolon" in item:
            new_report.append("unnecessary semicolon")
        elif "unclosed regular expression" in item:
            new_report.append("unclosed regular expression")
        elif "strings must use doublequote" in item:
            new_report.append("string formatting")
        elif "se extra leading zero" in item or "decimal point can be conf" in item:
            new_report.append("confusing syntax")
        elif ("expected" in item) and ("to match" in item) and ("instead saw" in item):
            new_report.append("closing pair not used")
        elif "label" in item:
            new_report.append("labelling error")
        elif "missing initializer for constant" in item:
            new_report.append("missing initializer for constant")
        elif "has already been declared" in item:
            new_report.append("redeclaring variables")
        elif "attempting to override" in item:
            new_report.append("overiding constants")
        elif "was used before it was declared" in item:
            new_report.append("used before declared")
        elif "a reserved word" in item:
            new_report.append("use restricted word")
        elif "expected an identifier and instead saw" in item:
            new_report.append("incorrect identifier")
        elif "may only be used in module code" in item:
            new_report.append("module code error")
        elif "import" in item:
            new_report.append("general import error")
        elif "expected an operator and instead saw" in item:
            new_report.append("operator error")
        elif "functions declared within loops referencing an outer scoped" in item:
            new_report.append("unlocal variable call in function")
        elif "is better written in dot notation" in item:
            new_report.append("dot notation")
        elif "class properties must be methods" in item:
            new_report.append("class properties outside methods")
        elif "duplicate class method" in item:
            new_report.append("duplicate class methods")
        else:
            new_report.append("other error")

    return new_report


def get_loc(content):
    return len(content.split("\n"))


class Code:
    def __init__(self, code_content, code_language, model_used, title):
        self.code_content = code_content
        self.code_language = code_language
        self.model_used = model_used
        self.title = title
        self.errors = None
        self.eol = get_loc(code_content)

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

    def lint(self):
        error = []
        if self.code_language == 'python':
            # Use Pylint to lint the Python code
            filename = "temp." + self.get_code_extension()
            with open(filename, "w") as f:
                f.write(self.code_content)

            # Run the Pylint script with the appropriate arguments
            process = subprocess.Popen(["pylint", filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
            output, error = process.communicate()
            os.remove(filename)
            output = output.decode("utf-8")
            errors = extract_text_in_parentheses(output)
            filtered_errors = remove_items_with_numbers(errors)
            report = array_to_frequency_dict(filtered_errors)
            self.errors = report
        elif self.code_language == 'java':
            # Use PMD to lint the Java code
            filename = "temp." + self.get_code_extension()
            with open(filename, "w") as f:
                f.write(self.code_content)
            # Construct the path to the PMD executable script
            pmd_script = r"C:\pmd-bin-7.1.0\bin\pmd.bat"
            # Run the PMD script with the appropriate arguments
            # pmd.bat check -d c:\src -R rulesets/java/quickstart.xml -f text
            process = subprocess.Popen(
                [pmd_script, "check", "-d", filename, "-R", "rulesets/java/quickstart.xml", "-f", "text",
                 "--no-progress"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
            output, error = process.communicate()
            os.remove(filename)
            errors = output.decode("utf-8")
            rule_titles = extract_rule_titles(errors)
            report = array_to_frequency_dict(rule_titles)
            self.errors = report
        elif self.code_language == 'javascript':
            # Use JShint to lint the JavaScript code
            filename = "temp." + self.get_code_extension()
            with open(filename, "w") as f:
                f.write(self.code_content)

            jshint_path = r"C:\Program Files\nodejs\node.exe"
            jshint_script = r"C:\Users\alexh\AppData\Roaming\npm\node_modules\jshint\bin\jshint"

            process = subprocess.Popen([jshint_path, jshint_script, filename], stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE, env=env)
            output, error = process.communicate()
            os.remove(filename)
            errors = output.decode("utf-8")
            rule_titles = extract_js_rule_titles(errors)
            report = remove_unwanted_items(rule_titles)
            report = classifying_errors(report)
            report = array_to_frequency_dict(report)
            self.errors = report
