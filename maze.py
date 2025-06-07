from cell import Cell
import random
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
        ):
        if seed is not None:
            random.seed(seed)
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)

    def __create_cells(self):
        for i in range(self.__num_cols):
            col = []
            for j in range(self.__num_rows):
                cell = Cell(self.__win)
                col.append(cell)
            self.__cells.append(col)
        
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)
        
    def __draw_cell(self, i, j):
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)

        last_col = self.__num_cols - 1
        last_row = self.__num_rows - 1
        self.__cells[last_col][last_row].has_bottom_wall = False
        self.__draw_cell(last_col, last_row)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            neighbors = []
            # góra
            if j > 0 and not self.__cells[i][j - 1].visited:
                neighbors.append(("N", i, j - 1))
            # dół
            if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited:
                neighbors.append(("S", i, j + 1))
            # lewo
            if i > 0 and not self.__cells[i - 1][j].visited:
                neighbors.append(("W", i - 1, j))
            # prawo
            if i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited:
                neighbors.append(("E", i + 1, j))

            if len(neighbors) == 0:
                self.__draw_cell(i, j)
                return
            
            direction, ni, nj = random.choice(neighbors)

            if direction == "N":
                self.__cells[i][j].has_top_wall = False
                self.__cells[ni][nj].has_bottom_wall = False
            elif direction == "S":
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[ni][nj].has_top_wall = False
            elif direction == "W":
                self.__cells[i][j].has_left_wall = False
                self.__cells[ni][nj].has_right_wall = False
            elif direction == "E":
                self.__cells[i][j].has_right_wall = False
                self.__cells[ni][nj].has_left_wall = False

            self.__break_walls_r(ni, nj)