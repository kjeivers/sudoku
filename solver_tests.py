import unittest

from solver import *

class TestParts(unittest.TestCase):
    def test_print_board(self):
        pretty = SudokuBoard("785243691931856724462971583457968132612573498398214657379524816285167349146839725").pretty_print()
        self.assertEqual(pretty,
"""
785|243|691
931|856|724
462|971|583
---+---+---
457|968|132
612|573|498
398|214|657
---+---+---
379|524|816
285|167|349
146|839|725
""".strip())

    def test_get_row(self):
        board = SudokuBoard("785243691931856724462971583457968132612573498398214657379524816285167349146839725")
        self.assertEqual("785243691", board.get_row(1))
        self.assertEqual("146839725", board.get_row(9))

    def test_get_column(self):
        board = SudokuBoard("785243691931856724462971583457968132612573498398214657379524816285167349146839725")
        self.assertEqual("794463321", board.get_column(1))
        self.assertEqual("143287695", board.get_column(9))

    def test_box_1_position_to_cell(self):
        self.assertEqual((1, 1), SudokuBoard.box_position_to_cell(1, 1))
        self.assertEqual((2, 2), SudokuBoard.box_position_to_cell(1, 5))
        self.assertEqual((3, 3), SudokuBoard.box_position_to_cell(1, 9))

    def test_box_5_position_to_cell(self):
        self.assertEqual((5, 5), SudokuBoard.box_position_to_cell(5, 5))
        self.assertEqual((6, 6), SudokuBoard.box_position_to_cell(5, 9))
    
    def test_box_9_position_to_cell(self):
        self.assertEqual((8, 9), SudokuBoard.box_position_to_cell(9, 8))

    def test_get_box(self):
        board = SudokuBoard("785243691931856724462971583457968132612573498398214657379524816285167349146839725")
        self.assertEqual("785931462", board.get_box(1))
        self.assertEqual("816349725", board.get_box(9))

class TestSolveBoards(unittest.TestCase):

    def test_almost_solved(self):
        almost_solved_sudoku = "-8524369193185672446297158345796813261257349839821465737952481628516734914683972-"
        solution = "785243691931856724462971583457968132612573498398214657379524816285167349146839725"
        self.assertEqual(solve(almost_solved_sudoku).board, solution)

    def test_easy_1(self):
        easy_1 = "96---5-74"+"7---4---1"+"--5-7-2-8"+"4--7--2--"+"-829--475"+"517-24-3-"+"53--4--2-"+"-9----1-3"+"76-38----"
        # TODO: finn riktig løsning
        solution = "785243691931856724462971583457968132612573498398214657379524816285167349146839725"
        self.assertEqual(solve(easy_1), solution)

    def test_medium_1(self):
        medium_1 = "5---27136"+"1-73-98-4"+"---5189-2"+"--3---6--"+"-9-53-2--"+"-412-7---"+"96--42---"+"---9---1-"+"-25---4--"
        # TODO: finn riktig løsning
        solution = "785243691931856724462971583457968132612573498398214657379524816285167349146839725"
        self.assertEqual(solve(medium_1), solution)

if __name__ == '__main__':
    unittest.main()
