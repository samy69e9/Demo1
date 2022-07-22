#protected (_variablename)
'''can be used in child classonly'''

class A:
    def __init__(self):
        self._a=14
class B(A):
    def __init__(self):
        A.__init__(self)
        print(self._a)


#private variable, can only be used inside class

class A:
    __a=10 #private var
def __sum(self):
    print(self.__a)

def display(self):
    print('A')
    ob=A()
    ob.__sum()
ob=A()

