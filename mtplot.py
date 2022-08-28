import matplotlib.pyplot as plt

animals = ['tiger','lion','gorlilla','pikachu']
counts = [1,3,42,12]

plt.pie(counts,labels=animals,autopct='%.0f%%')
plt.title('Animals we saw in the forest')

plt.show()

