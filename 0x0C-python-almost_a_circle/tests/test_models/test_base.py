#!/usr/bin/python3
"""
Unittest for Class Base
"""


from models.base import Base
import unittest


class TetsBaseClass(unittest.TestCase):
    """Test cases for the Base class"""
    base_1 = Base()
    base_2 = Base()
    base_3 = Base(5)

    def test_positive_numbers(self):
        """test number more or equal greather than zero"""
        base1 = Base(1)
        self.assertEqual(base1.id, 1)
        base2 = Base(2)
        self.assertEqual(base2.id, 2)
        base3 = Base(0)
        self.assertEqual(base3.id, 0)

    def test_none_value(self):
        """None value to id"""
        base1 = Base()
        self.assertEqual(base1.id, 4)
        base2 = Base()
        self.assertEqual(base2.id, 5)
        base3 = Base()
        self.assertEqual(base3.id, 6)
        base4 = Base()
        self.assertEqual(base4.id, 7)
        base5 = Base()
        self.assertEqual(base4.id, 7)
        self.assertEqual(base5.id, 8)

    def test_negative_numbers(self):
        """test number less than zero"""
        base1 = Base(-1)
        self.assertEqual(base1.id, -1)
        base2 = Base(-1024)
        self.assertEqual(base2.id, -1024)
        base3 = Base(-34)
        self.assertEqual(base3.id, -34)

    def test_base_tojsonstringnone(self):
        ret = "[]"
        test_list = self.base_1.to_json_string(None)
        self.assertEqual(ret, test_list)

    def test_base_tojsonstringempty(self):
        ret = "[]"
        test_list = self.base_1.to_json_string([])
        self.assertEqual(ret, test_list)

    def test_base_tojsonstringdict(self):
        test_dict = [{'id': 7}]
        ret = "[{\"id\": 7}]"
        self.assertEqual(self.base_1.to_json_string(test_dict), ret)

    def test_base_fromjsonstringnone(self):
        ret = []
        test_list = self.base_1.from_json_string(None)
        self.assertEqual(ret, test_list)

    def test_base_fromjsonstringempty(self):
        ret = []
        test_list = self.base_1.from_json_string("[]")
        self.assertEqual(ret, test_list)

    def test_base_fromjsonstringdict(self):
        ret = [{'id': 7}]
        test_dict = "[{\"id\": 7}]"
        self.assertEqual(self.base_1.from_json_string(test_dict), ret)


if __name__ == "__main__":
    unittest.main()
