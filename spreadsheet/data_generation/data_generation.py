import random
from spreadsheet.cell import Cell
def create_random_cells(num_cells: int) -> list[Cell]:
    cells = []
    for i in range(num_cells):
        row = random.randint(1, 25)
        col = random.randint(1, 25 )
        val = random.randint(1,9)
        cell = Cell(row, col, val)
        cells.append(cell)
    return cells

def write_to_file():
    file = open("sample_data.txt","w")
    file.write("hello")


write_to_file()