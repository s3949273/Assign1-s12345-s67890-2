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
    

    print("colNum:",ss.colNum())
    
    print("rowNum:",ss.rowNum())


if __name__ == "__main__":
    test_elems = [
        Cell(9, 9, 2.0),
        Cell(2, 5, 7),
        Cell(3, 1, 6),
        Cell(8, 5, -6.7),
    ]
    ss = LinkedListSpreadsheet()
    # display_linked_list(ss)
    # display_linked_list(ss)
    # ss.appendCol()

    # ss.insertRow(1)
    # display_linked_list(ss)
    ss.buildSpreadsheet(test_elems)
    display_linked_list(ss)
