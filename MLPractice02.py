import csv
filename = open("D:\\iitk\\indians-diabetes.data_2.csv.csv")

reader = csv.reader(filename,delimiter=',')

lines = list(reader)

print('No of Rows: ',len(lines),'\n\n')

print("List of Data \n",lines)

print('\n\n\n\n')

for line in lines :
    print(line,"\n________________________")
    