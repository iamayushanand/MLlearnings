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
colors=np.where(lbl==1,'b','r')
#X=[[x[i] for i in range(len(x))],[y[i] for i in range(len(y))]]
X=[[lbl[i]*x[i],lbl[i]*y[i]] for i in range(len(x))]
X=np.array(X)
print(X.shape)
lbl=lbl.reshape((1000,1))
lbl=np.hstack((lbl,lbl))
print(lbl.shape)
P=matrix(np.eye(2),tc='d')
print(X.shape)
G=matrix(X,tc='d')
q=matrix(np.zeros((2,1)),tc='d')
b=matrix(-1*np.ones((1000,1)),tc='d')
sol=solvers.qp(P,q,G,b)
xvals=np.linspace(0,20,1000)
plt.plot(xvals,(-sol['x'][0]/sol['x'][1])*xvals)
plt.scatter(x,y,c=colors)
plt.show()
print(-sol['x'][0]/sol['x'][1])
