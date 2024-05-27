import csv
import math
import random
import operator

def loaddataset(filepath, split, trainingset=[],testset=[]):
    csvfile = open(filepath,'r')
    lines = csv.reader(csvfile)
    dataset = list(lines)

    for x in range(1,len(dataset)):
        for y in range(5):
            dataset[x][y] = float(dataset[x][y])

        if random.random()<split:
            trainingset.append(dataset[x])
        else:
            testset.append(dataset[x])

def euclideandistance(instance1,instance2,length):

    dist = 0
    for i in range(length):
        dist += pow((instance1[i]-instance2[i]),2)

    return math.sqrt(dist)

def getNeighbours(trainingSet, testinstance, k):

    dist=0
    Distances = []
    length = len(testinstance)-1
    for x in range(len(trainingSet)):
        dist = euclideandistance(trainingSet[x], testinstance, length)
        Distances.append([trainingSet[x], dist])

    neighbours=[]
    for i in range(k):
        neighbours.append(Distances[i][0])

    return neighbours

def getResponse(neighbours):

    classvotes = {}

    for i in range(len(neighbours)):
        predictions = neighbours[i][-1]

        if predictions in classvotes:
            classvotes[predictions]+=1
        else:
            classvotes[predictions]=1
    classvotessorted =[]
    classvotessorted = sorted(classvotes.items(), key = operator.itemgetter(1), reverse = True )
    return classvotessorted[0][0]

def getaccuracy(predictions,testset):

    correct=0
    for x in range(len(testset)):
        if(predictions[x]==testset[x][-1]):
            correct+=1

    return (correct/len(testset))*100


def main():

    testset=[]
    trainingset=[]
    split=0.67
    filepath='iris.csv'
    loaddataset(filepath,split,trainingset,testset)
    k=3
    predictionSet =[]
    for x in range(len(testset)):
        neighbours = getNeighbours(trainingset,testset[x],k)
        predictions = getResponse(neighbours)
        predictionSet.append(predictions)

    accuracy = getaccuracy(predictionSet,testset)

    print('accuracy is ->', accuracy)

main()
















