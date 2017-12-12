from html.conf import *
from html.hook import *
from html.view import *

from server.core import *
from html.core.route import *


class app(Singleton):
    def __int__(self):
        self.__conf = conf()
        self.__route = route()
        self.__hook = hook()
        self.__view = view()
    def run(self,requestObj):
        pass