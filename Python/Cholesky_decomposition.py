import numpy as np
import math
def Cholesky(matrix):

    num_of_rows = matrix.shape[0]
    num_of_columns = matrix.shape[1]

    # Initialize the lower triangular matrix
    lower_matrix = np.zeros((num_of_columns,num_of_rows),dtype=float)

    if num_of_rows != num_of_columns:
        raise ValueError("Matrix must be square for Cholesky decomposition.")

    # Loop through rows and columns
    for i in range (0,num_of_rows,1):
        for j in range(0,num_of_rows,1):
           if(i >=j):
               if (i == j): ## Diagonal elements
                   t_s = 0
                   for k in range(0, j, 1):
                       t_s += lower_matrix[i, k] ** 2
                   lower_matrix[i, j] = math.sqrt(matrix[i, j] - t_s)
               else:# Off-diagonal elements
                   t_s = 0
                   for k in range(0, j, 1):
                       t_s = lower_matrix[i, k] * lower_matrix[j, k]
                   lower_matrix[i, j] = (matrix[i, j] - t_s) / lower_matrix[j, j]
    print("Lower matrix\n",lower_matrix)

if __name__ == '__main__':

    array = np.matrix([[4.0,-1.0,1.0],[-1.0,4.25,2.75],[1.0,2.75,3.5]])
    Cholesky(array)