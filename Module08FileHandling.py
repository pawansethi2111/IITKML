#reading the data from file

fob=open('sensor1.txt','r')
print("Latest starting location: ", fob.tell())
print("First :",fob.closed )
fob.close()
print("Second:",fob.closed)