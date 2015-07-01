from abc import ABCMeta, abstractmethod

class Mediator(object):
    @abstractmethod
    def create_colleagues(self):
        pass
    @abstractmethod
    def colleague_changed(self):
        pass
