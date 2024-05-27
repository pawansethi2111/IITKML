#Note: Add multiple line data in sensor1.txt file manually

fob=open('sensor.txt','r')
print("Line 1=", fob.readline() )
print("Line 2=",fob.readline() )
fob.close()

