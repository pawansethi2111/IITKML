import csv
import math
import random
import operator

def loadDataset(filepath,split,trainingset=[],testset=[]):
    csvfile = open(filepath, 'r')
    lines = csv.reader(csvfile)
    dataset = list(lines)
    for x in range(1,len(dataset)):
        #exclude id which is column 1
        for y in range(5):
            dataset[x][y] = float(dataset[x][y])
        if random.random() < split:
            trainingset.append(dataset[x])
        else:
            testset.append(dataset[x])

def euclideandistance(instance1,instance2,length):

    sum=0
    for i in len(length):
        sum += pow(instance1[i]-instance2[i], 2)
    return math.sqrt(sum)

def getneighbours(trainingset, testinstance,k):
    dist=0
    distances=[]
    length = len(testinstance)-1
    for i in range(len(trainingset)):
        dist = euclideandistance(trainingset[i], testinstance, length)
        distances.append(trainingset[i],dist)

    distances.sort(key = operator.itemgetter(1))

    neighbours=[]
    for i in range(k):
        neighbours.append(distances[i][0])

    return neighbours

def getresponse(neighbours):

    classvotes={}

    for x in range(len(neighbours)):
        response = neighbours[x][-1]
    if response in classvotes:
        classvotes[response]+=1
    else:
        classvotes[response] = 1

    classvotessorted  = sorted(classvotes.items(),key = operator.itemgetter(1), reverse = True)
    return classvotessorted

def getaccuracy(testset, predictions):

    correct=0
    for i in range(len(testset)):
        if(testset[i][-1] == predictions[i]:
            correct+=1
    return accuracy *100

def main():
    testset =[]
    trainingset=[]











