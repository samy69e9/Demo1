def AbyB(a,b):
    try:
        k = a/b
        print(k)
    except ZeroDivisionError:
        print("Can't divide by zero")
    
    finally:
        print("calculated")
AbyB(5,0)