import re

data = """(  

 )"""

# Extract email addresses using regular expression
emails = re.findall(r'\S+@\S+', data)

# Remove duplicates
unique_emails = list(set(emails))

# Filter out email addresses that are not valid
valid_emails = [email for email in unique_emails if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)]

# Print the filtered email addresses
for email in valid_emails:
    print(email)
