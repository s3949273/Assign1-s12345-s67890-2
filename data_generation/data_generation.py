import random
import sys,os
sys.path.insert(0, os.path.abspath('..'))
from spreadsheet.cell import Cell
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
        row = random.randint(1, 25)
        col = random.randint(1, 25 )
        val = random.randint(1,9)
        ret += str(row) +" "+  str(col) + " "+str(val)+"\n"
    return ret

def write_to_file():
    file = open("sample_data.txt","w")
    file.write(create_random_cells(200_000))



def test():
    file = open("sample_data.txt", "r")



