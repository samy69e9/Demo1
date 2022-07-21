class School:
    def f1(self):
        print("students names:")

class student1(School):
    def f2(self):
        print("Rajat")

class student2(School):
    def f3(self):
        print("Rahul")

class student3(student1,School):
    def f4(self):
        print("Karan")

ob=student3()
ob.f1()
ob.f2()