#example 7:
#-------------------

import matplotlib.pyplot as plt
import numpy as np
# evenly sampled time at 200ms intervals

t = np.arange(0.0, 5.0, 0.2) #numbers generated will be at AN INTERVAL OF 0.2....EG 4.2 ,4.4 , 4.6 , 4.8
print(t)

#red stars , blue squares and green dots
plt.plot(t, t  ,'r*-',
         t, t+3,'bs-',
         t, t+6,'r-', #now do red line an dots green
         t, t+6,'go',
         markersize = 7 )
plt.show()

