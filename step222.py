class M222:
    def __init__ (self):
        self._222Var = 0

obj = M222()
obj._222Var = 43
print(obj._222Var)

class Fun:
    def __init__ (self):
        self.__Avar = 21
    def getLow(self):
        print(self.__Avar)
    def setLow(self, private):
        self.__Avar = private

obj = Fun()
obj.getLow()
obj.setLow(15)
obj.getLow()
