import csv
import operator

F = open("iris.csv","r")
cr = csv.reader(F)
for r in cr:
    print(r)
#print("cr = ",cr)
#print("list(cr) = ",list(cr))
'''
data = list(cr)
print(data)
for x in range(1,len(data)):
    for y in range(5):
        data[x][y] = float(data[x][y])
    print(data[x])'''
#for r in cr:
#    print(r)
F.close()
D = {'A':1,'B':2}
print(D.items())
s = sorted(D.items(),key=operator.itemgetter(1), reverse=True)
print(s)
print(s[0][0])