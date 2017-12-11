class product(object):
    part1 = None
    part2 = None
    def name(self):
        print(self.part1+self.part2)
class builder(object):
    _product = product()
    def part1(self):
        pass
    def part2(self):
        pass
    def getProduct(self):
        return self._product
class Abuilder(builder):
    def part1(self):
        self._product.part1 = 'A1'
    def part2(self):
        self._product.part2 = 'A2'
class Bbuilder(builder):
    def part1(self):
        self._product.part1= 'B1'
    def part2(self):
        self._product.part2 = 'B2'

class director(object):
    def __init__(self,builder):
        builder.part1()
        builder.part2()

ba = Abuilder()
bb = Bbuilder()
d=director(ba)
ba.getProduct().name()
d=director(bb)
bb.getProduct().name()