from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell

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
        self.columns = 0

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
        print("val: [",end="")
        for x in self.val_array:
            print(x, end = " ")
        print("]",self.val_array.__len__())
        print(self.val_array.__len__())
        print("sum:",self.sum_array, self.sum_array.__len__())
        print()
    
    # def del_duplicates(self, arr:[Cell]):
    #     result = arr.copy() 
    #     checked = []
    #     for x in range(len(arr)):    
    #         for y in range(len(arr)):
    #             if arr[x].row == arr[y].row and arr[x].col == arr[y].col and x!=y:
    #                 if y not in checked and x not in checked:
    #                     checked.append(y)
    #                     result.__delitem__(x)        
    #         checked.append(x)
    #     return result



    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        # print("unsorted list: [")
        # for x in lCells:
        #     print(x)
        # print("]\n")
        # self.del_duplicates(lCells)
        lCells = set(lCells)
        lCells = list(lCells)
        self.mergeSort(lCells)
        print("sorted list [")
        for x in lCells:
            print(x)
        print("]\n")
        cur_row = 0
        cur_sum = lCells[0].val
        self.val_array.append(lCells[0].val)
        self.col_array.append(lCells[0].col)
        if lCells[0].row > 0:
            counter = lCells[0].row-1
            while counter > 0:
                self.appendRow()
                counter -=1
        for x in range(1,lCells.__len__()):
            #we want to append lCells[x].col no matter what
            self.col_array.append(lCells[x].col)
            self.val_array.append(lCells[x].val)
            if cur_row != lCells[x].row:

                self.sum_array.append(self.sum_array[-1]+cur_sum)
                cur_sum =0

                if lCells[x].row-cur_row > 1:
                    
                    counter = lCells[x].row -  cur_row
                    while counter > 1:
                        self.appendRow()
                        counter -=1
                cur_row = lCells[x].row
            cur_sum +=lCells[x].val
        self.sum_array.append(self.sum_array[-1]+cur_sum)
        self.columns = max(self.col_array)+1
    
    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        try:
            #since there won't be any values in the final row, we can just restate the previous value of sum_array as that will still be the cumulative sum up to the new 
            #row
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
            #just increment the self.columns attribute to increase number of columns
            self.columns += 1   
            return True
        except:
            return False

    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """

        if rowIndex < self.rowNum():
            if rowIndex < -1:
                return False
            elif rowIndex == -1:
                self.sum_array.append(self.sum_array[-1])
                return True
            elif rowIndex == 0:
                self.sum_array.insert(0, 1)
                return True
            else:
                self.sum_array.insert(rowIndex, self.sum_array[rowIndex-1])
                return True
        else:
            return False

    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or okFalse if not, e.g., colIndex is invalid.
        """
        if colIndex < self.columns:
            if colIndex < -1:
                return False
            if colIndex != -1:
                if colIndex == 0:
                    #basically add 1 to each of the values in col_array as long as they aren't 0
                    try:
                        for x in self.col_array:
                            if x != 0:
                                x +=1
                        self.columns +=1
                        return True
                    except:
                        return False
                else:
                    #colIndex > 0
                    try:
                        for x in range(self.col_array.__len__()):
                            if self.col_array[x] > colIndex:
                                self.col_array[x]+=1
                        self.columns +=1
                        return True
                    except:
                        return False
            else:
                self.columns +=1
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

        #to go to a particular column and a row and then update the value there
        #we have some row and we have some column
        #[-,2,-]
        #[-,3,-]
        #[-,4,-]
        if rowIndex > self.rowNum() or colIndex > self.columns:
            return False
        else:
            row_counter = 0
            value_counter = 0
            cur_sum = 0
            prev_sum = self.sum_array[0]
            #while loop for getting to the correct row
            print("got here")
            while row_counter <= rowIndex:
                if prev_sum == self.sum_array[row_counter]:
                    while prev_sum == self.sum_array[row_counter] and row_counter < self.rowNum():
                        row_counter +=1
                 
                    prev_sum = self.sum_array[row_counter]
                if cur_sum == self.sum_array[row_counter]:
                    row_counter +=1
                    cur_sum = 0
                if row_counter >= rowIndex:
                    break
                print("rc",row_counter,"cs",cur_sum, "vc",value_counter)
                cur_sum += self.val_array[value_counter]
                value_counter+=1
            difference = self.val_array[value_counter] - value
            self.val_array[value_counter]= value
            self.sum_array[row_counter] +=difference
            return True

    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """

        return self.sum_array.__len__()-1

    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        return self.columns

    def find(self, value: float) -> tuple[(int, int)]:  
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
        """
        #for this we just have to go through the values array as that contains all the cells 

        ret = []
        cur_sum = 0
        row_counter = 0
        prev_sum  = self.sum_array[0]
        for x in range(0, self.val_array.__len__()):
            if self.sum_array[row_counter] == prev_sum:
                row_counter +=1
                while self.sum_array[row_counter] == prev_sum:
                    
                    row_counter +=1
                prev_sum = self.sum_array[row_counter]
            if self.sum_array[row_counter] == cur_sum:
                cur_sum = 0
                prev_sum = self.sum_array[row_counter]
                row_counter +=1
                
            c = Cell(row_counter, self.col_array[x], self.val_array[x])
            cur_sum += self.val_array[x]
            if self.val_array[x] == value:
                ret.append((row_counter, self.col_array[x]))
        return ret

    def entries(self) -> [Cell]:
        """
        return a list of cells that have values (i.e., all non None cells).
        """
        #for this we just have to go through the values array as that contains only non-None Cells
        ret = []
        cur_sum = 0
        row_counter = 0
        prev_sum  = self.sum_array[0]
        for x in range(0, self.val_array.__len__()):
            if self.sum_array[row_counter] == prev_sum:
                while self.sum_array[row_counter] == prev_sum and row_counter < self.rowNum():
                    row_counter +=1
                prev_sum = self.sum_array[row_counter]
            if self.sum_array[row_counter] == cur_sum:
                cur_sum = 0
                prev_sum = self.sum_array[row_counter]
                row_counter +=1
            c = Cell(row_counter, self.col_array[x], self.val_array[x])
            cur_sum += self.val_array[x]
            ret.append(c)

        return ret

    
