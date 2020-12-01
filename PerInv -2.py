# In this exercise you need to create the inverse of matrix A using only row swaps


# -------------------------------------------
# Prints the content of matrix M 
# -------------------------------------------

def PrintMatrix(M):
    
    for i in range(0, 5):
        print('|{:>3d}{:>3d}{:>3d}{:>3d}{:>3d} |'.format(M[i][0],M[i][1],M[i][2],M[i][3],M[i][4]))


# -------------------------------------------
# Prints embedded matrices M and N
# -------------------------------------------

def PrintEmbedded(M,N):
    
    for i in range(0, 5):
        print('|{:>2d}{:>3d}{:>3d}{:>3d}{:>3d} ¦'.format(M[i][0],M[i][1],M[i][2],M[i][3],M[i][4])
              +'{:>2d}{:>3d}{:>3d}{:>3d}{:>3d} |'.format(N[i][0],N[i][1],N[i][2],N[i][3],N[i][4]))


# -------------------------------------------
# Prints embedded product M x N = P
# -------------------------------------------

def PrintProduct(M,N,P):
    
    for i in range(0, 5):
        if (i==2):
            print('|{:>2d}{:>3d}{:>3d}{:>3d}{:>3d} |'.format(M[i][0],M[i][1],M[i][2],M[i][3],M[i][4])
              +' x |{:>2d}{:>3d}{:>3d}{:>3d}{:>3d} |'.format(N[i][0],N[i][1],N[i][2],N[i][3],N[i][4])
              +' = |{:>2d}{:>3d}{:>3d}{:>3d}{:>3d} |'.format(P[i][0],P[i][1],P[i][2],P[i][3],P[i][4]))
        else:
            print('|{:>2d}{:>3d}{:>3d}{:>3d}{:>3d} |'.format(M[i][0],M[i][1],M[i][2],M[i][3],M[i][4])
              +'   |{:>2d}{:>3d}{:>3d}{:>3d}{:>3d} |'.format(N[i][0],N[i][1],N[i][2],N[i][3],N[i][4])
              +'   |{:>2d}{:>3d}{:>3d}{:>3d}{:>3d} |'.format(P[i][0],P[i][1],P[i][2],P[i][3],P[i][4]))
 

# -------------------------------------------
# In Matrix M swaps row_j with row_i
# -------------------------------------------

def SwapRows(i,j,M):        # swap row_i with row_j

    Y=M[i]
    M[i]=M[j]
    M[j]=Y


# -------------------------------------------
# Computes product N of square matrices M1, M2
# -------------------------------------------
def SqProd(M1,M2,N):

    for i in range(0, 5):
        for j in range(0, 5):
            N[i][j]=0
            for k in range (0, 5):
                N[i][j]+=(M1[i][k]*M2[k][j])
# -------------------------------------------

# Data initialisation

A=[[0,1,0,0,0],
   [0,0,1,0,0],
   [0,0,0,1,0],
   [0,0,0,0,1],
   [1,0,0,0,0]]

B=[[1,0,0,0,0],
   [0,1,0,0,0],
   [0,0,1,0,0],
   [0,0,0,1,0],
   [0,0,0,0,1]]

C=[[0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0]]

print ("The original matrix A, the task is to compute A^-1\n")
PrintMatrix(A)

print ("\n We adopt the embedded representation with matrix A on the left and the Identity matrix B on the right\n")
PrintEmbedded(A,B)

# -------------------------------------------
# DO NOT CHANGE ANYTHING ABOVE THIS LINE
# -------------------------------------------


# Below you write your code including
# Comment on the manipulated rows using print operation
# apply function SwapRows to manipulate A and B accordingly and
# apply function PrintEmbedded to print the current content of embedded A and B


print("\n\n Row 5 is identified as optimal constant in the computation of the inverse,i.e; each rows in A and B is swapped with Row 5\n")

print("n\n Below : Row_1 is swapped for Row_5\n")

SwapRows(0,4,A)
SwapRows(0,4,B)

PrintEmbedded(A,B)

print("n\n Below : Row_2 is swapped for Row_5\n")

SwapRows(1,4,A)
SwapRows(1,4,B)

PrintEmbedded(A,B)

print("n\n Below : Row_3 is swapped for Row_5\n")

SwapRows(2,4,A)
SwapRows(2,4,B)

PrintEmbedded(A,B)

print("n\n Below: Row_4 is swapped for Row_5\n")

SwapRows(3,4,A)
SwapRows(3,4,B)

PrintEmbedded(A,B)

# -------------------------------------------
# DO NOT CHANGE ANYTHING BELOW THIS LINE
# -------------------------------------------

# final test of correctness, by matrix multiplication of A and obtained B=A^-1

A=[[0,1,0,0,0],
   [0,0,1,0,0],
   [0,0,0,1,0],
   [0,0,0,0,1],
   [1,0,0,0,0]]

SqProd(A,B,C)

print ("\n\n We compute the product of A and A^-1 obtaining identity matrix on the right\n")

PrintProduct(A,B,C)
