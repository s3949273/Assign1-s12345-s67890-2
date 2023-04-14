from spreadsheet.cell import Cell
import random
from spreadsheet.arraySpreadsheet import ArraySpreadsheet
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

def print_entries(ss:LinkedListSpreadsheet):
    a = ss.entries()
    for x in a:
        print(x, end=" ")
    print()

def create_random_cells(num_cells: int) -> list[Cell]:
    cells = []
    for i in range(num_cells):
        row = random.randint(1, 100)
        col = random.randint(1, 100)
        val = random.randint(1,9)
        cell = Cell(row, col, val)
        cells.append(cell)
    return cells



if __name__ == "__main__":
    ss = CSRSpreadsheet()
    ss.buildSpreadsheet(create_random_cells(2500))






    # test_elems = [
    #     Cell(9, 9, 2.0),
    #     Cell(2, 5, 7),
    #     Cell(3, 1, 6),
    #     Cell(8, 5, -6.7),
    # ]

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
