def nested_dictionary(l1, l2, l3):
        result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
        return result

l1=['S001', 'S002', 'S003', 'S004']
l2=['Adina Park',"Leyton Mars","Duncan Boyl","Saim Richard"]
l3=[85, 98, 89, 92]

print(nested_dictionary(l1,l2,l3))