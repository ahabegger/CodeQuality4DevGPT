from Code import Code

def extract_from_commit(commit_sharings):
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

    return code_objects