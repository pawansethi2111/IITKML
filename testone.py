import math
def mean(number):
    return sum(number)/float(len(number))
def stdev(number):
    avg = mean(number)
    A = [pow(x-avg,2) for x in number]
    variance = sum(A)/ float(len(A)-1)
    return math.sqrt(variance)

def summarize(dataset):
    summaries = [(mean(attribute),stdev(attribute)) for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries


def separateByClass(dataset):
    separated = {}

    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] is not separated):
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated
def summarizeByClass(dataset):
    separated = separateByClass(dataset)
    summaries = {}

    for (classValue, instances) in separated.iteritems():
        summaries[classValue] = summarize(instances)
    return summaries
number1 = [10,20,30,40,1201]
number2 = [15,27,45,75,2301]
dataset = [number1,number2]
s = summarize(dataset)
print(s)
#cl = summarizeByClass(dataset)
#print(cl)