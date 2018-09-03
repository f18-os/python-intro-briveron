
import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program

# set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

textFname = sys.argv[1]
outputFname = sys.argv[2]

open(outputFname, 'w').close()


import string
frequency = {}
document_text = open(textFname, 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{1,20}\b', text_string)

for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

frequency_list=sorted(frequency_list)

for words in frequency_list:
    f = open(outputFname , "a")
    f.write( words)
    f.write(" ")
    f.write(str(frequency[words]))
    f.write("\n")

    #print (words, frequency[words])
