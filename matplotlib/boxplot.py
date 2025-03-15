import matplotlib.pyplot as plt

x =[10,3,4,6,7]
x1 = [4,5,6,7,8]
y = [x,x1]
plt.boxplot(y,showmeans=True,labels = ['c','python'],sym='go',boxprops=dict(color = 'red'),capprops=dict(color = 'blue'),whiskerprops= dict(color = 'red'))

plt.title("BOX PLOT")
plt.legend(loc =2)
plt.show()