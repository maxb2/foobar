# This fails hidden test 9 for some reason...
# I ended up using https://github.com/Trismeg/FooBar/blob/master/doomsday_fuel.py

from fractions import Fraction
# from numpy.lcm import reduce as lcm_reduce
# from math import gcd


def is_terminal(l):
    b = True
    for x in l:
        b = b and x == 0
    return b

def solution(M):
    n = len(M)

    terminals = [is_terminal(x) for x in M]
    t_order = [i for i in range(n) if terminals[i]]
    o_order = [i for i in range(n) if i not in t_order]
    # order = t_order + o_order

    # print(terminals, t_order, o_order)


    P = [[0 for i1 in range(n)] for i2 in range(n)]
  

    for i1 in range(n):
        if terminals[i1]:
            P[i1] = [ Fraction(0) for x in range(n) ] 
            P[i1][i1] = Fraction(1)
        else:
            denom = sum(M[i1])
            P[i1] = [Fraction(x,denom) for x in M[i1]]
    # return P

    o_n = len(o_order)
    t_n = len(t_order)


    R = [ [ Fraction(0) for i2 in range(t_n)] for i1 in range(o_n)]
    for i1 in range(o_n):
        for i2 in range(t_n):
            R[i1][i2] = P[o_order[i1]][t_order[i2]]

    # print("##### R")
    # print(R)
    # print("#####")

    I = [ [ Fraction(0) for i2 in range(o_n)] for i1 in range(o_n)]
    for i in range(o_n):
        I[i][i] = Fraction(1) 




    FF = [ [ Fraction(0) for i2 in range(o_n)] for i1 in range(o_n)]

    for i1 in range(o_n):
        for i2 in range(o_n):
            ii = Fraction(0)
            if i1 == i2:
                ii = Fraction(1)
            FF[i1][i2] = ii - P[o_order[i1]][o_order[i2]]

    # print('####### I-Q')
    # print(FF)
    # print('#######')

    F = invert_matrix(FF)
    probs = matrix_multiply(F,R)[0]
    denoms = [fr.denominator for fr in probs]

    lcm = denoms[0]
    for i in denoms[1:]:
        lcm = lcm*i//gcd(lcm, i)

    vals = [int(fr.numerator * lcm / fr.denominator) for fr in probs]
    vals.append(lcm)


    return vals


def gcd (a,b):
    if (b == 0):
        return a
    else:
        return gcd (b, a % b)
         
def check_squareness(A):
    """
    Makes sure that a matrix is square
        :param A: The matrix to be checked.
    """
    if len(A) != len(A[0]):
        raise ArithmeticError("Matrix must be square to inverse.")

def determinant(A, total=0):
    indices = list(range(len(A)))
    
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val

    for fc in indices:
        As = copy_matrix(A)
        As = As[1:]
        height = len(As)
        # builder = 0

        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc+1:]

        sign = (-1) ** (fc % 2)
        sub_det = determinant(As)
        total += A[0][fc] * sign * sub_det

    return total

def check_non_singular(A):
    det = determinant(A)
    if det != 0:
        return det
    else:
        raise ArithmeticError("Singular Matrix!")
        
def zeros_matrix(rows, cols):
    """
    Creates a matrix filled with zeros.
        :param rows: the number of rows the matrix should have
        :param cols: the number of columns the matrix should have
        :returns: list of lists that form the matrix.
    """
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(Fraction(0))

    return M

def identity_matrix(n):
    """
    Creates and returns an identity matrix.
        :param n: the square size of the matrix
        :returns: a square identity matrix
    """
    I = zeros_matrix(n, n)
    for i in range(n):
        I[i][i] = Fraction(1)

    return I

def copy_matrix(M):
    """
    Creates and returns a copy of a matrix.
        :param M: The matrix to be copied
        :return: The copy of the given matrix
    """
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(rows):
            MC[i][j] = M[i][j]

    return MC

def print_matrix(M):
    """
    docstring here
        :param M: The matrix to be printed
    """
    for row in M:
        print([round(x,3)+0 for x in row])

def transpose(M):
    """
    Creates and returns a transpose of a matrix.
        :param M: The matrix to be transposed
        :return: the transpose of the given matrix
    """
    rows = len(M)
    cols = len(M[0])

    MT = zeros_matrix(cols, rows)

    for i in range(rows):
        for j in range(cols):
            MT[j][i] = M[i][j]

    return MT

def matrix_multiply(A,B):
    """
    Returns the product of the matrix A * B
        :param A: The first matrix - ORDER MATTERS!
        :param B: The second matrix
        :return: The product of the two matrices
    """
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        raise ArithmeticError('Number of A columns must equal number of B rows.')

    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C

def check_matrix_equality(A,B, tol=None):
    """
    Checks the equality of two matrices.
        :param A: The first matrix
        :param B: The second matrix
        :param tol: The decimal place tolerance of the check
        :return: The boolean result of the equality check
    """
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False

    for i in range(len(A)):
        for j in range(len(A[0])):
            if tol == None:
                if A[i][j] != B[i][j]:
                    return False
            else:
                if round(A[i][j],tol) != round(B[i][j],tol):
                    return False

    return True

def invert_matrix(A, tol=None):
    """
    Returns the inverse of the passed in matrix.
        :param A: The matrix to be inversed
        :return: The inverse of the matrix A
    """
    # Section 1: Make sure A can be inverted.
    check_squareness(A)
    check_non_singular(A)

    # Section 2: Make copies of A & I, AM & IM, to use for row operations
    n = len(A)
    AM = copy_matrix(A)
    I = identity_matrix(n)
    IM = copy_matrix(I)

    # Section 3: Perform row operations
    indices = list(range(n)) # to allow flexible row referencing ***
    for fd in range(n): # fd stands for focus diagonal
        # fdScaler = 1.0 / AM[fd][fd]
        fdScaler = Fraction(1,  AM[fd][fd])
        # FIRST: scale fd row with fd inverse. 
        for j in range(n): # Use j to indicate column looping.
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        # SECOND: operate on all rows except fd row as follows:
        for i in indices[0:fd] + indices[fd+1:]: # *** skip row with fd in it.
            crScaler = AM[i][fd] # cr stands for "current row".
            for j in range(n): # cr - crScaler * fdRow, but one element at a time.
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]

    # Section 4: Make sure that IM is an inverse of A within the specified tolerance
    if check_matrix_equality(I,matrix_multiply(A,IM),tol):
        return IM
    else:
        raise ArithmeticError("Matrix inverse out of tolerance.")