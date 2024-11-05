import numpy as np

def getmatrix(row,col):
    matrix=[]
    for i in range(row):
        ro=list(map(int,input().split()))
        matrix.append(ro)
    return np.array(matrix)
   
def multiply(arr1,arr2):
    res=np.dot(arr1,arr2)
    return res
   
row1=int(input())
col1=int(input())
row2=col1
col2=int(input())
arr1=getmatrix(row1,col1)
arr2=getmatrix(row2,col1)
result=multiply(arr1,arr2)
print(result)
