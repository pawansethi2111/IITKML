import numpy as np
d1 = np.array( [ [1,2],
                 [3,4],
                 [5,6],
                 [7,8],
                 [9, 10],
                 [11,12],
                 [13,14] ] )
print(d1[1: :2,1 ])
# 1 se start hokar ...gap of :2 ,,,,,,pick column 1


print(d1[0: 5 :2, 0])
#0 se start hokar till the range of 5(excluding) at a gap of 2 ,pick 0
print(d1)
print( d1.shape)