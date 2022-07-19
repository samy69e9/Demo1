# #q10(Doubt)
str=input("Enter string\n")
if(len(str)<2):
    print("invalid string")
elif(len(str)==2):
    t=str[0]
    str[0]=str[1]
    str[1]=t
    print(str)
else:
    print(str[-1]+ str[1:-1]+ str[0])