l = [54, 80, 1, 10, 106]
print(l)
print("minimum element in a list is ", min(l))
print("maximum element in a list is ", max(l))
print("length=", len(l))
sum = 0
for i in range(0, len(l)):
    sum += l[i]
print("sum of all ements of list=", sum)
print("average element in a list is ", sum / len(l))