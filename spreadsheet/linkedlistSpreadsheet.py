from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell


class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, val:Cell = None):
        self.prev = None
        self.val = val
        self.next = None


# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED 
# Linked-List-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------



class linkedList:

    def __init__(self, head:ListNode = None, tail:ListNode = None, next = None, prev= None ):
        self.head = head
        self.prev = prev
        self.next = next
        self.tail = tail
    

class LinkedListSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        numRows = 5
        numCols = 5
        self.head = linkedList()
        self.tail = self.head
        curRow = self.head
        for row in range(numRows):
            curRow.head = ListNode(Cell(row,0,0))
            curCell = curRow.head
            for col in range(1,numCols):
                curCell.next = ListNode(Cell(row,col,0))
                curCell.next.prev = curCell
                curCell = curCell.next
            curRow.tail = curCell
            if row != numRows-1:
                curRow.next = linkedList()
                curRow.next.prev = curRow
                curRow = curRow.next
        self.tail = curRow


            
    def buildSpreadsheet(self, lCells: list[Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        for x in lCells:
            lnx:ListNode = ListNode(x)
            row_counter = lnx.val.row
            row = self.head
            #get to the correct row
            while row.next != None and row_counter > 0:
                row = row.next
                row_counter -= 1
            if row.next == None  and row_counter > 0:
                while row_counter > 0:
                    self.appendRow()
                    row = row.next
                    row_counter -=1

            column_counter = lnx.val.col
            column = row.head
            #get to the correct column
            while column.next!= None and column_counter > 0:
                column = column.next
                column_counter -=1
            if column.next == None and column_counter > 0:
                
                while row_counter > 0:
                    self.appendCol()
                    column = column.next
                    column_counter -=1
            #               x
            # [col1, prev, next, col4]
            prev:ListNode = column.prev
            next:ListNode = column.next
            #lnx has next and prev attributes as None, set them to the correct values
            lnx.prev = prev
            lnx.next = next
            #previous has its next attribute as Next, but we want lnx
            prev.next = lnx
            #next has its prev attribute as Prev, but we want lnx
            if next!= None:
                next.prev = lnx

    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.
        """ 
        rowNum = self.rowNum()
        colNum = self.colNum()
        self.tail.next = linkedList()
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        curRow = self.tail
        count =0
        curRow.head = ListNode(Cell(rowNum,0,count))
        
        curCell = curRow.head
        for y in range(1,colNum):
            curCell.next = ListNode(Cell(rowNum,y,count))
            curCell.next.prev = curCell
            
            curCell = curCell.next
            curRow.tail = curCell
        self.tail = curRow



    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        colNum =  self.colNum()
        rowNum = self.rowNum()
        curRow = self.head
        count = 0
        while(curRow.next != None):
            curCell = curRow.tail
            curCell.next = ListNode(Cell(count,colNum,0))
            curCell.next.prev = curCell
            curRow.tail = curCell.next
            curRow = curRow.next
            count +=1

        curCell = curRow.tail
        curCell.next = ListNode(Cell(count,colNum,0))
        curCell.next.prev = curCell
        curRow.tail = curCell.next

    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        if rowIndex > self.rowNum():
            return False
        elif rowIndex > 0:
            counter = rowIndex
            head = self.head
            while(head.next != None and counter >0 ):
                head = head.next
                counter-=1
            prev:linkedList = head.prev
            next:linkedList = head.next
            row:linkedList = linkedList()            
            #set the proper links to next and previous lists
            row.next = next
            row.prev = prev
            #make it so that the new row fits into the middle of the prev and next lists
            prev.next = row
            next.prev = row
        elif rowIndex == 0:
            row:linkedList = linkedList()
            row.next = self.head
            self.head = row
        elif rowIndex == -1:
            row: linkedList = linkedList()
            row.prev = self.tail
            self.tail = row
        return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be before the newly inserted row.  If inserting as first column, specify colIndex to be -1.
        """
        if colIndex < self.colNum():
            curRow = self.head
            row_counter = 0
            while (curRow != None):
                curCell = curRow.head
                while(curCell!=None):
                    if (curCell.val.col == colIndex-1):
                        temp:ListNode = curCell.next
                        curCell.next = ListNode(Cell(row_counter,colIndex,0 ))
                        curCell.next.prev = curCell
                        curCell.next.next = temp
                        if temp != None:
                            temp.prev =  curCell.next
                        curCell.next.val.col = curCell.val.col+1
                    elif ((curCell.next != None) and (curCell.val.col >= colIndex)):
                        curCell.next.val.col = curCell.val.col+1
                    
                    curCell = curCell.next
                curRow = curRow.next
                row_counter +=1
        else:
            return False

        return True


    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """

        # TO BE IMPLEMENTED
        try:
            row_counter = rowIndex
            col_counter = colIndex
            row = self.head
            while row.next!= None and row_counter >0:
                row = row.next
                row_counter -=1
            if row.next == None and row_counter > 0:
                return False
            
            col:ListNode = row.head
            
            while col.next!= None and col_counter >0:
                col = col.next
                col_counter -=1
            if col.next == None and col_counter > 0:
                return False
            col.val.val = value
        except: 
            return False

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """
        # head:linkedList = self.head
        # counter = 0
        # while head.next != None:
        #     counter+=1
        #     head = head.next
        return self.tail.tail.val.row + 1 


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        # curCell = self.head.head
        # counter = 0
        # while curCell.next !=None:
        #     counter+=1
        #     curCell = curCell.next
        return self.tail.tail.val.col +1

        # TO BE IMPLEMENTED



    def find(self, value: float) -> list[(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """
        ret = []
        head = self.head
        while head.next != None:
            cell = head.head
            while cell.next !=None:
                if cell.val.val == value:
                    ret.append((cell.val.row, cell.val.col))
                cell.next
            head.next

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return ret



    def entries(self) -> list[Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """
        ret = []
        head = self.head
        while head.next != None:
            cell = head.head
            while cell.next !=None:
                if cell.val.val !=None:
                    ret.append(cell.val)
                cell.next
            head.next

        return ret
