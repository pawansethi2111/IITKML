#example 2

import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,4,9,16],'k3') #values for x-axis,y-axis , r- is for red line , m for magenta , b for blue , o- for dot dot
plt.xlabel("----some numbers----")
plt.ylabel("----squared values----")
plt.axis([0,5,0,17])
# x-axis range will be 0 to 5
# y-axis range will be 0 to 17
plt.show()
