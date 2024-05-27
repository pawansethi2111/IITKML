import random
import csv
import operator
import math


def loaddataset(filepath, split, trainingset=[], testset=[]):
    file = open(filepath, 'r')
    csvfile = csv.reader(file)
    dataset = list(csvfile)
    #print(dataset)
    for x in range(1, len(dataset)):
        for y in range(5):
            dataset[x][y] = float(dataset[x][y])

        if random.random() < split:
            trainingset.append(dataset[x])
        else:
            testset.append(dataset[x])


def euclideandistance(instance1, instance2, length):
    dist = 0
    for x in range(1, length):
        dist += pow((instance1[x] - instance2[x]), 2)

        return math.sqrt(dist)


def getneighbours(trainingset,testinstance, k):
    length = len(testinstance) - 1
    dist = 0
    Distances = []
    for x in range(len(trainingset)):
        dist = euclideandistance(testinstance,trainingset[x], length)
        Distances.append([trainingset[x], dist])

    Distances.sort(key = operator.itemgetter(1))

    neighbours = []

    for x in range(k):
# error here
        neighbours.append(Distances[x][0])

    return neighbours


def getresponse(neighbours):
    classvotes = {}

    for x in range(len(neighbours)):
        predictions = neighbours[x][-1]
        if predictions in classvotes:
            classvotes[predictions] += 1
        else:
            classvotes[predictions] = 1

    Classvotessorted = sorted(classvotes.items(), key=operator.itemgetter(1), reverse=True)

    return Classvotessorted[0][0]


def getaccuracy(testset, predictionset):
    correct = 0
    for x in range(len(testset)):
        if testset[x][-1] == predictionset[x]:
            correct += 1
        print('actual dataset', testset[x][-1], " ==> ",end="")
        print('predicted dataset', predictionset[x])
    return correct / len(testset) * 100


def main():
    trainingset = []
    testset = []
    k = 3
    filepath = 'iris.csv'


    split = 0.67

    loaddataset(filepath, split, trainingset, testset)
    Predictionset = []
    for x in range(len(testset)):
        neighbours = getneighbours(trainingset, testset[x], k)
        predictions = getresponse(neighbours)
        Predictionset.append(predictions)

    accuracy = getaccuracy(testset, Predictionset)

    print('accuracy is', accuracy)
    #print('neighbours are', neighbours)


main()


