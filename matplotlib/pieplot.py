import matplotlib.pyplot as plt

x = [10,50,80,40]
y = ['c','c++','python','java']
ex = [ 0.4 ,0.0,0.0,0.0]
c =['red','green','yellow','blue']

plt.pie(x,labels=y,colors=c,explode=ex,autopct='%0.1f%%',shadow=True,radius=1,labeldistance=1.1,startangle=0,textprops={'fontsize':15},counterclock=False,wedgeprops={'linewidth':5},rotatelabels=False)
plt.title('PIE CHART')
plt.legend(loc=2)
plt.show()