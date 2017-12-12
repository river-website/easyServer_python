class earthSingleton(object):
    __earth = None
    name = ''
    def __new__(cls, *args, **kwargs):
        if not cls.__earth:
            cls.__earth = object.__new__(cls,*args,**kwargs)
        return cls.__earth
earth1 = earthSingleton()
earth1.name = 'earth1'
earth2 = earthSingleton()
print(earth2.name)