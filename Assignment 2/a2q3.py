def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


num = int(input("how many numbers"))
if num <= 0:
    print("please enter the right number")
else:
    for i in range(num):
        print(fibonacci(i))