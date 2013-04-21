#Michael Robertson
#mirob2005@gmail.com
#Completed: 4/20/2013

# Program takes as input a text file that has had the spaces removed along with
#   a dictionary file with a list of acceptable words.  A third input is an integer
#   restricting the maximum number of characters per line and outputs the text
#   with spaces added.

# The program will perform this by using a dynamic programming approach along
#   with the goal of minimizing the cost of outputting the paragraph where the
#   cost to output any line other than the last line of the paragraph is the cube
#   of the number of extra spaces at the end of the line (margin - total characters).

# After each paragraph, the program will then output the total cost.

import sys
import os

class reconstruct:
    def __init__(self, inputs):
        self.dictFile, self.inFile = inputs[0:2]
        self.margin = int(inputs[2])

        self.text = []
        self.dictionary = {}
        self.longest = 0
        self.breakpoints = []
        
        self.process()

    def process(self):
        self.checkInputs()
        self.readDict()
        self.checkMargin()
        self.readinFile()
        
        newText = self.insertSpaces()
        
        print(self.insertNewLines(newText))

    def checkInputs(self):
        if not os.path.exists(self.dictFile):
            print('File %s does not exist!'%self.dictFile)
            exit()
        if not os.path.exists(self.inFile):
            print('File %s does not exist!'%self.inFile)
            exit()
        if self.margin < 1:
            print('Margin size is not acceptable!')
            exit()

    #Each line contains one word plus a '\n', strip whitesplace and lower case
    def readDict(self):
        with open(self.dictFile,'r') as dictionary:
            for line in dictionary:
                self.dictionary[line.strip().lower()] = None

    # Check to make sure our margin isn't smaller than our longest word
    def checkMargin(self):
        for key in self.dictionary.keys():
            if len(key) > self.longest:
                self.longest = len(key)
        if self.margin < self.longest:
            print('Margin size is not acceptable (Longest word is %s characters long)!'%self.longest)
            exit()
    
    def readinFile(self):
        with open(self.inFile,'r') as inputText:
            for line in inputText:
                self.text.append(line)
                self.breakpoints.append(sorted(self.parse(line)))

    # Fills out our table to keep track of what substrings have already been found and which have not
    # Breakpoints are the indices in the line where a space should be inserted to form words
    def parse(self,line):
        n = len(line)
        
        s = line.lower()
        
        D = [[False for x in range(0,n)] for x in range(0,n)]
        breakpoints = set()
       
        for d in range(0,n):
            for i in range(0,n-d):
                j = i+d+1
                if s[i:j] in self.dictionary:
                    D[i][j-1] = line[i:j]
                else:
                    for k in range(i,j):
                        if D[i][k-1] and D[k][j-1]:
                            D[i][j-1] = line[i:j]
                            breakpoints.add(k)
                            break
        # This removes extra breakpoints that are found when words are substrings of other words
        # Example: 'theyouthevent' can be broken into:
        #   'the youth event' or 'the you the ...'
        #   Without this check, we get 'the you th event'
        #   With this check, we get 'the youth event'
        start = 0
        past = 0
        for x in sorted(breakpoints):
            if not s[start:x] in self.dictionary:
                if s[past:x] in self.dictionary:
                    breakpoints.remove(start)
                    start = x
                else:
                    breakpoints.remove(x)
            else:
                past = start
                start = x
        return breakpoints

    # Insert spaces at the word boundaries using breakpoints
    def insertSpaces(self):
        text = ''
        for (paragraph,bp) in zip(self.text,self.breakpoints):
            past = 0
            for pt in bp:
                text += paragraph[past:pt] + ' '
                past = pt
            text+= paragraph[past:]
        return text
    
    # Insert newlines at the line breaks, calls breakLines() mulitple times to minimize total cost of printing.
    def insertNewLines(self,text):
        text = text.split('\n')
        final = ''
        for para in text:
            if not para:
                continue
            attempts = {}
            for reduction in range(self.margin-self.longest+1):
                newText = self.breakLines(para,reduction)
                cost = 0
                for line in newText[:-1]:
                    cost += pow(self.margin-len(line),3)
                
                attempts[cost] = newText

            cost = sorted(attempts.keys())[0]
            newText = attempts[cost]
            
            for line in newText:
                final += line + '\n'
            final += str(cost)+'\n'

        return final

    # Uses the margin + reduction (if any) to insert newlines.
    # The margin width is found, then the line is traced back until a space
    #   is found (as to not break up words)
    # Reduction ranges from 0 to (margin - longest word) so that we try
    #   different formattings. The formatting with the smallest cost is used.
    # The goal is to have all the lines except the final line be of similar lengths
    #   due to the cost growing exponentially per space on each line.
    def breakLines(self,para,reduction):
        margin = self.margin - reduction
        newText = []
        while para:
            adjustment = 0
            current = para[:margin]
            if len(current) == margin:
                if len(para) > len(current):
                    if not current.endswith(' ') and para[margin] != ' ':
                        current = para[:margin-adjustment]
                        while current and not current.endswith(' '):
                            adjustment += 1
                            current = para[:self.margin-adjustment]
            if current.strip():
                newText.append(current.strip())
            para = para[len(current):]
        return newText

    
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python reconstruct.py dictFile inFile margin')
        exit()

    reconstruct(sys.argv[1:])
