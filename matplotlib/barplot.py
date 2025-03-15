import matplotlib.pyplot as plt
import numpy as np
# creating bar plot

x = ["python", "c", "c++", "java"]
y = [85,70,60,82]
z = [20,30,40,50]


plt.xlabel("languages",fontsize = 15)       #give lable to x axis
plt.ylabel("numbers",fontsize = 15)         #give lable to y axis
plt.title("language popularity",fontsize = 15)  #give title to the graph

width = 0.2
p = np.arange(len(x))
p1 = [j+width for j in p]



plt.bar(p1,y , width, color = "g")
plt.bar(p1,z , width, color = "r")

plt.xticks(p+width/2,x,rotation = 10)
 
plt.show() 


#for horizontal bar graph use plt.barh()
# align can be edge also  & color = "g" green color
# linewidth  change width of edge line
# ":" provide doted edge line and default (solid line)
#lable = "popularity" this lable parameter works with plt.legend() function give lable /title to graph
#plt.bar(x,y , width=0.5 , color = "g" , align="center", edgecolor = "r" , linewidth = 5 , linestyle = ":")  
