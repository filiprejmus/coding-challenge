from fold import fold
import unittest

string_input = "iamfilip"
list_input = [1,2,3,4,5,6]
range_input = range(0,100,2)

addfunc = lambda x,y: x+y
addspace = lambda x,y: x + ' ' + y

class TestFold(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(fold([], 0, addfunc), 0)

    def test_list(self):
        self.assertEqual(fold(list_input, 2, addfunc), 23)

    def test_string(self):
        self.assertEqual(fold(string_input,'', addspace), ' i a m f i l i p')

    def test_range(self):
        self.assertEqual(fold(range_input,0, addfunc), 2450)

    def test_non_sequence(self):
        with self.assertRaises(TypeError):
            (fold(3, 0 , addfunc))

    def test_multitype_list(self):
        with self.assertRaises(TypeError):
            (fold(['ab', 1], '' , addspace))
    


if __name__ == '__main__':
    unittest.main()