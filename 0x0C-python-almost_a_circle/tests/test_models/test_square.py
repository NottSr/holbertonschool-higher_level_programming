#!/usr/bin/python3
"""
Unittest for Class Square
"""


from models.square import Square
import unittest


class TetsSquare_01_attributes(unittest.TestCase):
    """
    Test cases for the Square class
    """

    def test_01_init(self):
        """
        -----Test for the fisrt Square writed-----
        """

        r1 = Square(10)
        self.assertEqual(r1.id, 48)
        r2 = Square(2)
        self.assertEqual(r2.id, 49)
        r3 = Square(2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertNotIsInstance(r3.height, Square)

    def test_02_init_TypeError(self):
        """
        -----Test Typeerror the values Must be integers-----
        """

        """
        Tests to TypeErrors
        """
        typeErr = ["number", "10", 3.0, [1, 2], {"a": 1}, float("nan"), None]
        for err in typeErr:
            with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Square(err, 10, "4")
            with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Square(23, err)
            with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Square(2, 3, err)

    def test_03_init_valueError(self):
        """
        -----Tests to ValueErrors-----
        """
        valueErr = [-2, -1024, -1]
        for err in valueErr:
            with self.assertRaisesRegex(ValueError, "width must be > 0"):
                Square(err, 10, 6)
            with self.assertRaisesRegex(ValueError, "x must be >= 0"):
                Square(23, err)
            with self.assertRaisesRegex(ValueError, "y must be >= 0"):
                Square(2, 3, err)

        """
        Width and height must be > 0
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 10, 6)


class TetsSquare_01_methods(unittest.TestCase):
    """
    Test cases for the Square class
    """

    def test_04_init_area(self):
        """
        -----Test area method-----
        """

        ra1 = Square(2)
        self.assertEqual(ra1.area(), 4)
        ra2 = Square(10, 3, 4, 12)
        self.assertEqual(ra2.area(), 100)

        """
        Width and height must be > 0
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 10, 6).area()

    def test_05_init_display(self):
        """
        -----Display method-----
        """

        rd1 = Square(1)
        result1 = None
        self.assertEqual(rd1.display(), result1)
        rd2 = Square(3)
        result2 = None
        self.assertEqual(rd2.display(), result2)
        rd3 = Square(5)
        result3 = None
        self.assertEqual(rd3.display(), result3)
        rd3 = Square(2)
        result3 = None
        self.assertEqual(rd3.display(), result3)

        """
        Hangling x and y
        """
        rd4 = Square(2, 2, 2, 2)
        result4 = None
        self.assertEqual(rd4.display(), result4)
        rd5 = Square(2, 2, 0)
        result5 = None
        self.assertEqual(rd5.display(), result5)
        rd6 = Square(3, 3, 1)
        result6 = None
        self.assertEqual(rd6.display(), result6)

    def test_06_init_str(self):
        """
        -----Test str method------
        """

        rs1 = Square(1, 3, 4, 5)
        str1 = "[Square] (5) 3/4 - 1"
        self.assertEqual(rs1.__str__(), str1)

        rs2 = Square(2, 0, 0, 34)
        str2 = "[Square] (34) 0/0 - 2"
        self.assertEqual(rs2.__str__(), str2)

    def test_07_init_update(self):
        """
        Test update method
        """

        """
        only with *args
        """
        ru1 = Square(1, 0, 0, 1)
        r1 = "[Square] (1) 0/0 - 1"
        self.assertEqual(ru1.__str__(), r1)
        ru1.update(0, 1, 2, 2)
        r2 = "[Square] (0) 2/2 - 1"
        self.assertEqual(ru1.__str__(), r2)
        ru1.update(8, 100, 10, 3)
        r2 = "[Square] (8) 10/3 - 100"
        self.assertEqual(ru1.__str__(), r2)
        ru1.update(100, 23)
        r2 = "[Square] (100) 10/3 - 23"
        self.assertEqual(ru1.__str__(), r2)
        ru1.update()
        r2 = "[Square] (100) 10/3 - 23"
        self.assertEqual(ru1.__str__(), r2)

        """
        With *args and **kwargs
        """
        r = Square(4, 0, 3, 1)
        r2 = "[Square] (1) 0/3 - 4"
        self.assertEqual(r.__str__(), r2)
        """
        Case not arguments
        """
        r.update()
        r2 = "[Square] (1) 0/3 - 4"
        self.assertEqual(r.__str__(), r2)
        r.update(id=100, x=10)
        r2 = "[Square] (100) 10/3 - 4"
        self.assertEqual(r.__str__(), r2)
        r.update(id=10, size=137)
        r2 = "[Square] (10) 10/3 - 137"
        self.assertEqual(r.__str__(), r2)
        r.update(1, 2, 3, id=100, x=10)
        r2 = "[Square] (1) 3/3 - 2"
        self.assertEqual(r.__str__(), r2)
        r.update(113, id=100, x=10)
        r2 = "[Square] (113) 3/3 - 2"
        self.assertEqual(r.__str__(), r2)
        r.update(id=100, x=10)
        r2 = "[Square] (100) 10/3 - 2"
        self.assertEqual(r.__str__(), r2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(id=100, x="10")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(size="wrong", x="10")


if __name__ == "__main__":
    unittest.main(failfast=True, exit=False)
