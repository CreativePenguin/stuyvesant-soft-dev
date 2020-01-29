import csv

readfile = open('utl/logins.csv','r').readlines()
writefile = open('utl/logins.csv','a+')

def __csvToDict(csv, dic={}):
    """Converts csv file into dictionary using recursion"""
    if csv:
        # arr = list. arr[0] = occupation. arr[1] = percentage
        arr = csv.pop(0).rstrip('\n').rsplit(',', 1)
        # transform array indexes to key and value in dictionary
        dic[arr[0]] = arr[1]
        return __csvToDict(csv, dic)
    return dic

def getDict():
    """returns dictionary containing all the usernames and passwords"""
    return __csvToDict(readfile)

def addUser(usr, pwd):
    """Adds a new user"""
    writefile.write(str(usr) + ',' + str(pwd) + '\n')  # Just adds another line to the file
