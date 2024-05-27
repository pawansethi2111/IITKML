#dictionary
#_____________

d={'A': 'Java' , 'B':'J2EE' , 'C':'Android', 'D':'Python', 'E':'Hadoop', 'Key':'Value'}
print("dictionary= ",d )
d['F']='Japan'
print("dictionary = ",d  )

d['B']='INDIA'
print("dictionary =",d)

del d['E']
print(" dictionary = ",d)

print("dictionary =",d)

print(dir())
#dictionary doesnt support 'positional access' / indexing

print(d['A'])
print(d['B'])
#print(d['0'])#error
#print(d[0])

res = d.get('Z',"Value not present")
print("result= ",res)