# # ...........Inheritence........
# # the process of creating a new class by using the properties of same  class.
# # EXAMPLE....

# class A:
#     def f1(self):
#         print('A')
# class B(A):
#     def f2(self):
#         print('B')
#         ob=B()
#         ob.f1()
#         ob.f2()


# # TYPES ::
# # SINGLE INHERITENCE:
# class A: #its a parent class or super class
#     def f1(self):
#         print('A')
# class B(A): #its a child class
#     def f2(self):
#         print('B')
#         ob=B()
#         ob.f1()
#         ob.f2()


# # MULTILEVEL INHERITENCE:: more thn one classes.

# class A ():
#     def f1():
#         print('A')
# class B('A'):
#     def f2(self):
#         print('B')
# class C(B):
#     def f3(self):
#         print('C')
#         ob=C() 
#         ob.f1()
#         ob.f2
#         ob.f3

      

# # MULTIPLE INHERITENCE:: same as upper


# # hierrarchical ::

# class A ():
#     def f1():
#         print('A')
# class B('A'):
#     def f2(self):
#         print('B')
# class C(B):
#     def f3(self):
#         print('C')
#         ob=c()
#         ob.f1()
#         ob.f3()
   

# #f2 wont be executed


# # HYBRID INHERITENCE:
# # multiple+herirarchal ??


# # SUPER KEYWORD:  is used to access variables of parent class in child class.

# class A():
#     a=10
#     b=20
#     def _init_(self):
#      print('A')
#     def m1(self):
#      print('m1')
# class B (A):
#     def display():


# # .................example.............

# class A():
#  def _init_(self):
#      print('A')
#  def m1(self):
#      print('m1')
# class B (A):

#     a=4
#     b=5
# def m2 (self):
#     print(self.a,self.b)
#     print(super(),super().b)
# ob=b()
# ob.m1()
# ob.m2()

# # .....example........

# class A():
#     a=10
#     b=20
#     def _init_(self)
#      print('A')
#     def m1(self):
#      print('m1')
# class B (A):

#      a=4
#      b=5
#      def m2 (self):
#       super().m1()
#       print(self.a,self.b)
#       print(super(),super().b)
#       ob=b()
#       ob.m1()
#       ob.m2()

# # .......EXample......
# class A():
#     a=10
#     b=20
#     def _init_(self):
#      print('A')
#     def m1(self):
#      print('m1')
# class B (A):

#     a=4
#     b=5

# #   def_init_(self)
# super()._init_(12,12)

# def m2 (self):

#     super().m1()
#     print(self.a,self.b)
#     print(super(),super().b)
#     ob=b()
#     ob.m1()
#     ob.m2()


# # POLYMORPHISM::

# # 1. COMPILE TIME :: OVERLOADING               2.RUN TIME :: OVERRIDING
# # OPERATOR
# # CONSTRUCTOR
# # FUNCTION

# # Python doesnt support overloading.                   Python does supports overriding.

# # ......example 1.....compile time.....

# class A():
#  def f1(self.A,B)
#   print('A')
#  def f1(self.A,B,C)


# # ..........example 2......run time......
# class A()
# a=10
# b=20
#  def _init_(self)
#      print('a')
#  def m1(self):
#      print('m1')
# class B (A):

#         a=4
#         b=5

# def m1 (self):
#     print('B class')

# ob=b()
# ob.m1()


# # MODULES::
# # just like header files in c++..we use modules in python.
# # 1.PRE DEFINED:: Eg: DATE,TIME 
# # .......EXAMPE......

# # from math import*
# # import math as m
# # import math

# # .m.sqrt()
# #  sqrt()
# # 2.USER DEFINED::