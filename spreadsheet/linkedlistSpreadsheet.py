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

    def populate(self, row, amount, val):
        self.head = ListNode(Cell(row,0,val))
        head = self.head
        for x in range(1, amount):
            head.next = ListNode(Cell(row, x, val))
            head.next.prev = head
            head = head.next
        self.tail = head
    def display_linked_list(self):
        #ss = linkedlist dimension 1
        head = self.head
        i = 0
        while head.next != None:
            print(head.val)
            head = head.next
        print(self.tail.val)

class LinkedListSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        numRows = 5
        numCols = 5
        self.head = linkedList()
        self.head.populate(0, numCols, None)
        self.tail = self.head
        head = self.head
        # for row in range(numRows):
        #     curRow.head = ListNode(Cell(row,0,0))
        #     curCell = curRow.head
        #     for col in range(1,numCols):
        #         curCell.next = ListNode(Cell(row,col,0))
        #         curCell.next.prev = curCell
        #         curCell = curCell.next
        #     curRow.tail = curCell
        #     if row != numRows-1:
        #         curRow.next = linkedList()
        #         curRow.next.prev = curRow
        #         curRow = curRow.next
        row_counter = 1
        while numRows > 0:
            new_row = linkedList()
            new_row.populate(row_counter, numCols, None)
            head.next = new_row
            head = head.next
            row_counter +=1
            numRows -=1

        self.tail = head
            
    def buildSpreadsheet(self, lCells: list[Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        try:
            for x in lCells:
                lx = ListNode(x)
                row_counter = lx.val.row

                head = self.head
                while row_counter > 0 and head.next !=None:
                    head = head.next
                    row_counter -=1
                if row_counter > 0 and head.next ==None:
                    append_row = row_counter
                    while append_row > 0:
                        self.appendRow()
                        append_row -=1
                    while row_counter >0:
                        head = head.next
                        row_counter -=1
                #do the same thing we did with rows, to col
                col = head.head
                col_counter = lx.val.col
                while col_counter > 0 and col.next !=None:
                    col = col.next
                    col_counter -=1
                
                if col_counter >0 and col.next == None:
                    append_col = col_counter
                    while append_col > 0:
                        self.appendCol()
                        append_col -=1
                    while col_counter > 0:
                        col = col.next
                        col_counter -=1
                #we are now at the correct location to insert the node
                col.val = lx.val
        except:
            print("something went wrong")
    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.
        """ 
        try:
            rows = self.rowNum()
            cols = self.colNum()
            new_tail:linkedList = linkedList()
            new_tail.populate(rows,cols, None)
            self.tail.next = new_tail
            new_tail.prev = self.tail
            self.tail = new_tail
            return True
        except:
            return False

    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        try:
            colNum =  self.colNum()
            rowNum = self.rowNum()
            curRow = self.head
            count = 0
            while(curRow.next != None):
                curCell = curRow.tail
                curCell.next = ListNode(Cell(count,colNum,None))
                curCell.next.prev = curCell
                curRow.tail = curCell.next
                curRow = curRow.next
                count +=1
            curCell = curRow.tail
            curCell.next = ListNode(Cell(count,colNum,None))
            curCell.next.prev = curCell
            curRow.tail = curCell.next
            curRow = curRow.next
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
            if rowIndex >=0:
                if rowIndex == 0:
                    head = self.head
                    new_row = linkedList()
                    new_row.populate(0, self.colNum(),None)
                    
                    head.prev = new_row
                    
                    new_row.next = head
                    self.head = new_row
                elif rowIndex > 0:
                    row_counter = rowIndex-1
                    #head is a row
                    head = self.head
                    while row_counter > 0 and head.next != None:
                        #get to the correct row
                        head = head.next
                        row_counter -=1
                    if row_counter > 0 and head.next == None:
                        #there weren't enough rows to which the user could insert the row where they wanted
                        return False
                    
                    else:
                        #we are at the correct row where we want to insert  
                        #prev is the previous row and next is the next row, we want to insert a row in between them
                        # next:linkedList = head.next
                        
                        #create the new row
                        new_row = linkedList()
                        #populate the new row
                        new_row.populate(rowIndex,self.colNum(), None)
                        #previous and next rows
                        prev = head
                        next = prev.next
                        #change the existing links to include the new row
                        prev.next  = new_row
                        next.prev = new_row
                        #set the correct links for the new row   
                        new_row.prev = prev
                        new_row.next = next
                #we now need to change the row values of all other cells
                #row
                head = self.head
                #counter we want to go back to the rowindex+1 and start changing row values from there
                counter = rowIndex+1
                #go to the correct row
                while counter > 0:
                    head = head.next
                    counter -=1
                #at the correct row, now start incrementing the row values for all cells after the current row
                while head.next !=None:
                    head_node = head.head
                    while head_node.next !=None:
                        head_node.val.row +=1
                        head_node= head_node.next    
                    head_node.val.row +=1
                    head = head.next
                tail = self.tail.head
                #the tail does not get incremented so it's own while loop is made
                while tail.next !=None:
                    tail.val.row +=1
                    tail = tail.next
                #again the tail of the tail row is not incremented so we can simply do this:
                self.tail.tail.val.row +=1
            elif rowIndex == -1:
                #we want to change the tail
                tail = self.tail
                new_row = linkedList()
                new_row.populate(self.rowNum(), self.colNum(),None)
                
                tail.next = new_row
                new_row.prev = tail
                self.tail = new_row
            else:
                return False
        else:
            return False
  
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
                        curCell.next = ListNode(Cell(row_counter,colIndex,None ))
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
            return True
        except: 
            return False

    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """
        head:linkedList = self.head
        counter = 0
        while head.next != None:
            counter+=1
            head = head.next
        if head.head.val != None:
            counter +=1
        return counter
        # return self.tail.tail.val.row + 1 

    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        curCell = self.head.head
        counter = 0
        while curCell.next !=None:
            counter+=1
            curCell = curCell.next
        if curCell.val != None:
            counter +=1
        return counter
        # return self.tail.tail.val.col +1

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
                cell = cell.next
            head = head.next
        #head is currently the tail
        tail = head.head
        while tail.next !=None:
            if tail.val.val == value:
                ret.append((tail.val.row,cell.val.row))
            tail = tail.next
        # REPLACE WITH APPROPRIATE RETURN VALUE
        if self.tail.tail.val.val == value:
            ret.append((self.tail.tail.val.row, self.tail.tail.val.col))
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
                cell = cell.next
            head = head.next
        tail = head
        while tail.head.next != None:
            if tail.head.val.val !=None:
                ret.append(tail.head.val)
            tail.head = tail.head.next
        if tail.tail.val.val !=None:
            ret.append(tail.tail.val)
        return ret
