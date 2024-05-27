import csv
import random
import math
import operator

def loaddataset(filepath, split, trainingset=[], testset=[]):
    file = open(filepath,'r')
    csvfile  = csv.reader(file)
    dataset = list(csvfile)

    for x in range(1,len(dataset)):
        for y in range(5):
            dataset[x][y] = float(dataset[x][y])
        if random.random() < split:
            trainingset.append(dataset[x])
        else:
            testset.append(dataset[x])

def euclideandistance(instance1,instance2,length):

    dist=0
    for i in range(1,length):

        dist+=pow((instance1[i]-instance2[i]),2)
        return math.sqrt(dist)

def getNeighbours(testinstance, trainingset, k):

    Distances=[]
    length = len(testinstance)-1
    for x in range(len(trainingset)):
        dist  = euclideandistance(trainingset[x],testinstance,length)
        Distances.append([trainingset[x],dist])

    Distances.sort(key = operator.itemgetter(1))
    neighbours=[]
    for x in range(k):
        neighbours.append(Distances[x][0])

    return neighbours

def getResponse(neighbours):

    classvotes={}

    for i in range(len(neighbours)):
        predictions = neighbours[i][-1]
        if predictions in classvotes:
            classvotes[predictions]+=1
        else:
            classvotes[predictions]=1

    Classvotessorted = sorted(classvotes.items(),key = operator.itemgetter(1), reverse = True)

    return Classvotessorted[0][0]

def getaccuracy(testset, predictionset):

    correct=0
    for x in range(len(testset)):
        if testset[x][-1] == predictionset[x]:
            correct+=1

    return correct/len(testset)*100

def main():

    trainingset=[]
    testset=[]
    split=0.67
    filepath='iris.csv'
    neighbours=[]
    k=3
    Predictionset=[]
    loaddataset(filepath,split,trainingset,testset)

    for i in range(len(testset)):
        neighbours = getNeighbours(testset[i], trainingset, k)
        predictions = getResponse(neighbours)
        Predictionset.append(predictions)
    accuracy = getaccuracy(testset,Predictionset)

    print("accuracy is ", accuracy)
    print("neighbours are", neighbours)
    print("predictions are", Predictionset)

main()










