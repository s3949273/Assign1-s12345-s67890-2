from spreadsheet.cell import Cell
import random
from spreadsheet.arraySpreadsheet import ArraySpreadsheet
from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.csrSpreadsheet import CSRSpreadsheet
from spreadsheet.linkedlistSpreadsheet import LinkedListSpreadsheet, linkedList, ListNode

def display_array(array: ArraySpreadsheet):
    arr =array.array 
    for x in arr:
        for y in x:
            if(y.val == None):
                print("("+str(y.row),str(y.col)+" N)", end = " ")
            else:
                print(y, end = " ")
        print() #newline
    print("finished")

def create_random_cells(num_cells: int, max_row:int, max_col:int) -> list[Cell]:
    """
        @params
        num_cells: the number of cells you want generated
        max_row: the abosulte value of the maximum row you want, not index, e.g.: if you want 25 rows, max_row will be 25 (not 24 as it would be for an index)
        max_col: the abosulte value of the maximum col you want, not index, e.g.: if you want 25 rows, max_col will be 25 (not 24 as it would be for an index)

    """
    cells = []
    cells.append(Cell(max_row-1,max_col-1,round(random.uniform(0.1,9.9), ndigits=2)))
    for i in range(num_cells-1):
        row = random.randint(0, max_row-1)
        col = random.randint(0, max_col-1)
        val = round(random.uniform(0.1,9.9), ndigits=2)
        cell = Cell(row, col, val)
        cells.append(cell)
    
    return cells

def display_linked_list(ss:LinkedListSpreadsheet ):
    #ss = linkedlist dimension 1
    cur_row = ss.head
    while cur_row != None:
        head = cur_row.head
        while head!= None:
            if head.val.val == None:
                print("(",head.val.row,head.val.col,", N)", end=" ")
            else:
                print(head.val,end=" ")
            head = head.next
        print("")
        cur_row = cur_row.next
    # tail_head = ss.tail.head
    # while tail_head.next != None:
    #     if(tail_head.val.val == None):
    #         print("(",tail_head.val.row,tail_head.val.col,", N)", end=" ")
    #     else:
    #         print(tail_head.val,end=" ")
    #     tail_head = tail_head.next
    print(ss.head.tail.val.col)
    print("colNum:",ss.colNum())
    
    print("rowNum:",ss.rowNum())

def print_entries(ss:BaseSpreadsheet):
    a = ss.entries()
    for x in a:
        print(x, end=" ")
    print()


if __name__ == "__main__":
    ss = CSRSpreadsheet()
    test_elems = [
        Cell(9, 9, 2.0),
        Cell(2, 5, 7),
        Cell(3, 1, 6),
        Cell(8, 5, -6.7),
        Cell(14,5,2)
    ]
    # test = create_random_cells(10, 10,10)
    ss.buildSpreadsheet(test_elems)
    # ss.print_all_arrays()
    print_entries(ss)
    # print_entries(ss)
    # test =list(set(test_elems))
    # for x in test:
    #     print(x)
    # print(ss.appendRow()) #true
    # print(ss.appendCol()) #true
    # print(ss.find(6.0)) # Printing output of find(6.0): (3,1)
    # print(ss.find(-6.0)) # Printing output of find(-6.0): 
    # print(ss.find(-6.7)) #Printing output of find(-6.7): (8,5)
    # print(ss.rowNum()) # Number of rows = 11
    # print(ss.colNum()) # Number of columns = 11
    # print(ss.update(2,5,-1.0)) # Call to update(2,5,-1.0) returned success.
    # print(ss.update(10,10,1.0)) # Call to update(10,10,1.0) returned success.
    # print(ss.update(11,11,2.5)) # Call to update(11,11,2.5) returned failure.
    # print(ss.rowNum())# Printing output of entries(): (2,5,-1.00) | (3,1,6.00) | (8,5,-6.70) | (9,9,2.00) | (10,10,1.00)
    # print(ss.colNum())# Call to insertRow(1) returned success.
    # print_entries(ss)# Call to insertCol(4) returned success.
    # print(ss.insertRow(1))# Call to insertRow(-2) returned failure.
    # print(ss.insertCol(4))# Number of rows = 12
    # print(ss.insertRow(-2))# Number of columns = 12
    # print(ss.colNum())# Number of rows = 12
    # print(ss.rowNum())# Number of columns = 12
    # print_entries(ss)#  Printing output of entries(): (3,6,-1.00) | (4,1,6.00) | (9,6,-6.70) | (10,10,2.00) | (11,11,1.00)
    # print(ss.update(2,5,-2.0))#Call to update(2,5,-2.0) returned success.
    # print_entries(ss)# Printing output of entries(): (2,5,-2.00) | (3,6,-1.00) | (4,1,6.00) | (9,6,-6.70) | (10,10,2.00) | (11,11,1.00)
