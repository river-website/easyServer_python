# 一个工厂多个关联产品

class animalProduct(object):
    def name(self):
        pass
class catConcreteProduct(animalProduct):
    def name(self):
        print("this is a cat!")
class dogConcreteProduct(animalProduct):
    def name(self):
        print("this is a dog")
class foodProcduct(object):
    def getFood(self):
        pass
class dogFood(foodProcduct):
    def getFood(self):
        print("this is dog food")
class catFood(foodProcduct):
    def getFood(self):
        print("this is cat food")

class creator(object):
    def getProduct(self):
        pass
    def getFood(self):
        pass
class catConcrete(creator):
    def getProduct(self):
        return catConcreteProduct()
    def getFood(self):
        return catFood()
class dogConcrete(creator):
    def getProduct(self):
        return dogConcreteProduct()
    def getFood(self):
        return dogFood()
factory = dogConcrete()
product = factory.getProduct()
product.name()
food = factory.getFood()
food.getFood()