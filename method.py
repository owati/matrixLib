
'''
    matrix methods
'''
from .matrix import Matrix


def diagDiff(mat):
    num1 = num2 = 1
    for i in range(mat.column):
        num1 *= mat.data[i][i]
        num2 *= mat.data[i][mat.column - 1 - i]
    return num1 - num2


'''
    finding the determinant of a matix
'''
def det(mat):
    if type(mat) != Matrix:
        raise TypeError('this is not of type matix')
    else:
        if mat.rows != mat.column:
            raise ValueError('cannot find the determinant of a non square matrix')
        else:
            if mat.column == 2:
                return diagDiff(mat)
            ans = diagDiff(mat)
            for i in range(1, mat.column):
                ans += diagDiff(mat.columnShiftLeft(i))
            return ans

'''
    to find the minor of an elemnt
'''
def minor(mat,coord):
    if type(mat) != Matrix:
        raise TypeError('this is not of type matix')
    elif type(coord) != tuple and type(coord) != list:
        raise TypeError(f'{coord} is not of type list o tuple')
    else:
        mat2 = mat.remRow(coord[0])
        mat2 = mat2.remColumn(coord[1])
        return mat2

'''
    to find the cofactor of the matix
'''
def cofactor(mat,coord):
    if type(mat) != Matrix:
        raise TypeError('this is not of type matix')
    elif type(coord) != tuple and type(coord) != list:
        raise TypeError(f'{coord} is not of type list o tuple')
    else:
        return det(minor(mat,coord))
    
'''
    to find the transpose of the matrix
'''
def transpose(mat):
    if type(mat) != Matrix:
        raise TypeError('this is not of type matrix')
    else:
        mat2 = Matrix(mat.column, mat.rows)
        for i in range(mat2.rows):
            for j in range(mat2.column):
                mat2.addElement(mat.data[j][i], i+1, j+1)
        return mat2

'''
    to find the adjoint of a matix
'''
def adjoint(mat):
    if type(mat) != Matrix:
        raise TypeError('this is not of type matrix')
    else:
        mat2 = Matrix(mat.rows, mat.column)
        for i in range(mat.rows):
            for j in range(mat.column):
                mat2.addElement(cofactor(mat,(i+1, j+1)), i+1, j+1)
        return transpose(mat2)

'''
    to find the inverse of the matrix
'''
def inverse(mat):
    if type(mat) != Matrix:
        raise TypeError('this is not of type matrix')
    else:
        return (1/det(mat)) * adjoint(mat)