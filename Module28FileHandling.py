import matplotlib.pyplot as plt
#look at index 4 and 6, which demonstrate

#overlapping cases

x1 = [1,3,4,5,6,7,9]
y1 = [4,7,2,4,7,8,3]

x2= [2,4,6,8,10]
y2= [5,6,2,6,2]

plt.bar(x1, y1, label="Blue Bar",color='b') #help in the legend (top corner me dabba) that shows blue line and red line)
plt.bar(x2,y2, label="Red Bar", color ='r') #help in the legend (top corner wala box ) that shows parameter
plt.plot(x1,y1)   #note in the output blue line is not touching the blue bar,,,it is touching red bar tho
plt.xlabel("bar number")
plt.ylabel("bar height")
plt.title("bar chart example")
plt.legend()
plt.show()