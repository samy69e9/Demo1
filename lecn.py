#q1
l1=['m','n']
n=3
res=[]

for i in range(len(l1)):
    for j in range(n):
        item=l1[i]+str(j+1)
        res.append(item)

print(res)

#Q2
l=[[4,5,3],[6,3,2],[6,9,1]]
sum_l=[]
for i in l:
    sum=0
    for j in i:
        sum=sum+j
    sum_l.append([sum])

print((sum_l))

#q3
l=[1,2,3,0,1,1,4,5,2,3]

print(list(set(l)))

#q4
for i in range(1200,3000):
    if (i%4==0 and i%8==0 and i%6!=0):
        print((i))

