#Michael Robertson
#mirob2005@gmail.com
#Completed: 4/--/2013

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
        
        self.dictionary = {}
        self.input = ''
        
        self.process()

    def process(self):
        self.checkInputs()
        self.readDict()
        self.readinFile()

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

    def readDict(self):
        with open(self.dictFile,'r') as dictionary:
            for line in dictionary:
                self.dictionary[line.strip().lower()] = None
    
    def readinFile(self):
        with open(self.inFile,'r') as inputText:
            for line in inputText:
                self.parse(line)
                
    def parse(self,line):
        n = len(line)
        
        s = line.lower()
        
        D = [[False for x in range(0,n)] for x in range(0,n)]
       
        for d in range(0,n):
            for i in range(0,n-d):
                j = i+d+1
                if s[i:j] in self.dictionary:
                    D[i][j-1] = line[i:j]
                else:
                    for k in range(i+1,j-1):
                        if D[i][k-1] and D[k][j-1]:
                            D[i][j-1] = line[i:j]
    
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python reconstruct.py dictFile inFile margin')
        exit()

    reconstruct(sys.argv[1:])