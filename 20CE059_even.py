# Create the class
class Matrix:

    # create getRow function it takes number of rows in matrix
    def getRow(self):
        self.row = int(input("Enter the number of row : "))

    # create getColumn function it takes number of column in matrix
    def getColumn(self):
        self.col = int(input("Enter the number of column : ")) 
   
    # takes input from the user and create the matrix
    def setElement(self):
        self.arr = []       # create the empty array for storing the entire matrix
        for x in range(self.row):
            col=[]      # create the empty array for storing the column value 
            for y in range(self.col):
                print("Enter the val at",x,y,":",end=" ")
                self.num = int(input())
                col.append(self.num)        # store the input 
            self.arr.append(col)  

        print("****matrix****")  
        print(self.arr)


    def addition(self,obj1,obj2):
        # add exception when both the marices does not matches the row and column
        try:        
            if obj1.row == obj2.row and obj1.col == obj2.col:                
                total_row = obj1.row        
                total_col = obj1.col

                self.newArr = []
                for x in range(total_row):
                    newcol=[]
                    for y in range(total_col):
                        newNum = obj1.arr[x][y] + obj2.arr[x][y]
                        newcol.append(newNum)        
                    self.newArr.append(newcol)
                
                print("Addition of two matrix")
                print(self.newArr)
            else:
                raise Exception
        except Exception:
            print("Addition is not occured because both matrices row and column does not matches")

    # transpose the matrix
    def transpose(self):
        self.transposeMatrix = []
        for x in range(self.col):
            c = []
            for y in range(self.row):
                newEle = self.arr[y][x]
                c.append(newEle)
            self.transposeMatrix.append(c)

        print("****Transpose Matrix****") 
        print(self.transposeMatrix)

# create the object
m = Matrix()    
m.getRow()
m.getColumn()
m.setElement()
m.transpose()

m1 = Matrix()
m1.getRow()
m1.getColumn()
m1.setElement()
m1.transpose()

m2 = Matrix()
m2.addition(m,m1)