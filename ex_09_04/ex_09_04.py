"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest 
number of mail messages. The program looks for 'From ' lines and takes the second word of those 
lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's 
mail address to a count of the number of times they appear in the file. After the dictionary is 
produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print(f'Error, the file {fname} does not exist in the current directory.')
    quit()

emailsSent = {}

for line in fh:
    if not line.startswith('From') or line.startswith('From:'):
        continue
    pieces = line.split()

    emailsSent[pieces[1]] = emailsSent.get(pieces[1], 0) + 1

mostEmailsSent = ''
mostEmailsSentCount = 0

for email, count in emailsSent.items():
    if count > mostEmailsSentCount:
        mostEmailsSent = email
        mostEmailsSentCount = count
        
print(mostEmailsSent, mostEmailsSentCount)