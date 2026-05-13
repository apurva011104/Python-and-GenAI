import re

text = input("Enter data: ")

try:
    cleaned = re.sub(r'[^a-zA-Z0-9: ]', '', text)

    print("Cleaned Data:", cleaned)

except Exception as e:
    print("Error:", e)