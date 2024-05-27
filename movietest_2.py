import csv
import math
import operator
import random

def loadDataset(filepath, split, testset=[], trainset=[] ):

    filename = open(filepath, 'r')
    f = csv.reader(filename)
    dataset = list(f)

    for x in range(1,len(dataset)):
        for y in range(5):
            dataset[x][y] = float(dataset[x][y])

        if random.random() < split:
            trainset.append(dataset[x])
        else:
            testset.append(dataset[x])

def Euclideandistance(instance1, instance2, length):
    dist = 0
    for i in range(1,length):
        dist += pow((instance1[i] - instance2[i]),2)

        return math.sqrt(dist)

def getNeighbours(testinstance, trainset, k):

    length = len(testinstance)-1
    distances = []
    for i in range(len(trainset)):
        dist = Euclideandistance(testinstance,trainset[i],length)
        distances.append([trainset[i], dist])

    distances.sort(key = operator.itemgetter(1))
    neighbours = []
    for i in range(k):
        neighbours.append(distances[i][0])
    return neighbours

def getPrediction(neighbours):

    classvotes = {}

    for i in range(len(neighbours)):
        val = neighbours[i][-1]
        if val in classvotes:
            classvotes[val] += 1
        else:
            classvotes[val] = 1

    classsorted = sorted(classvotes.items() , key = operator.itemgetter(1), reverse = True)

    return classsorted[0][0]

def getaccuracy(prediction,testset):
    correct = 0
    for x in range(len(testset)):
        if prediction[x] == testset[x][-1]:
            correct += 1
        print('Actual data ->', testset[x][-1], " Predicted Data ->", prediction[x])
    accuracy = correct/len(testset)*100.0
    return accuracy


def main():
    testset=[]
    trainingset=[]
    split = 0.67
    k=int(input("Enter K : "))
    loadDataset('iris.csv',split,testset,trainingset)

    print('test set size ->', len(testset))
    print('train set size->', len(trainingset))

    prediction = []
    for x in range(len(testset)):
        neighbours = getNeighbours(testset[x],trainingset,k)
        result = getPrediction(neighbours)

        prediction.append(result)
    accuracy = getaccuracy(prediction,testset)

    print("Accuracy is" , accuracy )

main()