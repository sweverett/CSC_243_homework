# CSC 243-501
# Assignment 5
# Spencer Everett

# I worked independently on this assignment

from random import *
from math import *

# Question 1
def findMinRow(lst):
    '''
    Returns the index of the sublist from 'lst' that contains the
    smallest sum.
    '''

    min_ind = -1

    try:

        for i in range(0,len(lst)):

            if sum(lst[i]) <= sum(lst[min_ind]):

                min_ind = i

        return min_ind

    except TypeError:

        return -1

# Question 2
def table(fname, n):
    '''
    If 'fname' exists, the numbers in 'fname' are re-organized into
    a two dimensional nxn list. 
    '''

    try:

        inf = open(fname,'r')
        contents = inf.read().split()
        inf.close()

        size = int(sqrt(len(contents)))
        table = []

        for i in range(0,n):

            table.append([])
            # Wasn't sure if this would work, but it seems to and is easier than
            # combining multiple lists

            for j in range(0,n):

                table[i].append(contents[n*i+j])

        return table

    except FileNotFoundError:

        return []

# Question 3
# Header is written for the changes needed for part (b)
def craps(loud=True):
    '''
    Simulates a game of craps, printing out each roll and returning '1' for
    a win and '0' for a loss.
    '''

    first_roll = [randrange(1,7), randrange(1,7)]

    if loud:

        print('Roll:',first_roll[0],'and',first_roll[1],'=',str(sum(first_roll)))

    if sum(first_roll) == 7 or sum(first_roll) == 11:

        return 1

    elif sum(first_roll) == 2 or sum(first_roll) == 3 or sum(first_roll) == 12:

        return 0

    else:

        while True:

            roll = [randrange(1,7), randrange(1,7)]

            if loud:

                print('Roll: ',roll[0],' and ',roll[1],' = ',str(sum(roll)))

            if sum(roll) == sum(first_roll):

                return 1

            elif sum(roll) == 7:

                return 0


def quietCraps():
    '''
    Simulates a game of craps by calling craps(), but only returning the result.    
    '''

    result = craps(False)

    return result
    
def testCraps(n):
    '''
    Calls the function quietCraps() 'n' times and returns the winning percentage.
    '''

    results = []
    
    for i in range(0,n):

        results.append(quietCraps())

    return sum(results)/len(results)
