
# part of lecture 7 Regular Expressions from CS50's python course

import re

email = input("Enter your email address: ")


pattern = r'^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$' # to escape the dot we use \. because dot means any character in regex
pattern = r'^(\w|\.)+@(\w+\.)?\w+\.edu$' # the same as above but using \w which means alphanumeric characters plus underscore

if re.search(pattern,email,flags=re.IGNORECASE): # IGNORECASE to make it case insensitive
    print("Valid email address.")
else:
    print("Invalid email address.")

