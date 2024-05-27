'''from collections import *
A=[1,2,3,4,2,3,1,2,4,5,6,3,2,5]
s = Counter(A)
print(s)

x=()
y=[]
z={}
print(type(x))
print(type(y))
print(type(z))
'''

import re
import os
def tokens(text, tok_size=4):
    return [text[i:i + tok_size] for i in range(len(text) - tok_size + 1)]

#print(tokens("Computer"))

def clean_split(in_str):
    return re.sub(r'[^\s\w]|_', '', in_str).lower().split()
'''
s = "comPU|ter\s|ci\math-123K"
print(clean_split(s))
print("hello good you")

s = "Welcome to Delhi"
print(s.split('e'))

'''
'''
a = os.listdir("C:\\Users\\Pawan Sethi\\Downloads\\")
x = [i for i in a if len(i) < 10]
for j in x:
    print(clean_split(j))
def Hello():
    print("Hello Pawan")
'''
import pickle
import math

x = math.log10(0.44)
print("2.5 log 10 - ",x)
f1 = open("abc.dat","wb")
X = [111,222,333,444]
pickle.dump(X,f1)
f1.close()
f2 = open("abc.dat","rb")
s = pickle.load(f2)
print(s)
f2.close()