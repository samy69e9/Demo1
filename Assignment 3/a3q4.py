#OUTPUT
# 1 15 3 4
# 42 15 3 4

a,b,x,y = 1,15,3,4
def fun(x, y):
   global a
   a = 42
   x,y = y,x
   b = 33
   b = 17
   c = 100

print (a,b,x,y)
fun(17,4)
print (a,b,x,y)