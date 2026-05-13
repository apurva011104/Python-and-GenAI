import re

text = "Visit https://google.com and http://github.com"

urls = re.findall(r'https?://\S+', text)

print(urls)