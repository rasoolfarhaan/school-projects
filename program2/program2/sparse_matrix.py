# Submitter: frasool(Rasool, Farhaan)
# Partner  : Anudeeph(Hegde, Anudeep)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
import prompt
from pickle import FALSE, TRUE

class Sparse_Matrix:

    # I have written str(...) because it is used in the bsc.txt file and
    #   it is a bit subtle to get correct. This function does not depend
    #   on any other method in this class being written correctly, although
    #   it could be simplified by writing self[...] which calls __getitem__.   
    def __str__(self):
        size = str(self.rows)+'x'+str(self.cols)
        width = max(len(str(self.matrix.get((r,c),0))) for c in range(self.cols) for r in range(self.rows))
        return size+':['+('\n'+(2+len(size))*' ').join ('  '.join('{num: >{width}}'.format(num=self.matrix.get((r,c),0),width=width) for c in range(self.cols))\
                                                                                             for r in range(self.rows))+']'
    
    def __init__(self, rows, cols, *matrix):
        matrix1 = dict()
        if type(rows) != int or (rows < 1):
            raise AssertionError("Rows must only contain integers greater than 0")
        if type(cols) != int or (cols < 1):
            raise AssertionError("Columns must only contain integers greater than 0")

        for x in matrix:
            if x[2] != 0:
                matrix1[(x[0], x[1])] = x[2]

        uniquelist = []
        for x in matrix:
            set1 = (x[0], x[1])
            if set1 in uniquelist:
                raise AssertionError("There cannot be more than one value per row and column index")
            else:
                uniquelist.append(set1)

        for x in matrix:
            for y in x:
                if (type(y) != int) and (type(y) != float):
                    raise AssertionError("Matrix value must be int or float")

        for x in matrix:
            if ((x[0]) >= rows) or ((x[1]) >= cols):
                raise AssertionError

        self.matrix = matrix1
        self.rows = rows
        self.cols = cols
        
    def size(self):
        return (self.rows, self.cols)
    
    def __len__(self):
        return self.rows*self.cols
    
    def __bool__(self):
        if len(self.matrix) == 0:
            return False 
        else:
            return True 
    
    def __repr__(self):
        list1 =[]
        for a, b in self.matrix.items():
            list1.append((a[0], a[1], b))
        str1 = 'Sparse_Matrix(' + str(self.rows) + "," + str(self.cols) + ","
        for a in list1:
            str1 += str(a) + ","
        return str1[0:-1] + ")"
    
    def __getitem__(self, tup1):
        if type(tup1) != tuple:
            raise TypeError
        if len(tup1) != 2:
            raise TypeError
        for a in tup1:
            if type(a) != int:
                raise TypeError
            if a >= self.rows or a < 0 or a >= self.cols:
                raise TypeError
        return self.matrix.get(tup1, 0)
    
    def __setitem__(self, tup1, val):
        if type(tup1) != tuple:
            raise TypeError
        if len(tup1) != 2:
            raise TypeError
        for a in tup1:
            if type(a) != int:
                raise TypeError
            if a >= self.rows or a < 0 or a >= self.cols:
                raise TypeError
        if type(val) != int:
            raise TypeError
        if val == 0:
            if tup1 in self.matrix:
                del self.matrix[tup1]
        if val != 0:
            self.matrix[tup1] = val
            
    def __delitem__(self, tup1):
        if type(tup1) != tuple:
            raise TypeError
        if len(tup1) != 2:
            raise TypeError
        for a in tup1:
            if type(a) != int:
                raise TypeError
            if a >= self.rows or a < 0 or a >= self.cols:
                raise TypeError
        if tup1 in self.matrix:
            del self.matrix[tup1]
            
    def row(self, int1):
        list1 = []
        if type(int1) != int:
            raise AssertionError
        if int1 < 0 or int1 > self.rows-1:
            raise AssertionError
        for b in range(0, self.cols):
            if (int1, b) in self.matrix:
                list1.append(self.matrix[(int1, b)])
            else:
                list1.append(0)
        return tuple(list1)
    
    def col(self, int1):
        list1 = []
        if type(int1) != int:
            raise AssertionError
        if int1 < 0 or int1 > self.cols-1:
            raise AssertionError
        for b in range(0, self.rows):
            if (b, int1) in self.matrix:
                list1.append(self.matrix[(b, int1)])
            else:
                list1.append(0)
        return tuple(list1)
    
    def details(self):
        str1 = ""
        str1 += str(self.rows) + "x" + str(self.cols) + " -> " + str(self.matrix) + " -> " + "("
        for a in range(0, self.rows):
            str1 += str(Sparse_Matrix.row(self, a)) + ", "
        return str1[0:-2] + ")"
    
    def __call__(self, int1, int2):
        dict1 = self.matrix.copy()
        if type(int1) != int:
            raise AssertionError
        if type(int2) != int:
            raise AssertionError
        if int1 < 0 or int2 < 0:
            raise AssertionError
        for a in range(0, self.rows):
            if (a, int2) in dict1:
                del dict1[(a, int2)]
        for a in range(0, self.cols):
            if (int1, a) in dict1:
                del dict1[(int1, a)]
        self.rows = int1
        self.cols = int2
        self.matrix = dict1
    
    def __iter__(self):
        lst = sorted(self.matrix, key = lambda x: self.matrix[x])

        for key in lst:
            yield (key[0], key[1], self.matrix[key])
    
    def __pos__(self):
        list1 = []
        for a in range(0, self.rows):
                for b in range (0,self.cols):
                    if (a,b) in self.matrix:
                        list1.append((a,b,self.matrix[(a,b)]))
                    else:
                        list1.append((a,b,0))
        return Sparse_Matrix(self.rows, self.cols, *list1)
    
    def __neg__(self):
        list1 = []
        for a in range(0, self.rows):
                for b in range (0,self.cols):
                    if (a,b) in self.matrix:
                        list1.append((a,b,-1*self.matrix[(a,b)]))
                    else:
                        list1.append((a,b,0))
        for a in list1:
            return Sparse_Matrix(self.rows, self.cols, *list1)
        
    def __abs__(self):
        list1 = []
        for a in range(0, self.rows):
                for b in range (0,self.cols):
                    if (a,b) in self.matrix:
                        list1.append((a,b,abs(self.matrix[(a,b)])))
                    else:
                        list1.append((a,b,0))
        for a in list1:
            return Sparse_Matrix(self.rows, self.cols, *list1)
    
    def __add__(self, right):
        if type(right) == int:
            list1 = []
            for a in range(0, self.rows):
                for b in range (0,self.cols):
                    if (a,b) in self.matrix:
                        list1.append((a,b,self.matrix[(a,b)]+right))
                    else:
                        list1.append((a,b,right))
            return Sparse_Matrix(self.rows, self.cols, *list1)
        
        if type(right) == Sparse_Matrix:
            list1 = []
            for a in range(0, self.rows):
                for b in range (0,self.cols):
                    if (a,b) in self.matrix:
                        if(a,b) in right.matrix:
                            list1.append((a,b,self.matrix[(a,b)]+right.matrix[(a,b)]))
                    else:
                        list1.append((a,b,0))
            return Sparse_Matrix(self.rows, self.cols, *list1)
        
        else:
            raise TypeError
    
    def __radd__(self, left):
        if type(left) == int:
            list1 = []
            for a in range(0, self.rows):
                for b in range (0,self.cols):
                    if (a,b) in self.matrix:
                        list1.append((a,b,self.matrix[(a,b)]+left))
                    else:
                        list1.append((a,b,left))
            return Sparse_Matrix(self.rows, self.cols, *list1)
        
        if type(left) == Sparse_Matrix:
            list1 = []
            for a in range(0, self.rows):
                for b in range (0,self.cols):
                    if (a,b) in self.matrix:
                        if(a,b) in left.matrix:
                            list1.append((a,b,self.matrix[(a,b)]+left.matrix[(a,b)]))
                    else:
                        list1.append((a,b,0))
            return Sparse_Matrix(self.rows, self.cols, *list1)
    
        else:
            raise TypeError
        
    def __sub__(self, right):
        if type(right) == int:
            list1 = []
            for a in range(0, self.rows):
                for b in range (0,self.cols):
                    if (a,b) in self.matrix:
                        list1.append((a,b,self.matrix[(a,b)]-right))
                    else:
                        list1.append((a,b,-1*right))
            return Sparse_Matrix(self.rows, self.cols, *list1)
        
        if type(right) == Sparse_Matrix:
            list1 = []
            for a in range(0, self.rows):
                for b in range (0,self.cols):
                    if (a,b) in self.matrix:
                        if(a,b) in right.matrix:
                            list1.append((a,b,self.matrix[(a,b)]-right.matrix[(a,b)]))
                    else:
                        list1.append((a,b,0))
            return Sparse_Matrix(self.rows, self.cols, *list1)
        
        else:
            raise TypeError

    def __rsub__(self, left):
        if type(left) == int:
            list1 = []
            for a in range(0, self.rows):
                for b in range (0,self.cols):
                    if (a,b) in self.matrix:
                        list1.append((a,b,left-self.matrix[(a,b)]))
                    else:
                        list1.append((a,b,-1*left))
            return Sparse_Matrix(self.rows, self.cols, *list1)
        
        if type(left) == Sparse_Matrix:
            list1 = []
            for a in range(0, self.rows):
                for b in range (0,self.cols):
                    if (a,b) in self.matrix:
                        if(a,b) in left.matrix:
                            list1.append((a,b,left.matrix[(a,b)]-self.matrix[(a,b)]))
                    else:
                        list1.append((a,b,0))
            return Sparse_Matrix(self.rows, self.cols, *list1)
    
        else:
            raise TypeError
        
    def __mul__(self, right):
        if type(right) == int:
            list1 = []
            for a in range(0, self.rows):
                for b in range (0,self.cols):
                    if (a,b) in self.matrix:
                        list1.append((a,b,self.matrix[(a,b)]*right))
                    else:
                        list1.append((a,b,0))
            return Sparse_Matrix(self.rows, self.cols, *list1)
        
        if type(right) == Sparse_Matrix:
            list1 = []
            for a in range(0, self.rows):
                for b in range (0,self.cols):
                    if (a,b) in self.matrix:
                        if(a,b) in right.matrix:
                            list1.append((a,b,self.matrix[(a,b)]*right.matrix[(a,b)]))
                    else:
                        list1.append((a,b,0))
            return Sparse_Matrix(self.rows, self.cols, *list1)
        
        else:
            raise TypeError

    def __rmul__(self, left):
        if type(left) == int:
            list1 = []
            for a in range(0, self.rows):
                for b in range (0,self.cols):
                    if (a,b) in self.matrix:
                        list1.append((a,b,self.matrix[(a,b)]*left))
                    else:
                        list1.append((a,b,0))
            return Sparse_Matrix(self.rows, self.cols, *list1)
        
        if type(left) == Sparse_Matrix:
            list1 = []
            for a in range(0, self.rows):
                for b in range (0,self.cols):
                    if (a,b) in self.matrix:
                        if(a,b) in left.matrix:
                            list1.append((a,b,left.matrix[(a,b)]*self.matrix[(a,b)]))
                    else:
                        list1.append((a,b,0))
            return Sparse_Matrix(self.rows, self.cols, *list1)
    
        else:
            raise TypeError
        
    def __pow__(self, right):
        if type(right) == int:
            if right <= 0:
                raise AssertionError
            list1 = []
            for a in range(0, self.rows):
                for b in range (0,self.cols):
                    if (a,b) in self.matrix:
                        list1.append((a,b,self.matrix[(a,b)]**right))
                    else:
                        list1.append((a,b,0))
            return Sparse_Matrix(self.rows, self.cols, *list1)
        else:
            raise TypeError
        
    def __eq__(self, right):
        if type(right) == Sparse_Matrix:
            if self.matrix == right.matrix:
                return True 
            else:
                return False
        else:
            return False
        
        if type(right) == int:
            set1 = set()
            for a, b in self.matrix.items():
                if b == right:
                    set1.add(b)
            if len(set1) == 1:
                for a in set1:
                    if a == right:
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False
        
    def __neq__(self, right):
        if type(right) == Sparse_Matrix:
            if self.matrix != right.matrix:
                return True
            else:
                return False
        else:
            return True

if __name__ == '__main__':
    
    #Simple tests before running driver
    #Put your own test code here to test Sparse_Matrix before doing the bsc tests
    #Debugging problems with these tests is simpler

    # print('Printing')
    # m = Sparse_Matrix(3,3, (0,0,1),(1,1,3),(2,2,1))
    # print(m)
    # print(repr(m))
    # print(m.details())
    #
    # print('\nlen and size')
    # print(len(m), m.size(),)
    #
    # print('\ngetitem and setitem')
    # print(m[1,1])
    # m[1,1] = 0
    # m[0,1] = 2
    # print(m.details())
    #
    # print('\niterator')
    # for r,c,v in m:
    #     print((r,c),v)
    #
    # print('\nm, m+m, m+1, m==m, m==1')
    # print(m)
    # print(m+m)
    # print(m+1)
    # print(m==m)
    # print(m==1)
    # print()
    
    import driver
    driver.default_file_name = 'bscp22W22.txt'
#     driver.default_show_exception = prompt.for_bool('Show exceptions when testing',True)
#     driver.default_show_exception_message = prompt.for_bool('Show exception messages when testing',True)
#     driver.default_show_traceback = prompt.for_bool('Show traceback when testing',True)
    driver.driver()
