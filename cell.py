from graphics import Line, Point

class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self.__win is None:
            return
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        bg = "white"
        
        # lewa
        color = "black" if self.has_left_wall else bg
        self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), color)

        # prawa
        color = "black" if self.has_right_wall else bg
        self.__win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), color)

        # góra
        color = "black" if self.has_top_wall else bg
        self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), color)

        # dół
        color = "black" if self.has_bottom_wall else bg
        self.__win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), color)

    def draw_move(self, to_cell, undo=False):
        start_x = (self.__x1 + self.__x2) // 2
        start_y = (self.__y1 + self.__y2) // 2

        end_x = (to_cell.__x1 + to_cell.__x2) // 2
        end_y = (to_cell.__y1 + to_cell.__y2) // 2

        color = "red"
        if undo:
            color = "gray"

        if self.__win is not None:
            self.__win.draw_line(Line(Point(start_x, start_y), Point(end_x, end_y)), color)
