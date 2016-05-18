from numpy import *

import operator
import kNN
import matplotlib
import matplotlib.pyplot as plt

datingDataMat, datingLabels = kNN.file2matrix('datingTestSet.txt')
# flight range, time playing video game, ice cream ate
#print datingDataMat
print datingLabels

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,0],datingDataMat[:,1],
           15.0*array(datingLabels),15.0*array(datingLabels))
#plt.show()

normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
print ranges
print minVals

kNN.datingClassTest()

