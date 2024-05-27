
#example1
#writing the data into file

fob = open('sensor1.txt','w')
totalchars=fob.write("This is first line")
fob.close()
print("Result = ",totalchars)
print('Data saved successfully')

#example2
#reading the data from file

fob = open('sensor1.txt','r')
print("Latest starting location: ", fob.tell())
print("First :",fob.closed)
fob.close()
print("Second:",fob.closed)

#example3
#Note: Add multiple line data in sensor1.txt file manually

fob = open('sensor1.txt','r')
print("Line 1=", fob.readline() )
print("Line 2=",fob.readline() )
fob.close()

#example 4:
fob = open('sensor1.txt','r')
arr = fob.readlines()
print("data= \n",arr)
fob.close()


#example 5
fob = open('sensor1.txt','r')
mylist = fob.readlines()

