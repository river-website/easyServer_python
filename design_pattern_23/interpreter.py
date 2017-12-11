class abstractExpression(object):
    def interpret(self,context):
        pass
class add(abstractExpression):
    def interpret(self,context):
        context.out += 1
class equ(abstractExpression):
    def interpret(self,context):
        context.out = (int)(context.str.split("=")[1])
class pri(abstractExpression):
    def interpret(self,context):
        print(context.out)
class all(abstractExpression):
    exp = {}
    exp['+'] = add()
    exp['='] = equ()
    exp['p'] = pri()
    def interpret(self,context):
        ls = context.str.split(";")
        for s in ls:
            context.str = s
            if '+' in s:
                self.exp['+'].interpret(context)
            elif '=' in s:
                self.exp['='].interpret(context)
            else:
                self.exp['p'].interpret(context)
class context(object):
    out = 0
    def __init__(self,str):
        self.str = str
a = all()
a.interpret(context("i=4;i++;i++;i++;print i;"))
