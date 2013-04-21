#Michael Robertson
#mirob2005@gmail.com
#Completed: 4/20/2013

# Program parses a text file and outputs a 'dictionary' file
# Prints each unique word, one per line to be used be reconstruct.py

import sys

fin = open(sys.argv[1],'r').read()

uniqueWords = set(fin.lower().split())

fout = open(sys.argv[1].replace('original.txt','dict.txt'),'w')
for word in uniqueWords:
    fout.write(word+'\r\n')