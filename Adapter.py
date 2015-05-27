from Adaptee import Banner
from Target import Print

class PrintBannerSubClass(Banner, Print):
    def __init__(self, string):
        super(PrintBannerSubClass, self).__init__(string)

    def printWeak(self):
        self.showWithParen()

    def printStrong(self):
        self.showWithAster()

class PrintBannerDelegation(Print):
    def __init__(self, string):
        self.banner = Banner(string)

    def printWeak(self):
        self.banner.showWithParen()

    def printStrong(self):
        self.banner.showWithAster()



if __name__ == '__main__':
    p = PrintBannerSubClass('Hello p')
    p.printWeak()
    p.printStrong()

    q = PrintBannerDelegation('Hello q')
    q.printWeak()
    q.printStrong()