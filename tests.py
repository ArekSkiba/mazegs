import unittest
from maze import Maze
from cell import Cell


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_dimensions(self):
        cols, rows = 5, 4
        m = Maze(0, 0, rows, cols, 10, 10, None)
        self.assertEqual(len(m._Maze__cells), cols)
        self.assertEqual(len(m._Maze__cells[0]), rows)

    def test_maze_cells_are_cell_instances(self):
        m = Maze(0, 0, 3, 3, 10, 10, None)
        for col in m._Maze__cells:
            for cell in col:
                self.assertIsInstance(cell, Cell)

    def test_initial_cell_coordinates(self):
        m = Maze(0, 0, 2, 2, 10, 10, None)
        for col in m._Maze__cells:
            for cell in col:
                self.assertEqual(cell._Cell__x1, -1)
                self.assertEqual(cell._Cell__x2, -1)
                self.assertEqual(cell._Cell__y1, -1)
                self.assertEqual(cell._Cell__y2, -1)

    def test_cell_size_logic(self):
        m = Maze(0, 0, 4, 4, 20, 30, None)
        self.assertEqual(len(m._Maze__cells), 4)
        self.assertEqual(len(m._Maze__cells[0]), 4)


    def test_reset_cells_visited(self):
        m = Maze(0, 0, 4, 4, 10, 10, None)
        # ręcznie zaznacz jedną komórkę jako odwiedzoną
        m._Maze__cells[0][0].visited = True
        m._Maze__reset_cells_visited()
        self.assertFalse(m._Maze__cells[0][0].visited)




if __name__ == "__main__":
    unittest.main()