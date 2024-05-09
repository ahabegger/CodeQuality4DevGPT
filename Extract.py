"""
Extract.py
This file defines a function that will be used to extract the code objects from the DevGPT Dataset
"""

# Importing the internal dependencies
from CodeClass import Code


def extract_data(json_object):
    """
    This function extracts the code objects from the json object
    :param json_object:
    :return: code_objects
    """

    code_objects = []

    # Extracting the data from the DevGPT Dataset
    for item in json_object["Sources"]:
        chatgpt_sharings = item["ChatgptSharing"]
        for chatgpt_sharing in chatgpt_sharings:
            try:
                title = chatgpt_sharing["Title"]
            except KeyError:
                title = "Untitled"
            try:
                model = chatgpt_sharing["Model"]
            except KeyError:
                model = "Unknown"

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
                        # Convert to UTF-8
                        code = code_object["Content"]
                        code = code.encode('utf-8').decode('utf-8')
                    except KeyError:
                        code = "No Code Found"

                    code_objects.append(Code(code, code_type, model, title))

    return code_objects
