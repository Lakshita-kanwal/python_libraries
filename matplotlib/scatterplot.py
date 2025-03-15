import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [2,3,4,5,6,7,8]
y2 = [15,64,27,14,13,17,18]
c = [10,20,45,60,98,34,67]
size = [300,400,100,600,400,500,200]

plt.scatter(x,y,s = size,cmap='virids',alpha = 0.4,marker="*")

#add multiple scatter plolts in same graph 
plt.scatter(x,y2,s = size,cmap='virids',alpha = 0.4)
t = plt.colorbar()
t.set_label("COLORBAR",fontsize = 15)
plt.title("SCATTER PLOT",fontsize = 15)
plt.xlabel("DAY")
plt.ylabel("NUMBER")

plt.grid()
plt.show()

#plt.scatter(x,y,color = c,s = size,alpha= 0.4,marker="*",edgecolors='black',linewidths=1)
#parameter of plt.scatter function
# marker = change shape of scatters
#edgecolors = outline colour of scatters
#linewidth = change the width of scatters edge
#setlable  = set lanle for colour bar
#color bar = show the rnage of colour used in graph
#alpha =use to fade or dark the color of scatters
#size array = use to change the size of corrosponding scatter
