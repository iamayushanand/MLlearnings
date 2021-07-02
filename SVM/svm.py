import sys
sys.path.insert(1,"../utils")
from dataGen import DataGen 
from cvxopt import matrix,solvers
import numpy as np
import matplotlib.pyplot as plt
gen=DataGen()
gen.genData(lambda x: x+10,500,(1,20),label=1)
gen.genData(lambda x: x-10,500,(1,20),label=-1)
#gen.plotData()

x,y=gen.getData()
lbl=gen.getLabels()
lbl=np.array(lbl)
X=[[x[i],y[i]] for i in range(len(x))]
X=np.array(X)
print(X.shape)
lbl=lbl.reshape((1,1000))
print(lbl.shape)
P=matrix(np.eye(2),tc='d')
print(np.matmul(-1*lbl,X).shape)
G=matrix(np.matmul(-1*lbl,X),tc='d')
q=matrix(np.zeros((2,1)),tc='d')
b=matrix(-1*np.ones(2),tc='d')
sol=solvers.qp(P,q,G,b)
xvals=np.linspace(0,20,1000)
plt.plot(xvals,(-sol['x'][0]/sol['x'][1])*xvals)
plt.scatter(x,y)
plt.show()
print(sol['x'][0])
