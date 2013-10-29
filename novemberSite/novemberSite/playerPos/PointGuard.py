class PointGuard:
    "Point guard class"
    abbrev = "PG"
    
    #def __init__(self, n = "New Player", v = 0):
    def __init__(self, name, value):
        self.name = name
        self.position = "PG"
        self.value = input("Enter value: ")
        self.__salary__ = 10000
        
    def printObj(self):
        print self.value, " | ", self.position, " | ", self.name
        
    def setName(self, name):
        self.name = name