class name:
    def _init_(self):
        print("A")

    def f1(self):
        print("Rahul")

class address(name):
    def f1(self):
        print("Karan")

ob=address()
ob.f1()