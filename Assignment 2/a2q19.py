l, u, d, s = 0, 0, 0, 0
Password = 'Alfred@batman09'
lowercase_alphabets = 'asdfghjklpoiuytrewqzxcvbnm'
uppercase_alphabets = 'ASDFGHJKLPOIUYTREWQZXCVBNM'
digits = "0123456789"
specialchar = '!@#$%^&*'
if len(Password) >= 6:
    for i in Password:
        if i in lowercase_alphabets:
            l += 1
        if i in uppercase_alphabets:
            u += 1
        if i in digits:
            d += 1
        if i in specialchar:
            s += 1
if l >= 1 and u >= 1 and d >= 1 and s >= 1 and l+u+d+s == len(Password):
    print("Password is valid")
else:
    print("Password is  not valid")