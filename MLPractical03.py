#load csv using numpy

import numpy
filename = open("C:/PycharmProjects/p3/packageML2/indians-diabetes.data.csv")

data = numpy.loadtxt(filename, delimiter=",")

filename.close()

print("Numpy loadtxt Size= ", data.shape)

print("Data :\n", data)