import numpy as np


A = np.random.randint(1,10,size = (3,3))
B = np.random.randint(1,10,size = (3,3))
print(A)
print(B)

def multiply_matrix(A,B):
  
        C = np.zeros((A.shape[0],B.shape[1]),dtype = int)
        for row in range(A.shape[0]): 
            for col in range(B.shape[1]):
                for elt in range(len(B)):
                  C[row, col] += A[row, elt] * B[elt, col]
        return C


result=multiply_matrix(A,B)
print(result)
