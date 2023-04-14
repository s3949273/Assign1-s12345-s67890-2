from spreadsheet.cell import Cell
from spreadsheet.linkedlistSpreadsheet import LinkedListSpreadsheet, linkedList, ListNode

# def display_array(array: ArraySpreadsheet):
#     arr =array.array 
#     for x in arr:
#         for y in x:
#             print("("+str(y.row)+","+ str(y.col)+","+ str(y.val)+")", end=" ")
#         print() #newline
#     print("finished")




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

if __name__ == "__main__":
    test_elems = [
        Cell(9, 9, 2.0),
        Cell(2, 5, 7),
        Cell(3, 1, 6),
        Cell(8, 5, -6.7),
    ]
    ss = LinkedListSpreadsheet()
    ss.buildSpreadsheet(test_elems)
    print(ss.appendRow())
    print(ss.appendCol())
    print(ss.find(6.0))
    print(ss.find(-6.0))
    print(ss.find(-6.7))
    print(ss.rowNum())
    print(ss.colNum())
    print(ss.update(2,5,-1.0))
    print(ss.update(10,10,1.0)) #should be true
    print(ss.update(11,11,2.5)) #should be false
    # print(ss.rowNum())
    # print(ss.colNum())
    # # print(ss.entries())
    print_entries(ss)
    print(ss.insertRow(1))
    print(ss.insertCol(4))
    print(ss.insertRow(-2))
    print(ss.colNum())
    print(ss.rowNum())
    # print(ss.entries())
    print_entries(ss)
    print(ss.update(2,5,-2.0))
    # print(ss.entries())
    print_entries(ss)
