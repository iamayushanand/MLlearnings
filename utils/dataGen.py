import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math
class DataGen:
    xVals=[]
    yVals=[]
    labels=[]
    colors=['blue','red','green','purple']
    def __init__(self):
        self.xVals=[]
        self.yVals=[]
        self.labels=[]

    def genData(self,f,N,xRange,label=1):
        for cnt in range(N):
            x=np.random.uniform(low=xRange[0],high=xRange[1])
            y=f(x)+np.random.randn()
            self.xVals.append(x)
            self.yVals.append(y)
            self.labels.append(label)

    def plotData(self):
        plt.figure()
        
        scatter=plt.scatter(self.xVals,self.yVals,c=self.labels,cmap=matplotlib.colors.ListedColormap(self.colors))
        plt.legend(handles=scatter.legend_elements()[0],labels=list(set(self.labels)))
        plt.show()

    def getData(self):
        return self.xVals,self.yVals

    def getLabels(self):
        return self.labels

    def addData(x,y,label=1):
        self.xVals.append(x)
        self.yVals.append(y)
        self.labels.append(label)

