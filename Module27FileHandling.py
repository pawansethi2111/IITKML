# iklauta topic jahan se 1 indexing he

import matplotlib.pyplot as plt
plt.figure(1)       #first figure : me 3 subplots banae he humne
plt.subplot(311)    #the first subplot in the first figure
plt.plot([1,2,3])   #3rd rows, 1 column and 1 box me(311) line draw ki -> 1,2,3
                    #line will be like 0->1 , 1->2, 2->3 (1,2,3)

plt.subplot(312)    # the second subplot in the first figure
plt.plot([4,5,6])   #3rd rows , 1column and 2 box me(312) line draw kro -> 4,5,6`

plt.subplot(313)    # third subplot in first figure
plt.plot([7, 8, 9]) # 3rd row, 1 column abd 3rd box (313) me line draw ki -> [7,8,9]

plt.figure(2)       #a second figure
plt.plot([11, 12, 13]) #creates a subplot(111) by default

plt.figure(1)       #figure 1 current : subplot(313) still current
                    #make subplot(311) in figure1 current
plt.subplot(311)    #subplot 311 title
plt.title('Easy as 1,2,3')

plt.figure(3)       #a second figure
#x = [1,2,3,4,5]

import numpy as np
x = np.arange(1,6) #it will create an array [1,2,3,4,5] excluding 6 including 1
y = x**2    #this is a concept of advanced array where if we square the x , it will square all values ,,not one
            #also if you want to square just one x value do, y= x[0]**2, but here we need x**2
plt.plot(x,y, 'ro-')

plt.show()
