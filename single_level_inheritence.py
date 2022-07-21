class name:
    a=10
    b=20
    def _init_(self,a,b):
        print('A')
    
    def f1(self):
        print("Sanyam")            

class address(name):
    a=4
    b=5
    def _init_(self):
        super()._init_(12,12)

    def f2(self):
        super().f1()
        print(self.a,self.b)
        print(super().a,super().b)

ob=address()
ob.f1()
ob.f2()