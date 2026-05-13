import re

logs = [
    "2025-01-01 10:30:00 - 192.168.0.10",
    "Invalid data line",
    "2025-01-02 11:00:00 - 10.0.0.5"
]

pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\d+\.\d+\.\d+\.\d+)'

for line in logs:
    try:
        match = re.search(pattern, line)

        if match:
            timestamp, ip = match.groups()
            print(f"Timestamp: {timestamp} | IP: {ip}")

    except Exception:
        continue