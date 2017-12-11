class flyweight(object):
    char = ''
    click = 0
    def __init__(self,char):
        self.char = char
    def draw(self):
        print(self.char)
class flyweightFactory(object):
    map = {}
    def createWeight(self,key):
        value = self.map.get(key)
        if not value:
            value = flyweight(key)
            self.map[key] = value
        return value
fact = flyweightFactory()
em = fact.createWeight("k")
em.draw()
en = fact.createWeight("t")
en.draw()
e  = fact.createWeight("k")
print(em)
print(en)
print(e)