import unittest
from euler_square import Cell, Grid, EulerSquare


class TestEulerSquare(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.test_square = EulerSquare(3)
        self.test_square.grid[0][0].set_cell("a", "1")
        self.test_square.grid[0][1].set_cell("c", "2")
        self.test_square.grid[0][2].set_cell("b", "0")
        self.test_square.grid[1][0].set_cell("b", "2")
        self.test_square.grid[1][1].set_cell("a", "0")
        self.test_square.grid[1][2].set_cell("c", "1")
        self.test_square.grid[2][0].set_cell("c", "0")
        self.test_square.grid[2][1].set_cell("b", "1")
        self.test_square.grid[2][2].set_cell("a", "2")

    def test_is_valid(self):
        self.assertTrue(self.test_square.is_valid())
        self.test_square.grid[1][1].set_cell("a", "1")
        self.assertFalse(self.test_square.is_valid())

    def test_make_ood_square_conditions(self):
        self.test_square = EulerSquare(5)
        self.test_square.make_odd_square_conditions()
        self.assertTrue(self.test_square.is_valid())


class TestGrid(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.test = Grid(2)
        self.test.grid[0][0].set_cell("a", "1")
        self.test.grid[0][1].set_cell("b", "1")
        self.test.grid[1][0].set_cell("a", "2")
        self.test.grid[1][1].set_cell("b", "2")

    def test_print_grid(self):
        expected_grid = " a1 b1\n a2 b2\n"
        original_result = self.test.__str__()
        self.assertEqual(expected_grid, original_result)

    def test_count(self):
        expected_count_number = 1
        orignal_num_number = self.test.count(self.test.grid[0][0])
        self.assertEqual(expected_count_number, orignal_num_number)


class TestCell(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.test_cell_a = Cell()
        self.test_cell_a.set_letter("a")
        self.test_cell_a.set_number("1")

        self.test_cell_b = Cell()
        self.test_cell_b.set_letter("a")
        self.test_cell_b.set_number("1")

        self.test_cell_c = Cell()
        self.test_cell_c.set_letter("A")
        self.test_cell_c.set_number("1")

        self.test_cell_d = Cell()
        self.test_cell_d.set_cell("a", "2")

    def test__eq__(self):
        self.assertEqual(self.test_cell_a, self.test_cell_b)
        self.assertEqual(self.test_cell_b, self.test_cell_a)
        self.assertNotEqual(self.test_cell_a, self.test_cell_c)
        self.assertNotEqual(self.test_cell_a, self.test_cell_d)

    def test__str__(self):
        expected_output_a = "a1"
        orignal_result = self.test_cell_a.__str__()
        self.assertEqual(expected_output_a, orignal_result)


if __name__ == "__main__":
    unittest.main()
