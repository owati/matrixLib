'''
    an extensive matrix module created by Owati Mofiyinfoluwa
'''

class Matrix:

    '''
        initialization function
    '''
    def __init__(self, rows=1, column=1, *args):

        self.rows = rows
        self.column = column
        self.data = []
        if not args:
            self.data = [[0 for j in range(self.column)] for i in range(0, self.rows)]
        else:
            
            for i in args:
                if type(i) != list and type(i) != tuple:
                    raise TypeError('can only accept lists or tuples')
                else:
                    if len(i) != self.column:
                        self.data = [[0 for j in range(self.column)] for i in range(self.rows)]
                        raise TypeError(f'list {i} doest match the matrix dimension')
                    else:
                        self.data.append(i)
            if len(args) < self.rows:
                for i in range(self.rows - len(args)):
                    self.data.append([0 for i in range(self.column)])
                    
                    
        self.presentRow = 0
        self.presentColumn = 0
        
    '''
        string representation
    '''
    def __str__(self):
        msg = ''
        for i in range(self.rows):
            rowString = ' --- ' + ( '--- ' * (self.column-1) ) + '\n'
            for j in self.data[i]:
                rowString += '| ' + str(j) + ' '
            rowString += '|\n'
            msg += rowString
        msg +=  ' --- ' + ( '--- ' * (self.column-1) ) + '\n'
        
        return msg
    
    
    '''
        to add two matrices
    '''
    def __add__(self, mat):
        if type(mat) == Matrix:
            if mat.column == self.column and mat.rows == self.rows:
                ans = Matrix(self.rows, self.column)
                for i in range(self.rows):
                    for j in range(self.column):
                        num = self.data[i][j] + mat.data[i][j]
                        ans.addElement(num, (i + 1), (j + 1))
                return ans
            else:
                print('these matices are not compatible')
        
        else:
            print(f'cannot add matrix and {type(mat)}')
            
    
    '''
        subtact two matices
    '''
    def __sub__(self, mat):
        if type(mat) == Matrix:
            if mat.column == self.column and mat.rows == self.rows:
                ans = Matrix(self.rows, self.column)
                for i in range(self.rows):
                    for j in range(self.column):
                        num = self.data[i][j] - mat.data[i][j]
                        ans.addElement(num, (i + 1), (j + 1))
                return ans
            else:
                print('these matices are not compatible')
        
        else:
            print(f'cannot subtract matrix and {type(mat)}')
            
            
    '''
        to multiply
    '''        
    def __mul__(self, val):
        if type(val) == int or type(val) == float:
                mat = Matrix(self.rows, self.column)
                for i in range(self.rows):
                    for j in range(self.column):
                        mat.addElement(self.data[i][j]*val, i+1, j+1)
                return mat
        elif type(val) == Matrix:
            if self.column == val.rows:
                mat = Matrix(self.rows, val.column)
                for i in range(mat.rows):
                    list1 = self.getMatrix(i+1, 1, col=self.column)
                    list1list = [list1.data[0][i] for i in range(list1.column)]
                    for j in range(mat.column):
                        list2 = val.getMatrix(1,j+1,row=self.column)
                        list2list = [list2.data[i][0] for i in range(list2.rows)]
                        
                        mat.addElement(self.addList(list1list, list2list), i+1, j+1)
                return mat
            else:
                raise TypeError('cannot multiply because matrices are not compatible')
        else:
            raise TypeError(f'cannot mutiply matrix and {type(val)}')
            
    def __rmul__(self, val):
        if type(val) == int or type(val) == float:
                mat = Matrix(self.rows, self.column)
                for i in range(self.rows):
                    for j in range(self.column):
                        mat.addElement(self.data[i][j]*val, i+1, j+1)
                return mat
        else:
            raise TypeError(f'cannot mutiply matrix and {type(val)}')
        
                    
        
    '''
        to add a specific element
    '''
    def addElement(self, num, row, col):
        if row <= 0 or row > self.rows or col <= 0 or col > self.column:
            print(f'ERROR:: there is no allocation for ({row}, {col}) in this matrix')
        else:
            self.data[row -1][col-1] = num
    
    '''
        to change an entire column
    '''
    def changeColumn(self, col, colNum):
        if len(col) != self.rows:
            print('ERROR:: columns not compatible with list')
        else:
            if colNum == 0 or colNum > self.column:
                print(f'ERROR:: {colNum} is not a valid col')
            else:
                for i in range(self.rows):
                    self.data[i][colNum - 1] = col[i]
    
    
    '''
        to change an entire row
    '''
    def changeRow(self, row, rowNum):
        if len(row) != self.column:
            print('ERROR:: row not compatible with list')
        else:
            if rowNum == 0 or rowNum > self.rows:
                print(f'ERROR:: {rowNum} is not a valid row')
            else:
                self.data[rowNum - 1] = row
                
    '''
        remove an entire row
    '''
    def remRow(self, rowNum=1):
        if self.rows == 1:
            raise ValueError('the matrix must have a least one row')
        else:
            if rowNum > self.rows:
                raise IndexError('the matrix does not contain a row of this number')
            else:
                mat = Matrix(self.rows-1, self.column)
                i = 0
                found = False
                while i < self.rows:
                    if i == (rowNum - 1):
                        i += 1
                        found = True
                    else:
                        if found:
                            mat.changeRow(self.data[i], i)
                        else:
                            mat.changeRow(self.data[i], i+1)
                        i += 1
                return mat
    
    '''
        to remove an entire column
    '''
    def remColumn(self, colNum=1):
        if self.column == 1:
            raise ValueError('the matrix must have a least one column')
        else:
            if colNum > self.column:
                raise IndexError('the matrix does not contain a row of this number')
            else:
                mat = Matrix(self.rows, self.column - 1)
                i = 0
                found = False
                while i < self.column:
                    if i == (colNum - 1):
                        i += 1
                        found = True
                    else:
                        if found:
                            for j in range(self.rows):
                                mat.addElement(self.data[j][i], j+1, i)
                        else:
                            for j in range(self.rows):
                                mat.addElement(self.data[j][i], j+1, i+1)
                        i += 1
                return mat
     
    '''
        to interchange two rows
    '''
    def interRow(self, row1, row2):
        if row1 in range(1, self.rows + 1) and row2 in range(1, self.rows+1):
            mat = Matrix(self.rows, self.column)
            for i in range(self.rows):
                if i == (row1 - 1):
                    mat.changeRow(self.data[row2 - 1],i+1)
                elif i == (row2 - 1):
                    mat.changeRow(self.data[row1 - 1], i+1)
                    
                else:
                    mat.changeRow(self.data[i], i+1)
            return mat
        else:
            raise IndexError('one or two of these rows doesnt exist in  the matrix')
    
    
    '''
        to interchange two columns
    '''
    def interColumn(self, col1, col2):
        if col1 in range(1, self.column + 1) and col2 in range(1, self.column + 1):
            mat = Matrix(self.rows, self.column)
            for i in range(self.column):
                if i == (col1 - 1):
                    for j in range(self.rows):
                        mat.addElement(self.data[j][col2 - 1], j+1, i+1)
                elif i == (col2 - 1):
                    for j in range(self.rows):
                        mat.addElement(self.data[j][col1 - 1], j+1, i+1)
                else:
                    for j in range(self.rows):
                        mat.addElement(self.data[j][i], j+1, i+1)
                        
            return mat
        else:
            raise IndexError('one or two of these columns doesnt exist in  the matrix')
                        
    '''
        to shift the matix up along the rows
    '''
    def rowShiftUp(self, num=1):
        mat = self
        for i in range(num):
            for j in range(self.rows - 1):
                mat = mat.interRow(j+1,j+2 )
        return mat
    
    '''
        to shift the matrix down along the rows
    '''
    def rowShiftDown(self, num=1):
        mat = self
        for i in range(num):
            for j in range(self.rows - 1):
                mat = mat.interRow(self.rows - j, self.rows - j -1)
        return mat
    
    
    '''
        to shift a column left along the column
    '''
    def columnShiftLeft(self, num=1):
        mat = self
        for i in range(num):
            for j in range(self.column -1):
                mat = mat.interColumn(j+1,j+2)
        return mat
    
    
    '''
        to shift the matrix down along the rows
    '''
    def columnShiftRight(self, num=1):
        mat = self
        for i in range(num):
            for j in range(self.column - 1):
                mat = mat.interColumn(self.column - j, self.column - j -1)
        return mat
            
    
    '''
        to select an element
    '''
    def getElement(self, m, n):
        return self.data[m - 1][n - 1]
    
    
    '''
        to select a matrix from a matrix
    '''
    def getMatrix(self, m, n, row=1, col=1):
        mat = Matrix(row, col)
        for i in range(m, m+row):
            newList = []
            for j in range(n, n+col):
                newList.append(self.data[i-1][j-1])
            mat.changeRow(newList, i - m + 1)
        
        return mat


    '''
        to show the matrix in a grid format
    '''     
    def show(self):        
        print(self)
        
        
    @staticmethod
    def addList(a, b):
        num = 0
        for i in range(len(a)):
            num += a[i]*b[i]
        return num
    
    @staticmethod
    def IDENTITY(num):
        mat = Matrix(num, num)
        for i in range(num):
            mat.addElement(1, i+1, i+1)
        return mat
