class CC:
    def setXY(self, x, y):
        self.x = x
        self.y = y
    def printXY(self):
        print(self.x, self.y)

dd = CC()
dd.setXY(4, 5)

# del CC
ee = CC()
dd.printXY()