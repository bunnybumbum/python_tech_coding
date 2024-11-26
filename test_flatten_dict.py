import unittest
from src.flatten_dict import flatten_dict

class TestFlattenDict(unittest.TestCase):
    def test_simple_dict(self):
        input_dict = {"a": 1, "b": 2, "c": 3}
        expected_output = {"a": 1, "b": 2, "c": 3}
        self.assertEqual(flatten_dict(input_dict), expected_output)

    def test_nested_dict(self):
        input_dict = {
            'a': 1,
            'b': {
                'c': 2,
                'd': {
                    'e': 3,
                    'f': 4
                }
            },
            'g': {
                'h': 5
            }
        }
        expected_output = {
            'a': 1,
            'b.c': 2,
            'b.d.e': 3,
            'b.d.f': 4,
            'g.h': 5
        }
        self.assertEqual(flatten_dict(input_dict), expected_output)
    
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            flatten_dict("invalid_input")

if __name__ == "__main__":
    unittest.main()
    