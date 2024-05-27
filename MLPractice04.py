import numpy
import urllib.request
web_path=urllib.request.urlopen("https://goo.gl/QnHW4g")
dataset = numpy.genfromtxt(web_path, delimiter=",")
print("Shape of Data from Url: ", dataset.shape)
print("format of data dim = ", dataset.ndim)

print(dataset)
print("\n\n\n")
for line in dataset:
    print(line)