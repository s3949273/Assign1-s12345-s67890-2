import random
import sys,os
import matplotlib.pyplot as plt
import seaborn as sns
sys.path.insert(0, os.path.abspath('..'))
from spreadsheet.cell import Cell
from spreadsheet.arraySpreadsheet import ArraySpreadsheet
from time import perf_counter
# class Cell:
#     def __init__(self, row: int, col: int, val: float):
#         # a cell object has the row, column and value
#         self.row = row
#         self.col = col
#         self.val = val

#     def __str__(self) -> str:
#         """
#         Convert cell to a string for printing.
#         """

#         return "(" + str(self.row) + "," + str(self.col) + "," + "{:.2f}".format(self.val) + ")"
    
def create_random_cells(num_cells: int) -> list[Cell]:
    ret = ""
    for _ in range(num_cells):
        row = random.randint(1, num_cells/1000)
        col = random.randint(1, num_cells/1000)
        val = random.uniform(0.1,9.9)
        ret += str(row) +" "+  str(col) + " "+str(val)+"\n"
    return ret

def write_to_file():
    file = open("sample_data.txt","w")
    file.write(create_random_cells(200_000))


def display_array(array: ArraySpreadsheet):
    arr =array.array 
    for x in arr:
        for y in x:
            if(y == None):
                print("("+str(y.row),str(y.col)+" N)", end = " ")
            else:
                print(y, end = " ")
        print() #newline
    print("finished")


def test():
    spreadsheet = ArraySpreadsheet()
    cellsFromFiles = []
    try:
        dataFile = open("sample_data.txt", 'r')
        for line in dataFile:
            values = line.split()
            currRow = int(values[0])
            currCol = int(values[1])
            currVal = float(values[2])
            currCell = Cell(currRow, currCol, currVal)
            # each line contains a cell
            cellsFromFiles.append(currCell)
        dataFile.close()
        # construct the spreadsheet from the read in data
        start_time = perf_counter()
        spreadsheet.buildSpreadsheet(cellsFromFiles)
        end_time = perf_counter()
        print(end_time-start_time)
        display_array(spreadsheet)
    except FileNotFoundError as e:
        print("Data file doesn't exist.")



if __name__ == "__main__":
    write_to_file()
    test()
