# CSC 243-501
# Assignment 4
# Spencer Everett

# I worked independently on this assignment

# Question 1
def statement(accountlst):
    '''
    Takes a list of floats 'accountlst' and returns a list of the sum of
    positive numbers (deposits) and negative numbers (withdrawals).
    '''
    
    deposits = []
    withdrawals = []

    for n in accountlst:

        if n > 0:

            deposits.append(n)

        else:

            withdrawals.append(n)

    return [sum(deposits),sum(withdrawals)]

# Question 2
def findIndices(s1, s2):
    '''
    Finds all indices of list 's1' in which an element of list 's2' is
    present.
    '''

    indices = []

    for i in range(len(s1)):

        if s1[i] in s2:

            indices.append(i)

    return indices

# Question 3
def pairSum(lst, n):
    '''
    Prints the indices of any pair of two elements in 'lst' whose sum is
    equal to 'n'.
    '''

    pairs = ''

    for j in range(len(lst)):

        for k in range(j,len(lst)):

            if lst[j]+lst[k] == n:

                print(j,k)

# Question 4
def encrypt(key, number):
    '''
    Returns the encryption of string 'number' using the encryption key 'key'.
    '''

    encryption = ''

    for n in number:

        encryption += key[eval(n)]

    return encryption

# Question 5
def oddrow(lst):
    '''
    Description
    '''
    pass
