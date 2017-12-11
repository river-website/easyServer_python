# 一个工厂一个产品

class animalProduct(object):
    def name(self):
        pass
class catConcreteProduct(animalProduct):
    def name(self):
        print("this is a cat!")
class dogConcreteProduct(animalProduct):
    def name(self):
        print("this is a dog")
class creator(object):
    def getProduct(self):
        pass
class catConcrete(creator):
    def getProduct(self):
        return catConcreteProduct()
class dogConcrete(creator):
    def getProduct(self):
        return dogConcreteProduct()
factory = dogConcrete()
product = factory.getProduct()
product.name()