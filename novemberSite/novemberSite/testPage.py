#Module Setup
import time
import calendar

import testFunctions
import playerPos

miami1 = playerPos.PointGuard("Mario Chalmers", 40)
miami2 = playerPos.PointGuard("Norris Cole", 60)

miami1.printObj()
print miami1.abbrev


#playerPos.SmallForward.printObj()

#Variable Setup
x = 3
y = 3
strVar = "My String"
listVar = [1,2,3,"Four","Five","Six"]
dictVar = {'key1': '1', 'keyTwo': 2, 'third': 'Three'}


print time.asctime(time.localtime(time.time()))
print calendar.month(2013,10)

#Printing Number variables
print "\n==Printing Numbers=="
if (x == 3 and 3 != 5 and x in listVar and x is y):
	print "good"
else:
	print "bad"

#Printing String variables
print "\n==Printing Strings=="

print "string:\t\t" + strVar
print "string [4]:\t" + strVar[4]
print "string [3:]:\t" + strVar[3:]
print "string [3:6]:\t" + strVar[3:6]

#Printing List variables
print "\n==Printing Lists=="

print listVar
print listVar[:4]
print listVar[2:3]

#Printing Dictionary variables
print "\n==Printing Dictionary=="

print dictVar['keyTwo']
print dictVar.keys()
print dictVar.values()
print str(dictVar)
print dictVar.items()

#Printing imported Function
print "\n==Printing Function=="

def importTestFunction():
    print "success"
    
testFunctions.firstFunction([1,2,3])

