# String Reconstruction
- Written in Python and uses a Dynamic Programming approach to reduce the number of operations performed.

## Usage:
- python reconstruct.py dictionaryFile textFileWithSpacesRemoved marginWidth

## About:
- Program takes as input a text file that has had the spaces removed along with a dictionary file with a list of acceptable words. 
- A third input is an integer restricting the maximum number of characters per line and outputs the text with spaces added.
- The program will perform this by using a dynamic programming approach along with the goal of minimizing the cost of outputting the paragraph.
- The cost to output any line other than the last line of the paragraph is the cube of the number of extra spaces at the end of the line (margin - total characters).
- After each paragraph, the program will then output the total cost.

## Implementation:
- All of the words in the dictionary file are parsed and inserted into a python dictionary data type.
- The margin width provided is checked against the longest word in the dictionary.
- A 2D list is used to keep track if a substring is contained in the dictionary or is a concatenation of words in the dictionary thus preventing duplicated work.
- This 2D list is filled out in the 'parse' method which then returns the indices of the string which are the breakpoints (locations where one word ends and another begins).
- Using these breakpoints, spaces are inserted into the string where words boundaries exists.
- NewLines are then inserted into the string based off the margin width.
- The 'breakLines' method takes care to not insert a NewLine in the middle of a word.
- Lastly, the 'insertNewLines' method runs the 'breakLines' method multiple times with adjustments done on the margin width (down to the length of the longest word) in order to calculate formatting that will result in the minimum cost to print.

## Results:
- A sample dictionary file and text file is located in the Examples directory along with a few sample outputs with differing margin widths.
