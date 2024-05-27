# pie chart
import matplotlib.pyplot as plt
myLabels = ['S1', 'S2', 'S3'] #s1 section1 #s2 section2 #drawing will be anticlockwise always
sections =[60, 90, 50 ]
myColors = ['c','g', 'r']
plt.pie(sections, labels = myLabels, colors = myColors, startangle = 45 , explode=(0,0.1,0.2), autopct = '%.2f%%' )
# %.2f is for fill in the blank where have to round about till 2 decimal places
# and then %% is for %% at the end

#it starts drawing from anticlockwise
# at a startangle of 45 degree and then draws it so on and so forth
#in diagram s2 is thoda sa bahar why , because we have used explode(0,0.1,0)

plt.title('Pie Chart Example')
plt.show()

