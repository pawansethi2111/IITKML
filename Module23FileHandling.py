#example : for comparative analysis eg for 2 teamsd playing cricket , which one scored better runs

import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5], [1,2,3,4,5], 'go-', label='line 1', linewidth=2 )
plt.plot([1,2,3,4,5],[1,4,9,16,25],'rs--', label='label 2', linewidth=4 ) #values for x-axis,y-axis , r- is for red line , m for magenta , b for blue , o- for dot dot
plt.xlabel("----Team 1 Runs----")
plt.ylabel("----Team 2 Runs----")
plt.axis([0,6,0,26])
plt.legend(loc="upper left") #also write center , upper center , lower centre
# x-axis range will be 0 to 5
# y-axis range will be 0 to 17
plt.show()
