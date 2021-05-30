import numpy as np
import matplotlib.pyplot as plt
def perceptron_train(X,y):
    theta=np.random.randint(0,100,(2,1))
    k=0
    print(theta)
    changed=1
    while changed==1:
        changed=0
        for row in range(len(X)):
            #print(np.matmul(X[row],theta))
            if (np.sign(np.matmul(X[row],theta))!=y[row]).all():
                #print(X[row][...,None])
                theta=theta+y[row][0]*X[row][...,None]
                #print(theta)
                changed=1
                k+=1
    print("number of updates:"+str(k))
    return theta
def perceptron_test(theta,X,y):
    accuracy=0
    for row in range(len(X)):
        if (np.sign(np.matmul(X[row],theta))==y[row]).all():
            accuracy+=1
    return accuracy/len(X)
X=[]
y=[]
plotx=[]
ploty=[]
def loaddata():
    Xfile=open("p1_a_X.dat")
    for lin in Xfile:
        tmp=[eval(x) for x in lin.split()]
        plotx.append(tmp[0])
        ploty.append(tmp[1])
        X.append(tmp)
        #print(tmp)
    yfile=open("p1_a_y.dat")
    for lin in yfile:
        tmp=[eval(lin)]
        y.append(tmp)
        #print(tmp)
def loaddata_test():
    global X
    global y
    X=[]
    y=[]
    Xfile=open("p1_b_X.dat")
    for lin in Xfile:
        tmp=[eval(x) for x in lin.split()]
        X.append(tmp)
        #print(tmp)
    yfile=open("p1_b_y.dat")
    for lin in yfile:
        tmp=[eval(lin)]
        y.append(tmp)
        #print(tmp)
loaddata()
thetaRecv=perceptron_train(np.array(X),np.array(y))
print(thetaRecv)
loaddata_test()
print(perceptron_test(thetaRecv,np.array(X),np.array(y)))
def perceptronLine(x):
    return (-1*thetaRecv[0][0]/thetaRecv[1][0])*x
linePlot=list(map(perceptronLine, plotx))
plt.scatter(plotx,ploty)
plt.plot(plotx,linePlot)
plt.show()
#thetaRecv=loaddata(X,y)
