# CSC 243-501
# Assignment 3
# Spencer Everett

# I worked on this homework independently

# Question 1
def crypto(fname, word):
    '''
    Searches the file 'fname' for all occurences of the string
    'word' and replaces the characters of 'word' with 'x's.
    '''
    
    inf = open(fname,'r')
    contents = inf.read()
    inf.close()

    print(contents.replace(word,'x'*len(word)))

# Question 2
def printPositive(fname):
    '''
    Converts numbers from 'fname' to appropriate data types and prints
    them, one line for each.
    '''

    inf = open(fname,'r')
    contents = inf.readlines()
    inf.close()

    posNums = []

    for n in contents:

        if eval(n.strip()) > 0:

            posNums.append(n)

    print(''.join(posNums).strip())
    # Note: I realize we haven't discussed .join() in class yet. However I found
    # it while searching through help(str) and it was too good to pass up! I could
    # have used a for loop instead to concatenate the list into a string.

# Question 3
def payroll(infname, outfname):
    '''
    Opens inputted file, calculates payroll from listed hours and pay rates, and
    writes the values to an output file.
    '''
    inf  = open(infname,'r')
    contents = inf.read().split()
    inf.close()

    outfname = open(outfname,'w')

    for n in range(0,len(contents)-1,2):
        
        outfname.write(str(eval(contents[n])*eval(contents[n+1]))+'\n')

    outfname.close()

# Question 4
def printNTimes(lst, n):
    '''
    Takes an inputted list 'lst' and prints all values of the list in which
    the value divided by the previous value is 'n'.
    '''

    for i in range(1,len(lst)):

        if lst[i]/lst[i-1] == n:

            print(str(lst[i]))

# Question 5
def constantDiff(lst, num):
    '''
    If all string elements of 'lst' have an equal difference in encoding value
    equal to 'num', the function returns true. Otherwise returns false.
    '''

    diff = []

    for i in range(1,len(lst)):

        diff.append(abs(ord(lst[i])-ord(lst[i-1])))

    if diff.count(num) == len(diff) and len(diff) != 0:

        return True

    else:

        return False 
