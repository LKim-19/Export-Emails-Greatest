name = "mbox-short.txt"
handle = open(name)

emails = dict()

# For loop to split the lines up into individual words
# in the file into a list
for line in handle:
    x = line.split()
    # If From exists in the split list it will get the email and append it to the dictionary, adding one count
    # As it continues to read the file if similar emails pop up it will increase the count by 1
    if 'From' in x:
        emails[x[1]] = emails.get(x[1], 0) + 1

# Sets the variables message and email to None
messages = None
email = None

# For loop to basically they key,value pair from the emails dictionary by calling its items
for emails, number in emails.items():
    # If email is None or the number is larger than messages then it assigns the email and messages to
    # the largest email with the largest messages
    if email is None or number > messages:
        email = emails
        messages = number

print(email, messages)
