import matplotlib.pyplot as plt
idxes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr1 = [23, 40, 28, 43, 8 , 44, 43, 18, 17 ]
arr2 = [17, 30, 22, 14, 17, 17, 29, 22, 30]
arr3 = [15, 31, 18, 22, 18, 19, 13, 32, 39]


#adding legend for stack plots is tricky
#total sale in january : add all 3 in index 1 : 23+17+15
mylabels = ['D1', 'D2', 'D3']
#mylabels =['Salesperson1', 'Salesperson2' , 'Salesperson3']
#comparative analysis

plt.stackplot(idxes, arr1, arr2, arr3, labels = mylabels, colors=['r','g','b'] )

plt.title('Stack Plot Example')
plt.legend(loc = "upper center")
#loc ==>location
plt.show()