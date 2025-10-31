
import re

url = input("Enter your Twitter URL: ").strip()

# pattern = r'^https?://(www\.)?twitter\.com/([A-Za-z0-9_]{1,15})/?$' added by github copilot

if matches:= re.search(r"^https?://(www\.)?twitter\.com/([a-z0-9_]+)",url, re.IGNORECASE):

    print(f"Valid Twitter handle: {matches.group(2)}")
else:
    print("Invalid Twitter URL.")


# I finished the lecture