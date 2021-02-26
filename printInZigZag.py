'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

P   A   H   N
A P L S I I G
Y   I   R

Write the code that will take a string and make this conversion given a number of rows:

'''

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows < 2:
        print(s + "\n")
        return;
    
    strArray = []
    cycle = cycleLoop = 2*numRows - 2
    space = spaceLoop = numRows - 2
    
    for row in range(numRows):
        i = row
        
        if row==0 or row==numRows-1:
            cycleTempA = cycleTempB = cycle
            tempA = tempB = space
        else:
            tempA = spaceLoop
            tempB = space - spaceLoop - 1
            cycleTempA = cycleLoop
            cycleTempB = cycle - cycleLoop
            
        while(i<len(s)):
            strArray.append(s[i] + tempA*" ") ## change after
            i += cycleTempA
            
            cycleTempA, cycleTempB = cycleTempB, cycleTempA
            tempA, tempB = tempB, tempA
            
        strArray.append("\n")
        spaceLoop -= 1
        cycleLoop -= 2
        
    print("".join(strArray))
    return;
    
convert("PAYPALISHIRING", 3)
convert("abcdefghijklmnopqrstuvwxyz", 1)
convert("abcdefghijklmnopqrstuvwxyz", 2)
convert("abcdefghijklmnopqrstuvwxyz", 4)
convert("abcdefghijklmnopqrstuvwxyz", 5)
        