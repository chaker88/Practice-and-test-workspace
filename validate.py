
# part of lecture 7 Regular Expressions from CS50's python course

import re

email = input("Enter your email address: ")


pattern = r'.+@.+\.edu' # to escape the dot we use \. because dot means any character in regex


if re.search(pattern,email):
    print("Valid email address.")
else:
    print("Invalid email address.")

# I stopped at 30:00 minutes
