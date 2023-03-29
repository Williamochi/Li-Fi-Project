import copy
import numpy as np
def aa():
    a = [1,2,3]
    b = a
    b += [3,2,1]
    return a,b
# print(aa())
def aaa():
    a = 1
    b = a
    b += 2
    return a,b
# print(aaa())
def bb():
    a = [[1,2,3],
         [4,5,6]]
    b=[]
    b += a
    b[1] = [3,2,1]
    b[0][1] = 1
    b[1][1] = 1
    return a,b
# print(bb())
def cc():
    a = [1,2,3]
    b = []
    b.append(a)
    b[0][0] = 2
    return a,b[0],id(a),id(b[0])
# print(cc())
def dd():
    a = [[1,2,3],
         [4,5,6]]
    b = []
    b=copy.deepcopy(a)
    b[0][0] = 2
    return a,b
def ee():
    a = np.array([[1,2,3],
         [4,5,6]])
    b = np.zeros((2, 3)) 
    for i in range(len(a)):
        for j in range(len(a[0])):
            b[i][j]=a[i][j]
    b[0][0] = 2
    return a,b
print(ee())