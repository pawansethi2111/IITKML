import csv
import os
import random
'''
F = open("C:\\Users\\Pawan Sethi\\PycharmProjects\\IITKMLProject\\email_small\\emails.csv","r")
cr = csv.reader(F)
F1 = open("C:\\Users\\Pawan Sethi\\PycharmProjects\\IITKMLProject\\email_small\\testing\\testing.csv","w")
cw1 = csv.writer(F1)
F2 = open("C:\\Users\\Pawan Sethi\\PycharmProjects\\IITKMLProject\\email_small\\training\\training.csv","w")
cw2 = csv.writer(F2)
L1 = []
L2 = []
for i in cr:
    if random.random() < 0.65:
        L1.append(i)
    else:
        L2.append(i)
cw2.writerows(L1)
cw1.writerows(L2)
F.close()
F1.close()
F2.close()

F1 = open("C:\\Users\\Pawan Sethi\\PycharmProjects\\IITKMLProject\\email_small\\testing\\testing.csv", "r")
F2 = open("C:\\Users\\Pawan Sethi\\PycharmProjects\\IITKMLProject\\email_small\\testing\\testing1.csv", "w")
S = F1.readlines()
for l in S:
    if len(l) > 1:
        F2.write(l)
F1.close()
F2.close()
os.remove("C:\\Users\\Pawan Sethi\\PycharmProjects\\IITKMLProject\\email_small\\testing\\testing.csv")
os.rename("C:\\Users\\Pawan Sethi\\PycharmProjects\\IITKMLProject\\email_small\\testing\\testing1.csv",
          "C:\\Users\\Pawan Sethi\\PycharmProjects\\IITKMLProject\\email_small\\testing\\testing.csv")


F1 = open("C:\\Users\\Pawan Sethi\\PycharmProjects\\IITKMLProject\\email_small\\training\\training.csv","r")
F2 = open("C:\\Users\\Pawan Sethi\\PycharmProjects\\IITKMLProject\\email_small\\training\\training1.csv","w")
S = F1.readlines()
for l in S:
    if len(l) > 1:

        F2.write(l)
F1.close()
F2.close()
os.remove("C:\\Users\\Pawan Sethi\\PycharmProjects\\IITKMLProject\\email_small\\training\\training.csv")
os.rename("C:\\Users\\Pawan Sethi\\PycharmProjects\\IITKMLProject\\email_small\\training\\training1.csv","C:\\Users\\Pawan Sethi\\PycharmProjects\\IITKMLProject\\email_small\\training\\training.csv")
'''
F1 = open("C:\\Users\\Pawan Sethi\\PycharmProjects\\IITKMLProject\\email_small\\training\\training.csv","r")
F2 = open("C:\\Users\\Pawan Sethi\\PycharmProjects\\IITKMLProject\\email_small\\training\\spam\\spam.csv","w")
F3 = open("C:\\Users\\Pawan Sethi\\PycharmProjects\\IITKMLProject\\email_small\\training\\ham\\ham.csv","w")

S = F1.readlines()
for l in S:
    if l[-2].isdigit():
        if int(l[-2]) == 1:
            F2.write(l)
        elif int(l[-2]) == 0:
            F3.write(l)
F1.close()
