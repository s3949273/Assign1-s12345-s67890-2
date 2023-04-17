import random
import sys,os

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
sys.path.insert(0, os.path.abspath('..'))
from spreadsheet.cell import Cell
from spreadsheet.arraySpreadsheet import ArraySpreadsheet
from spreadsheet.linkedlistSpreadsheet import LinkedListSpreadsheet
from spreadsheet.csrSpreadsheet import CSRSpreadsheet
from spreadsheet.baseSpreadsheet import BaseSpreadsheet

from time import perf_counter

    
def create_random_cells(num_cells: int, max_col:int, max_row:int) -> list[Cell]:
    ret = ""
    ret += str(max_row-1)+" "+ str(max_col-1)+ " "+str(round(random.uniform(0.1,9.9), ndigits=2)) +"\n"
    for _ in range(num_cells):
        row = random.randint(0, max_col-1)
        col = random.randint(0, max_row-1)
        val = round(random.uniform(0.1,9.9), ndigits=2)
        ret += str(row) +" "+  str(col) + " "+str(val)+"\n"
    return ret

def write_to_file(cells_to_generate:int, max_col:int, max_row:int):
    file = open("sample_data.txt","w")
    file.write(create_random_cells(cells_to_generate, max_col, max_row))

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

def get_lCells()->list[Cell]:
    """
    basically read from the file and create a list of cells from the data from the file
    """
    try:
        lcells = []
        data_time = perf_counter()
        dataFile = open("sample_data.txt", 'r')
        for line in dataFile:
            values = line.split()
            currRow = int(values[0])
            currCol = int(values[1])
            currVal = float(values[2])
            currCell = Cell(currRow, currCol, currVal)
            # each line contains a cell
            lcells.append(currCell)
        dataFile.close()
        data_time_close = perf_counter()
        return lcells
    except FileNotFoundError as e:
        print("Data file doesn't exist.")
    pass

def set_up_cells(cells_to_generate, max_col, max_row):
    write_to_file(cells_to_generate, max_col, max_row)
    return get_lCells()

def test_buildSpreadSheet(spreadSheet:BaseSpreadsheet,lCells:list[Cell]):
    start_time = perf_counter()
    spreadSheet.buildSpreadsheet(lCells)
    end_time = perf_counter()
    return end_time-start_time

def test_entries(spreadSheet:BaseSpreadsheet):
    start_time = perf_counter()
    spreadSheet.entries()
    end_time = perf_counter()
    return end_time-start_time

def test_update(spreadSheet:BaseSpreadsheet, rowIndex: int, colIndex:int, val:float):
    start_time = perf_counter()
    spreadSheet.update(rowIndex, colIndex,val)
    end_time = perf_counter()
    return end_time-start_time

def test_append_row(spreadSheet:BaseSpreadsheet):
    start_time = perf_counter()
    spreadSheet.appendRow()
    end_time = perf_counter()
    return end_time-start_time

def test_append_col(spreadSheet:BaseSpreadsheet):
    start_time = perf_counter()
    spreadSheet.appendCol()
    end_time = perf_counter()
    return end_time-start_time

def test_insert_row(spreadSheet:BaseSpreadsheet, rowIndex:int):
    start_time = perf_counter()
    spreadSheet.insertRow(rowIndex)
    end_time = perf_counter()
    return end_time-start_time

def test_insert_col(spreadsheet:BaseSpreadsheet, colIndex:int):
    start_time = perf_counter()
    spreadsheet.insertCol(colIndex)
    end_time = perf_counter()
    return end_time-start_time

def find(spreadSheet:BaseSpreadsheet, value:float):
    start_time = perf_counter()
    spreadSheet.find(value)
    end_time = perf_counter()
    return end_time-start_time


if __name__ == "__main__":
    small_spreadsheets= []
    for _ in range(10):
        small_spreadsheets.append(ArraySpreadsheet())
    small_lCells = []
    for _ in range(10):
        small_lCells.append(set_up_cells(_*5000, 25, 25))
    
    #note values are in milliseconds not seconds, this is because the values are really small
    test_buildSpreadSheet_small = pd.DataFrame([test_buildSpreadSheet(small_spreadsheets[x], small_lCells[x])*1000 for x in range(10)],columns=["build_spreadsheet"])
    test_append_col_small = pd.DataFrame([test_append_col(small_spreadsheets[x])*1000 for x in range(10)],columns=["append_col"])
    test_append_row_small = pd.DataFrame([test_append_row(small_spreadsheets[x])*1000 for x in range(10)],columns=["append_row"])
    test_insert_col_small = pd.DataFrame([test_insert_col(small_spreadsheets[x], x)*1000 for x in range(10)],columns=["insert_col"])
    test_insert_row_small = pd.DataFrame([test_insert_row(small_spreadsheets[x], x)*1000 for x in range(10)],columns=["insert_row"])
    test_entries_small = pd.DataFrame([test_entries(small_spreadsheets[x])*1000 for x in range(10)],columns=["entries"])
