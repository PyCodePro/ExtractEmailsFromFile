import re

# Define the regex pattern for emails
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Open the input file and read its contents
with open('input.txt', 'r') as f:
    text = f.read()

# Find all matches of the email pattern in the text
matches = re.findall(email_pattern, text)

# Open the output file for writing
with open('output.txt', 'w') as f:
    # Write each email address on a new line in the output file
    for email in matches:
        f.write(email + '\n')
