# Downloading Python Java and javascript code from the Stack Dedup Dataset
# Creating Code Objects for the Data
# Linting the Code Objects

# Importing the external dependencies
import random
import time
import requests

# Importing the internal dependencies
import WriteToCSV
from CodeClass import Code

# Set your personal access token.txt here
for line in open("token.txt"):
    token = line

# Headers to authenticate with GitHub API
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}


def fetch_repos(language):
    max_repos = 300  # Set the maximum number of repositories to fetch
    repos = []
    page = 1

    while len(repos) < max_repos:
        url = f"https://api.github.com/search/repositories?q=language:{language}+stars:2..100&sort=updated&page={page}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            rate_limit_remaining = int(response.headers.get('X-RateLimit-Remaining', 0))
            if rate_limit_remaining == 0:
                reset_time = int(response.headers.get('X-RateLimit-Reset', time.time())) + 10
                sleep_time = reset_time - time.time()
                if sleep_time > 0:
                    print(f"Rate limit exceeded. Sleeping for {sleep_time} seconds.")
                    time.sleep(sleep_time)
            page_data = response.json()['items']
            repos.extend(page_data)
            page += 1
            if not page_data:  # If there are no more repositories, break out of the loop
                break
        else:
            print(f'Failed to fetch repositories: {response.status_code}')
            break
        if len(repos) >= max_repos:  # Ensure not to fetch more than needed
            repos = repos[:max_repos]
    return repos


def get_random_file(repo_contents_url, file_extension):
    response = requests.get(repo_contents_url, headers=headers)
    if response.status_code == 200:
        files = [file['download_url'] for file in response.json() if file['name'].endswith(file_extension)]
        if files:
            return random.choice(files)
        else:
            return None
    else:
        print(f"Failed to access repository contents: {response.status_code}")
        return None


extension_map = {'python': '.py', 'java': '.java', 'javascript': '.js'}
results = []
human_java_code_objects = []


def extract_code_from_github(lang):
    count = 1
    time.sleep(1)  # Sleep for 1 second to avoid rate limiting
    print(f"Fetching repositories for {lang}")
    repos = fetch_repos(lang)
    print(f"Fetched {len(repos)} repositories")
    code_objects = []

    for repo in repos:
        contents_url = repo['contents_url'].replace('{+path}', '')  # Adjust URL to fetch root contents
        random_file_url = get_random_file(contents_url, extension_map[lang])
        if random_file_url:
            print(
                f"({count}/300) Testing Repository: {repo['name']} - URL: {repo['html_url']} - Random File: {random_file_url}")
            name = repo['name']
            file_url = random_file_url
            count += 1

            try:
                time.sleep(1)  # Sleep for 1 second to avoid rate limiting
                contents = requests.get(file_url, headers=headers).text
                code_object = Code(contents, lang, file_url, name)
                code_objects.append(code_object)
            except:
                continue

    return code_objects


python_code_objects = extract_code_from_github("python")
java_code_objects = extract_code_from_github("java")
javascript_code_objects = extract_code_from_github("javascript")

# Print the number of code objects
python_total_code = len(python_code_objects)
java_total_code = len(java_code_objects)
javascript_total_code = len(javascript_code_objects)
print(f"Python Code Objects: {python_total_code}")
print(f"Java Code Objects: {java_total_code}")
print(f"Javascript Code Objects: {javascript_total_code}")


# Lint Python Code Objects
print('-' * 50)
print("Human Python Code Linting")
print(f"Attempting to lint {python_total_code} Python Code Objects")
print('-' * 50)

count = 1
linting_failure = 0
for code in python_code_objects:
    print(f"({count}/{python_total_code}) {code.title}")
    count += 1
    try:
        code.lint()
        if code.errors is None:
            print(f"Failure Linting: {code.title} - {code.errors}")
            linting_failure += 1
        if 'astroid-error' in code.errors.keys():
            print(f"Failure Linting: {code.title} - astroid-error")
            linting_failure += 1
    except Exception as e:
        print(f"Failure Linting: {code.title} - Action Aborted - {e}")
        linting_failure += 1
        continue

print('-' * 50)
print("Human Python Code Linted")
print(f"Failure Rate: {linting_failure}/{python_total_code}")
print('-' * 50)

# Write the Python Code Objects to a CSV file
print('-' * 50)
print("Human Python Code Writing to CSV")
print('-' * 50)

WriteToCSV.write_python_to_csv(python_code_objects, "Human")


# Lint Java Code Objects
print('-' * 50)
print("Human Java Code Linting")
print(f"Attempting to lint {java_total_code} Java Code Objects")
print('-' * 50)

count = 1
linting_failure = 0
for code in java_code_objects:
    print(f"({count}/{java_total_code}) {code.title}")
    count += 1
    try:
        code.lint()
    except Exception as e:
        print(f"Failure Linting: {code.title} - Action Aborted - {e}")
        linting_failure += 1
        continue

print('-' * 50)
print("Human Java Code Linted")
print(f"Failure Rate: {linting_failure}/{java_total_code}")
print('-' * 50)

# Write the Java Code Objects to a CSV file
print('-' * 50)
print("Human Java Code Writing to CSV")
print('-' * 50)

WriteToCSV.write_java_to_csv(java_code_objects, "Human")


# Lint Javascript Code Objects
print('-' * 50)
print("Human Javascript Code Linting")
print(f"Attempting to lint {javascript_total_code} Javascript Code Objects")
print('-' * 50)

count = 1
linting_failure = 0
for code in javascript_code_objects:
    print(f"({count}/{javascript_total_code}) {code.title}")
    count += 1
    try:
        code.lint()
    except Exception as e:
        print(f"Failure Linting: {code.title} - Action Aborted - {e}")
        linting_failure += 1
        continue

print('-' * 50)
print("Human Javascript Code Linted")
print(f"Failure Rate: {linting_failure}/{javascript_total_code}")
print('-' * 50)

# Write the Javascript Code Objects to a CSV file
print('-' * 50)
print("Human Javascript Code Writing to CSV")
print('-' * 50)

WriteToCSV.write_javascript_to_csv(javascript_code_objects, "Human")
