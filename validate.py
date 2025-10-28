
# part of lecture 7 Regular Expressions from CS50's python course

import re

email = input("Enter your email address: ")

if re.search('@',email):
    print("Valid email address.")
else:
    print("Invalid email address.")
