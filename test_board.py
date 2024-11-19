import unittest

from solver import *

class TestCases(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()
