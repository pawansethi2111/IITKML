import numpy as np
#are all elemenets greater than 0
print(np.all([1,2,3,4]))
print(np.all( [1,2,0,3,4]))

# is there any element greater than zero
print(np.any([1,2,3,4]))      #true
print(np.any([1,2,0,3,4]))    #true
print(np.any([0,0,0,0.,0]))   #false
print(np.any([0,0,0,0.,0,1])) #true

true,false,none
