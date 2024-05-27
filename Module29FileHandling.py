#Scatter Plots
import matplotlib.pyplot as plt
x1 = [1,2,3,4,5]
y1 = [2,3,2,3,4]

x2 = [2,3,4]
y2 = [5,5,5]

x3 = [1,2,3,4,5]
y3 = [6,8,7,8,7]

plt.scatter(x1,y1)       #scatter is to draw the dot
plt.scatter(x2,y2,marker ='v', color='r')
plt.scatter(x3, y3, marker ='^', color= 'm')

#in do lines se n umber print hua near symbol gola zip(x1,y1)
for x,y in zip(x1,y1): #zip jo he combines x and y
    plt.text(x,y+.1,str(y)); # plt.text krne se number add horha at posn x , y+0.1 coordinate
    #text is to print the text message
plt.title('Scatter Plot Example')
plt.show()