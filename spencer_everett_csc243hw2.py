# CSC 243-501
# Assignment 2 template
# Spencer Everett

# I worked on this homework independently.

# Question 1
def maxlen(s):
    '''
    Takes an inputted string 's' and finds the largest word
    after punctuation is removed.
    '''

    punc = [',','.',';',':','!','?']
    str_len = []

    for i in punc:
        
        s = s.replace(i,'')

    s = s.split(' ')

    for n in range(len(s)):

        str_len.append(len(s[n]))

    return max(str_len)
    
# Question 2
def customSpam(name, amount, address):
    '''
    Prints a personalized sam message with the inputted name,
    amount, and email address.
    '''
    print(name)
    name = ((name.title()).split())
    print(name)
    name = name[0]+' '+name[1]
    print(name)

##    amount = amount.split()

    for n in range(len(amount)):

        if amount[n] != ' ':

            amount.insert(n+1,' ')

    print(amount)

    #amount = (amount.upper()).split()
    #amount = (amount.split()).upper()
    print(amount,sep = ' ')
    
    print('Dear ',name,',\n'
          'We would like to let you know about a great opportunity.\n'
          'You can make ',amount,' dollars in just a few short weeks!\n'
          'This is a limited-time offer.\n'
          'Please contact us at ',address,' for more information',sep = '')
    

# Question 3
def countWords(file, num):
    '''
    Takes an inputted file, removes punctuation, and then finds the numer of
    occurences of words with 'num' characters. Returns 0 for num<0.
    '''

    if num >= 0:

        inf = open(file,'r')
        contents = inf.read()
        inf.close()

        punc = [',','.',';',':','!','?']
        count = 0

        for i in punc:
                
            contents = contents.replace(i,'')

        contents = contents.replace('\n',' ')
        contents = contents.split(' ')

        for n in contents:

            if len(n) == num:

                count += 1

        return count

    else:

        return 0

# Question 4
def distribution(fname):
    '''
    Description
    '''

    inf = open(fname,'r')
    contents = inf.read()
    inf.close()

    contents = contents.split()
    print(contents)
    grades = ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F']






    
