from numpy import *

import operator
import kNN

def createDataSet():
    group = array([1.0,1.1],[1.0,1.0],[0,0],[0,0.1])
    labels = ['A','A','B','B']
    return group,labels

group,labels = createDataSet()
print group
print labels
ret = kNN.classify0([0,0],group,labels,3)