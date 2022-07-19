def remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples
tuples=[(),(),('a','b'),('a','b','c'),(','),("d")]
print("before: ",tuples)
print("after: ",(remove(tuples)))