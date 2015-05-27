# -*- coding: utf-8 -*-

class Banner(object):
    __string = ''

    def __init__(self, string):
        self.__string = string

    def showWithParen(self):
        print('(' + self.__string + ')')

    def showWithAster(self):
        print('*' + self.__string + '*')
