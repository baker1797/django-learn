myList = [1,2,3]

def firstFunction(myList, age = 12):
    "First Function Testing"
    print "first function"
    print myList
    myList.append([4,5,6]);
    print myList
    myList = [7,8,9]
    print myList
    print age
    return

def defaultValFunction():
    firstFunction(myList) #uses default value
    firstFunction(myList, 32)
    print myList

def anonFunction():
    sumAnon = lambda var1, var2: var1 + var2
    print sumAnon(2,8)

def dirList():
    import novemberSite
    print dir(novemberSite)