import unittest

from solver import *

class TestCases(unittest.TestCase):

    def test_almost_solved(self):
        almost_solved_sudoku = "-8524369193185672446297158345796813261257349839821465737952481628516734914683972-"
        solution = "785243691931856724462971583457968132612573498398214657379524816285167349146839725"

        self.assertEqual(solution, Solver(almost_solved_sudoku).solve().board, solution)

    def test_easy_1(self):
        easy_1 = "96---5-74"+"7---4---1"+"--5-7-2-8"+"4--7--2--"+"-829--475"+"517-24-3-"+"53--4--2-"+"-9----1-3"+"76-38----"
        # TODO: finn riktig løsning
        solution = "785243691931856724462971583457968132612573498398214657379524816285167349146839725"
        self.assertEqual(solution, Solver(easy_1).solve().board)

    def test_medium_1(self):
        medium_1 = "5---27136"+"1-73-98-4"+"---5189-2"+"--3---6--"+"-9-53-2--"+"-412-7---"+"96--42---"+"---9---1-"+"-25---4--"
        # TODO: finn riktig løsning
        solution = "785243691931856724462971583457968132612573498398214657379524816285167349146839725"
        self.assertEqual(solution, Solver(medium_1).solve().board)

if __name__ == '__main__':
    unittest.main()
