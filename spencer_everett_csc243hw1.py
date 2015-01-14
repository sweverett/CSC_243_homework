# CSC 243-501
# Assignment 1
# Spencer Everett
# 1/13/15

# I worked independently on this homework

# Question 1
def computePay():
    '''
    With the hours and pay rate given as inputs, this returns the amount
    of money recieved.
    '''

    hours = int(input('Enter the hours worked: '))
    rate = float(input('Enter the pay rate per hour: '))
    pay = hours*rate

    return pay

# Question 2
def createStr(s, c):
    '''
    Returns the string 'c' times the number of its occurences in string 's'.
    Returns an empty string if none are present.
    '''

    return s.count(c)*c

# Question 3
def sequences():
    '''
    This function prints three sequences with each on a separate line.
    The sequences are formed with the range function, using a starting
    and ending number along with the change between each elements.
    '''
    
    for i in range(17,33,2):
        print(i, end = " ")
    print()

    for i in range(10,55,5):
        print(i, end = " ")
    print()

    for i in range(18,-3,-3):
        print(i, end = " ")
    print()

# Question 4
def sumLength(lst):
    '''Finds the sum of characters in all elements of the inputted list.'''

    sum = 0

    for i in range(len(lst)):

        sum += len(lst[i])

    return sum

# Question 5
def printChar(lst, index):
    '''
    For each element of 'lst', prints the character at 'index'
    '''

    for i in range(len(lst)):
        print(lst[i][index])
