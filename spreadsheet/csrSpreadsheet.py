from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell
from test import create_random_cells

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class CSRSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        self.col_array:list[int] = []
        self.val_array:list[float] = []
        #lets start by adding the first and last elements of the sum array (last element being the cumulative sum of all the elements)
        self.sum_array:list[float] = [0]

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

    def print_all_arrays(self):
        print("col:",self.col_array, self.col_array.__len__())
        print("val:",self.val_array, self.val_array.__len__())
        print("sum:",self.sum_array, self.sum_array.__len__())
        print()

    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        # print("unsorted list: [")
        # for x in lCells:
        #     print(x)
        # print("]\n")
        # self.mergeSort(lCells)
        # print("sorted list [")
        # for x in lCells:
        #     print(x)
        # print("]\n")
        cur_row = lCells[0].row
        cur_sum = lCells[0].val
        self.val_array.append(lCells[0].val)
        self.col_array.append(lCells[0].col)
        for x in range(1,lCells.__len__()):
            #we want to append lCells[x].col no matter what
            self.col_array.append(lCells[x].col)
            
            self.val_array.append(lCells[x].val)
            if cur_row != lCells[x].row:
                self.sum_array.append(self.sum_array[-1]+cur_sum)
                cur_sum =0
                cur_row = lCells[x].row
            cur_sum +=lCells[x].val
     
    def build_sum_array(self ):
        prev = self.col_array[0]
        sum_arr = []
        for x in self.col_array:
            if x < prev:
                sum_arr.append(x)
        pass
    
    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        try:
            self.sum_array.append(self.sum_array[-1])
            return True
        except:
            #something went wrong
            return False

    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        try:
            return True
        except:
            return False

    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True

    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or okFalse if not, e.g., colIndex is invalid.
        """
        if colIndex < self.colNum():
            if colIndex < -1:
                return False
            if colIndex != -1:
                if colIndex == 0:
                    #basically add 1 to each of the values in col_array as long as they aren't 0
                    try:
                        for x in self.col_array:
                            if x != 0:
                                x +=1
                        return True
                    except:
                        return False
                else:
                    #colIndex > 0
                    try:
                        #we can't simply do range(collindex, col_array.len()) because the columns are not in order because they differ in row
                        for x in self.col_array:
                            if x > colIndex:
                                x+=1
                        return True
                    except:
                        return False
            else:
                #since col index is the last index, it basically works the same as append col, append col has no visible changes to any of the arrays
                return True
        else:
            return False

    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        # TO BE IMPLEMENTED

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True

    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """
        num_rows = 0


        return self.sum_array.__len__()-1

    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        
        return max(self.col_array)+1

    def find(self, value: float) -> tuple[(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """

        # TO BE IMPLEMENTED

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return []

    def entries(self) -> list[Cell]:
        """
        return a list of cells that have values (i.e., all non None cells).
        """

        return []

    