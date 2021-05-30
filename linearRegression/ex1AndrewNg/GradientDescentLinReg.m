clear;
data=load('ex1data1.txt');
hold on;
global X=data(:,1);
global Y=data(:,2);
%plot(X,Y,'rx','MarkerSize',10);
global m=length(X);
X=[X ones(m,1)];
function [thetaNew] = updateRule(theta,alpha)
  global m;
  global X;
  global Y;
  thetaNew=theta-alpha*(1/m)*sum(X'*(X*theta-Y),2);
end
function plotRegression(theta)
  global X;
  t=X'(1,:);
  t=[t' ones(length(t),1)];
  %disp(t);
  ylinearReg=t*theta;
  
  %disp(t'(1,:));
  h=plot(t'(1,:),ylinearReg');
  %pause(10);
  %delete(h);
end

function [cost] = computeCost(theta)
  global X;
  global Y;
  global m;
  cost=sum((X*theta-Y).^2)/(2*m);
end


iters=1500;
theta=[0;0];
%alpha=2*m/(sum(X(:,1).^2))
alpha=0.01;
%disp(computeCost(theta));
Ysurf=linspace(-10,10,100);
Xsurf=linspace(-1,4,100);
Zsurf=zeros(length(Xsurf),length(Ysurf));
for i=1:length(Xsurf)
  for j=1:length(Ysurf)
    Zsurf(i,j)=computeCost([Xsurf(i);Ysurf(j)]);
   end
end
%disp(Zsurf);
%Zsurf=computeCost([Xsurf. Ysurf.]);
Zsurf=Zsurf';
contour(Xsurf,Ysurf,Zsurf,logspace(-2,3,20));
%for i=0:iters
%disp(updateRule(theta,0.01));
%plotRegression(updateRule(theta,0.01));
%Xsurf=[Xsurf theta(1)];
%Ysurf=[Ysurf theta(2)];
%Zsurf=[Zsurf computeCost(theta)];
%theta=updateRule(theta,alpha);
%disp(theta);
%end
%plotRegression(theta);
%surf(Xsurf,Ysurf,Zsurf);