class interator(object):
    def first(self):
        pass
    def next(self):
        pass
    def cur(self):
        pass
    def isDone(self):
        pass
class asc(interator):
    __list= None
    __cur = 0
    def __init__(self,list):
        self.__list = list
    def first(self):
        return  self.__list[0]
    def next(self):
        self.__cur += 1
        return self.__list[self.__cur]
    def isDone(self):
        if self.__cur >= len(self.__list)-1:
            return True
        return False
    def cur(self):
        return self.__list[self.__cur]
class desc(interator):
    __list = None
    __cur = 0

    def __init__(self, list):
        self.__list = list

    def first(self):
        return self.__list[len(self.__list)-1]

    def next(self):
        self.__cur += 1
        return self.__list[len(self.__list)-self.__cur-1]

    def isDone(self):
        if self.__cur >= len(self.__list)-1:
            return True
        return False

    def cur(self):
        return self.__list[len(self.__list)-self.__cur]
class aggregate(object):
    list = []
    def add(self,obj):
        self.list.append(obj)
    def remove(self,obj):
        self.list.remove(obj)
    def count(self):
        return len(self.list)
    def createInter(self):
        i = desc(self.list)
        self.inter = i
    def foreach(self):
        f = self.inter.first()
        print(f)
        while(not self.inter.isDone()):
            f = self.inter.next()
            print(f)
a = aggregate()
a.createInter()
a.add("1")
a.add("2")
a.add("3")
a.foreach()