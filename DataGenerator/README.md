# Data generation utilities
This folder contains codes and utilities for easily generating data and testing them.

| function name | Arguments | Description |
| ------------- | --------- | ----------- |
| genData | a function f ,a tuple,a label(1 by default) | generates data of the form y=f(x)+Gaussian noise where x ranges as specified by tuple and assigns a label as passed into the arguments |
| getData | none | returns the generated data or none if no data has been generated in the form of a tuple of two lists (xValues,yValues)|
| plotData | none | returns none if no data generated else it plots the generated data by matplotlib library |
| getLabels | none | returns labels of the generated datapoints as a list |
| addData | two numbers specifying coordinates and label | adds a point to the dataset |

