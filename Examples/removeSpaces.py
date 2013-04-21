#Michael Robertson
#mirob2005@gmail.com
#Completed: 4/20/2013

# Program removes the spaces from a text file

import sys
import re

fin = open(sys.argv[1],'r').read()

text = re.sub(' ','',fin)

open(sys.argv[1].replace('original.txt','in.txt'),'w').write(text)