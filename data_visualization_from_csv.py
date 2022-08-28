import pandas as pd

from matplotlib import pyplot as plt

#make sure the csv file same directory as the .py file 
datas = pd.read_csv('Book1.csv')
print(datas)

#here you can use datas to access the column data 
#why ColumnB because my excel column is written there ColumnB
print(datas.ColumnB)
#result: 
#left_Side:indicate the indicies only #right-side:indicate data 


#if you want even more detail retreive the by row 
print(datas.ColumnB.iloc[0])


# plot graph by using 2 column
plt.plot(datas.columnA, datas.ColumnB);
#you can change it to 2 dot using o
plt.plot(datas.columnA, datas.ColumnB, 'o');
plt.show()