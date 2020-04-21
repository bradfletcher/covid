import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.style as mplstyle
mplstyle.use('fast')

fig, ax = plt.subplots()

f = open("stats.csv", "r" ) 

series1 = [] 
series2 = [] 
series3 = [] 
xaxis = [] 

# mpl.rcParams['path.simplify'] = True 
# mpl.rcParams['path.simplify_threshold'] = 1.0 
count = 0
for l in f:
    if(count != 0): 
        values = []
        values = l.split(",") 
        xaxis.append(int( values[0] ) / 24.0 )
        series1.append(int(values[1])) 
        series2.append(int(values[2])) 
        series3.append(int(values[3])) 
    count +=1 

plt.plot(xaxis, series1, 'r',  markevery=5, label="infected" )
plt.plot(xaxis, series2, 'g',  markevery=5, label="recovered" )
plt.plot(xaxis, series3, 'black',  markevery=5, label="dead" )
plt.ylabel("people")
plt.xlabel("days")
plt.title("COVID-19 Simulation" )

# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# place a text box in upper left in axes coords 
ax.text(0.6, 0.5, "Infected: " + str(series1[-1]) + "\nRecovered: " + str(series2[-1]) + "\nDead: " + str(series3[-1]) , transform=ax.transAxes, fontsize=14,
        verticalalignment='bottom', bbox=props)

plt.legend(loc='upper left') 
plt.savefig('figure1.pdf') 
plt.savefig('figure1.png') 
plt.show() 
