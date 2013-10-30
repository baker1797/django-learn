class PointGuard:
    "Point guard class"
    abbrev = "PG"
    positionCount = 0
    
    #def __init__(self, n = "New Player", v = 0):
    def __init__(self, name, value):
        self.name = name
        self.position = "PG"
        self.value = value
        self.__salary = 10000           #hidden to public, visible using miami1._PointGuard__salary
        PointGuard.positionCount += 1
        
    def __str__(self):
        return "Pos | Val | Name\n %s | %d | %s" \
        %(self.position, self.value, self.name)
        
    def setName(self, name):
        self.name = name
        
def shootBall():
    print "shoot the ball"