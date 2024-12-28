import unittest

from solver import *

class TestCases(unittest.TestCase):

    def test_almost_solved(self):
        almost_solved_sudoku = SudokuBoard("""
            -85│243│691
            931│856│724
            462│971│583
            ───┼───┼───
            457│968│132
            612│573│498
            398│214│657
            ───┼───┼───
            379│524│816
            285│167│349
            146│839│72-
            """)
        solution = SudokuBoard("""
            785│243│691
            931│856│724
            462│971│583
            ───┼───┼───
            457│968│132
            612│573│498
            398│214│657
            ───┼───┼───
            379│524│816
            285│167│349
            146│839│725
            """)
        self.assertEqual(solution.pretty_print(), Solver(almost_solved_sudoku).solve().pretty_print())

    def test_easy_1(self):
        easy_1 = SudokuBoard("""
            96-│7--│--5
            --5│-4-│-7-
            -74│--1│2-8
            ───┼───┼───
            4--│-82│517
            7--│9--│-24
            2--│475│-3-
            ───┼───┼───
            53-│-9-│76-
            -4-│---│38-
            -2-│1-3│---
            """)
        solution = SudokuBoard("""
            962│738│145
            185│249│673
            374│651│298
            ───┼───┼───
            496│382│517
            753│916│824
            218│475│936
            ───┼───┼───
            531│894│762
            649│527│381
            827│163│459
            """)
        self.assertEqual(solution.pretty_print(), Solver(easy_1).solve().pretty_print())

    def test_medium_1(self):
        # "5---27136"+"1-73-98-4"+"---5189-2"+"--3---6--"+"-9-53-2--"+"-412-7---"+"96--42---"+"---9---1-"+"-25---4--"
        medium_1 = SudokuBoard("""
            5--│1-7│---
            -27│3-9│518
            136│8-4│9-2
            ───┼───┼───
            --3│-9-│-41
            ---│53-│2-7
            6--│2--│---
            ───┼───┼───
            96-│---│-25
            -42│9--│---
            ---│-1-│4--
            """)

        solution = SudokuBoard("""
            589│127│364
            427│369│518
            136│854│972
            ───┼───┼───
            253│798│641
            814│536│297
            679│241│853
            ───┼───┼───
            961│483│725
            342│975│186
            785│612│439
            """)
        self.assertEqual(solution.pretty_print(), Solver(medium_1).solve().pretty_print())

if __name__ == '__main__':
    unittest.main()
