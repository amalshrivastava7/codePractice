class FractionClass:
    def __init__(self, top, bottom):

        self.numerator  = top
        self.denominator = bottom

    def calculateratio(self):
        return (self.numerator/self.denominator)


newobj = FractionClass(10, 5)

print(newobj.calculateratio())