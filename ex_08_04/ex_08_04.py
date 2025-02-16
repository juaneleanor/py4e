"""
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list 
of words using the split() method. The program should build a list of words. For each word on each 
line check to see if the word is already in the list and if not append it to the list. When the 
program completes, sort and print the resulting words in python sort() order as shown in the desired output.
"""

fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print(f'Error, the file {fname} does not exist.')
    quit()

lst = []

for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)

lst.sort()
print(lst)