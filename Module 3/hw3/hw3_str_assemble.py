"""
# HW 3 - Stringers Assemble!

## Description

For this assignment, modify the function "str_concat" prompt the user for the
following strings:

- A date/time stamp
- A status (i.e. Info, Warning, Critical)
- A Message

Using these three variables and your preferred string formatting method such as
f-strings or `.format()`, assemble and print a message that looks like this:

"[<date/time>]: (<status>) <message>"

### Example usage

>>> python3 hw3_str_assemble.py
Please enter a Date & Time stamp:
10-30-2020 0630
Please enter a Status:
Critical
Please enter a Message:
Time to wake up!
[10-30-2020 0630]: (Critical) Time to wake up!


## Instructions

Replace/alter the contents in between the START and END comments below with
your code to fulfill the requirements for this assignment.

### Requirements
- You *must* use `input` to prompt the user for the string values.
- You *must* print out the combination of the variables using this template:

    [<date/time>]: (<status>) <message>

    where <date/time> is replaced by the user entered date & time stamp,
    <status> is replaced by the user entered status, and <message> is replaced
    by the sure entered message.
"""

def str_assemble():
    # START: your code here
    time_input = input('Please enter a Date & Time stamp: ')
    print(time_input)

    status_input = input('Please enter a Status: ')
    print(status_input)

    message_input = input('Please enter a Message: ')
    print(message_input)

    print(f'[{time_input}]: ({status_input}) {message_input}')
    # END: your code here

if __name__ == "__main__":
    str_assemble()
