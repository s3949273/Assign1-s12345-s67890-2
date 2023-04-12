from spreadsheet.cell import Cell
from spreadsheet.arraySpreadsheet import ArraySpreadsheet

def display(array: ArraySpreadsheet):
    arr =array.array 
    for x in arr:
        for y in x:
            print("("+str(y.row)+","+ str(y.col)+","+ str(y.val)+")", end=" ")
        print() #newline
    print("finished")
test_elems = [
Cell(9, 9, 2.0),
Cell(2, 5, 7),
Cell(3, 1, 6),
Cell(8, 5, -6.7),
]

if __name__ == "__main__":
    my_arr = ArraySpreadsheet()
    display(my_arr)
    # my_arr.appendCol()
    # my_arr.appendCol()
    # my_arr.insertRow(5)
    my_arr.insertCol(15)
    display(my_arr)
    print("column number: ", my_arr.colNum())

