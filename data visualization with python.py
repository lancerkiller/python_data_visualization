import pandas as pd

from matplotlib import pyplot as plt


x = [1,2,3]
#dispaly y axis for first graph 
y = [1,3,4]
#display z axis for second graph 
z = [10,5,0]

#x,y graph 
plt.plot(x,y)
#x, z graph 
plt.plot(x,z)
plt.title("Testing plot")
plt.xlabel('x')
plt.ylabel('y')

plt.legend(['this is y axis','this is z'])
plt.show()