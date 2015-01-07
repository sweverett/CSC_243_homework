# CSC 243-501
# Assignment 1
# Spencer Everett

# List your collaborator(s) here (no more than two other people)
# Include a comment that provides significant details about each
# person's contribution to the assignment

# If you did not collaborate with anyone, place a comment in the
# file indicating that

# Files without this information will earn a 0

# Include doc strings for full credit

# Question 1
def computePay():
    '''
    Description
    '''

    hours = int(input('Enter the hours worked: '))
    rate = float(input('Enter the pay rate per hour: '))
    pay = hours*rate

    print('You earned $' + str(pay))

    return pay

# Question 2
def createStr(s, c):
    pass

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
    '''
    Description
    '''

    sum = 0

    for i in range(len(lst)):

        sum += len(lst[i])

    print(sum)

# Question 5
def printChar(lst, index):
    pass

