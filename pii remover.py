import json
import re

# Load your JSON file (replace 'your_file.json' with the actual file path)
with open('file.json', 'r') as json_file:
    data = json.load(json_file)

# Define regular expressions for names, phone numbers, and emails
#name_pattern = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'
phone_pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}\b'

# Function to find and print personal information
def find_personal_info(data, path=''):
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{path}.{key}" if path else key
            find_personal_info(value, new_path)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_path = f"{path}[{i}]"
            find_personal_info(item, new_path)
    elif isinstance(data, str):
       # names = re.findall(name_pattern, data)
        phones = re.findall(phone_pattern, data)
        emails = re.findall(email_pattern, data)

        #if names:
           # print(f"Names found in '{path}': {names}")
        if phones:
            print(f"Phone numbers found in '{path}': {phones}")
        if emails:
            print(f"Email addresses found in '{path}': {emails}")

# Start searching for personal information
find_personal_info(data)
