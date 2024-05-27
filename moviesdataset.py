import csv
import math
import random
import operator

def loadDataset(filepath, split, trainingset =[], testset=[]):

    file = open(filepath, 'r')
    csvfile = csv.reader(file)

    dataset = list(csvfile)

    for x in range(1,len(dataset)):
        for y in range(5):
            dataset[x][y] = float(dataset[x][y])

        if random.random()<split:
            trainingset.append(dataset[x])
        else:
            testset.append(dataset[x])

def euclideandistance(instance1,instance2,lenghtyyy ):

    dist=0
    for i in range(1,lenghtyyy):
        dist += pow((instance1[i]-instance2[i]),2)

    return math.sqrt(dist)

def getNeighbours(testinstance,trainingset,k ):

    Distance = []
    length = len(testinstance)-1
    for i in range(len(trainingset)):
        dist = euclideandistance(testinstance,trainingset[i],length)
        Distance.append([trainingset[i],dist])
    Distance.sort(key=operator.itemgetter(1))
    neighbours=[]
    for i in range(k):
        neighbours.append(Distance[i][0])

    return neighbours

def getResponse(neighbours):
    classvotes={}

    for i in  range(len(neighbours)):

        if neighbours[i][-1] in classvotes:
            classvotes[neighbours[i][-1]]+=1
        else:
            classvotes[neighbours[i][-1]]=1

    classvotessorted=[]
    classvotessorted = sorted(classvotes.items(), key = operator.itemgetter(1), reverse =True )

    return classvotessorted[0][0]

def getaccuracy(testset, predictions):

    correct=0
    for x in range(len(testset)):
        print('actual->',testset[x][-1])
        print('predicted->',predictions[x])
        if(testset[x][-1] == predictions[x]):
            correct+=1
    return correct/len(testset)*100

def main():
    testset=[]
    trainset=[]
    split=0.67
    filepath = 'iris.csv'

    loadDataset(filepath,split,trainset,testset)
    k=3
    predictionset=[]
    correct=0
    for x in range(len(testset)):
        neighbours= getNeighbours(testset[x],trainset,k)
        predictions = getResponse(neighbours)
        predictionset.append(predictions)


    accuracy = getaccuracy(testset,predictionset)

    #accuracy = correct/len(testset)

    print('accuracy is ->', accuracy)
main()







