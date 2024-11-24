import unittest
from unittest import TestCase

from board import *


class TestSudokuBoard(unittest.TestCase):
    def test_print_board(self):
        pretty = SudokuBoard(
            "785243691931856724462971583457968132612573498398214657379524816285167349146839725").pretty_print()
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

    def test_get_row_str(self):
        board = SudokuBoard("785243691931856724462971583457968132612573498398214657379524816285167349146839725")
        self.assertEqual("785243691", board.get_row_str(0))
        self.assertEqual("146839725", board.get_row_str(8))

    def test_get_column_str(self):
        board = SudokuBoard("785243691931856724462971583457968132612573498398214657379524816285167349146839725")
        self.assertEqual("794463321", board.get_column_str(0))
        self.assertEqual("143287695", board.get_column_str(8))

    def test_get_box_str(self):
        board = SudokuBoard("785243691931856724462971583457968132612573498398214657379524816285167349146839725")
        self.assertEqual("785931462", board.get_box_str(0))
        self.assertEqual("816349725", board.get_box_str(8))

    def test_get_cell(self):
        board = SudokuBoard("785243691931856724462971583457968132612573498398214657379524816285167349146839725")
        self.assertEqual(7, board.get_cell(0, 0).value)
        self.assertEqual(9, board.get_cell(0, 1).value)
        self.assertEqual(5, board.get_cell(8, 8).value)

if __name__ == '__main__':
    unittest.main()


