import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
data = np.genfromtxt('/home/hadoop/results-csv.csv', delimiter=',', names=['x', 'y'])

x=data['x']
y=data['y']

plt.figure(figsize=(12, 9))  
plt.xticks(range(000000000, 1900000000000, 1000000),fontsize=14)  

plt.yticks(range(0,500, 50), fontsize=14)  


plt.title('Doctor/Service')
plt.xlabel("Doctor ID", fontsize=16)  
plt.ylabel("No. of Services", fontsize=16)  

plt.hist(list(x)+list(y),color="#3F5D7D",bins=10)

plt.savefig("/home/hadoop/fraud.png", bbox_inches="tight");  