sum = 0
num = int(input("enter the number to check whether it is armstrong or not"))
print(num)
order = len(str(num))
original_num = num
while num > 0:
    digit = num % 10
    sum = sum + digit ** order
    num = num // 10
if sum == original_num:
    print("number is armstrong number")
else:
    print("number is not armstrong number")