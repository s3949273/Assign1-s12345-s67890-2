from spreadsheet.cell import Cell
from spreadsheet.baseSpreadsheet import BaseSpreadsheet


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class ArraySpreadsheet(BaseSpreadsheet):

    def __init__(self):
        #2D array ROW(Column(Cell))
        #Cell(row, column, val)
        #[                          ,                         ,                         ]
        #  [Cell(), Cell(), Cell()]   [Cell(), Cell(), Cell()] [Cell(), Cell(), Cell()]
            #Cell has attributes row, column and value
        
        
        self.array = []
        #initalise the array to be of size 10x 10
        self.rowsize, self.columnsize = 10,10
        for row in range(self.rowsize):
            temp_array = []
            for column in range(self.columnsize):
                temp_array.append(Cell(row,column, None))
            self.array.append(temp_array)
        

    def buildSpreadsheet(self, lCells: list[Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """

        for element in lCells:
            row = element.row
            col = element.col
            if self.rowNum() < row:
                while self.rowNum() < row:
                    self.appendRow()
                    self.appendCol()
            if self.colNum() < col:
                while self.colNum() < col:
                    self.appendCol()
                    self.appendRow()
            try:
                self.array[row][col] = Cell(row,col,element.val)
            except:
                return False

    def appendRow(self)->bool:
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        try:
            self.array.append([Cell(self.rowNum(), _, None) for _ in range(0, self.colNum()+1)])
            return True
        except:
            print("something went wrong")
            return False        


    def appendCol(self)->bool:
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        
        try:
            #columns[rows], column1[row1, row2], column2,  
            col = self.colNum()+1
            for row in range(0, self.rowNum()+1):
                self.array[row].append(Cell(row,col, None))
        except:
            print("something went wrong")
            return False

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        #complete
        if rowIndex > self.rowNum():
            return False
        if (rowIndex == -1):
            rowIndex = self.rowNum() - rowIndex -1
        elif(rowIndex < -1):
            return False
        try:
            self.array.insert(rowIndex,[Cell(rowIndex, _, None) for _ in range(0, self.colNum())])   
            for x in range(rowIndex,self.rowNum()):
                for cell in self.array[x]:
                    cell.row +=1
            return True   
        except:
            return False
        

    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """
        try:
            
            if colIndex > self.colNum():
                return False
            if (colIndex == -1):
                colIndex = self.colNum() - colIndex
            elif(colIndex < -1):
                print("you tried to insert a column out of the bounds")
                return False
            colSize = self.colNum() +1
            for row in range(self.rowNum()):
                self.array[row].insert(colIndex,Cell(row, colIndex-1,None))
                for column in range(colIndex,colSize):
                    self.array[row][column].col +=1
            return True
        except:
            return False
        # REPLACE WITH APPROPRIATE RETURN VALUE
            
    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """
        try:
            self.array[rowIndex][colIndex].val = value
            return True
        except:
            return False


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """
        # REPLACE WITH APPROPRIATE RETURN VALUE
        return len(self.array)-1


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return len(self.array[0])-1




    def find(self, value: float) -> list[(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        # TO BE IMPLE
        ret = []
        for row in range(0, self.rowNum()):
            for col in range(0, self.colNum()):
                if self.array[row][col].val == value:
                    ret.append((row,col))
        
        return ret

    def mergeSort(self,arr):
        # original reference: https://www.geeksforgeeks.org/merge-sort/
        # while we took the original reference from geeksforgeeks, we had to implement the part 
        # where it would check whether the columns were the same and if the rows needed to be changed
        if len(arr) > 1:

            # Finding the mid of the array
            mid = len(arr)//2

            # Dividing the array elements
            L = arr[:mid]

            # into 2 halves
            R = arr[mid:]

            # Sorting the first half
            self.mergeSort(L)

            # Sorting the second half
            self.mergeSort(R)

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i].row < R[j].row:
                    arr[k] = L[i]
                    i += 1
                elif L[i].row > R[j].row:
                    arr[k] = R[j]
                    j += 1
                else:
                    if L[i].col < R[j].col:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                k += 1

            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    def entries(self) -> list[Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """

        ret = []
        for y in range(0, self.array.__len__()):
            for x in range(0, self.array[y].__len__()):
                if self.array[x][y].val != None:
                    ret.append(self.array[x][y])
        self.mergeSort(ret)
        # TO BE IMPLEMENTED
        return ret
