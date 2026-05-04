import urllib.parse as urlParser

url = input("Enter url: ")

parsed = urlParser.urlsplit(url)
base_url = f"{parsed.scheme}://{parsed.netloc}"
path = parsed.path

print(f"Base URL: \"{base_url}\"")
print(f"Path: \"{path}\"")