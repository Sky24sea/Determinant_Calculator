import numpy as np
import pandas as pd

def enterMatrix():
    n = int(input("Enter the size of the square matrix: "))
    global x
    x = np.zeros((n,n),dtype="int")
    for i in range(n):
        for j in range(n):
            x[i][j] = int(input(f'Enter {i+1}. row , {j+1}. column: '))
    print("Matrix; ")
    print(x)
    return x

def determinant_calculate(x):
    sonuc = 0
    y = np.copy(x)
    if len(x) and len(x[0]) == 2:
        sonuc = ((x[0][0]*x[1][1])-(x[0][1]*x[1][0]))
        return sonuc
    elif len(x) and len(x[0]) == 3:
        t1 = (x[0][0]*x[1][1]*x[2][2])+(x[1][0]*x[2][1]*x[0][2])+(x[2][0]*x[0][1]*x[1][2])
        t2 = (x[0][2]*x[1][1]*x[2][0])+(x[1][2]*x[2][1]*x[0][0])+(x[2][2]*x[0][1]*x[1][0])
        sonuc = t1 - t2
        return sonuc
    else:
        i = 0
        for j in range(len(x[0])):
            y = np.copy(x)
            df = pd.DataFrame(y)
            df.drop(i,axis=0, inplace=True)
            df.drop(j,axis=1, inplace=True)
            y = df.to_numpy()
            M = determinant_calculate(y)
            sonuc = sonuc + (x[i][j]*((-1)**(i+1+j+1))*M)
        return sonuc 
    
enterMatrix()
result = determinant_calculate(x)
print(result)

