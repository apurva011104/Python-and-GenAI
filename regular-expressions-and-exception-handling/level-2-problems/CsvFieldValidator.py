import re

emails = ["alex@corp.com", "wrong.email@"]

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

for email in emails:
    try:
        if re.match(pattern, email):
            print(f"Valid: {email}")
        else:
            print(f"Invalid: {email}")

    except Exception as e:
        print("Error:", e)