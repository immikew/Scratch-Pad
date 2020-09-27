"""
# HW2 - Welcome

## Description

For this assignment, modify the function "welcome" that uses `input` to prompt
the user for their name and then welcomes them with "Hello Username", where
"Username" is the name that was entered by the user.

### Example Usage

>>> python3 hw2_welcome.py
What is your name?
Name: Username
Hello Username

## Instructions

Replace/alter the contents in between the START and END comments below with
your code to fulfill the requirements for this assignment.

### Requirements
- You *must* use `input` to prompt the user for a name
- You *must* print out a statment that addresses their name and uses the word
    "welcome" (see also Example Usage)
"""

def welcome():
    # START: Your code here
    
    username = input("What is your name?")
    print(f"Username: {username}")
    print(f"Hello and Welcome, {username}.")
    
    # END: Your code here

if __name__ == '__main__':
    welcome()