import unittest
from dict2 import Dict2

class TestDict2(unittest.TestCase):
    def test_set_get_item(self):
        obj = Dict2()
        obj['a'] = 1
        self.assertEqual(obj['a'], 1)

    def test_custom_exception(self):
        obj = Dict2()
        with self.assertRaises(KeyError):
            val = obj['a']

    def test_iter(self):
        obj = Dict2()
        obj['a'] = 1
        obj['b'] = 2
        obj['c'] = 3
        keys = [key for key in obj]
        self.assertEqual(keys, ['a', 'b', 'c'])

    def test_update_existing_key(self):
        obj = Dict2()
        obj['a'] = 1
        obj['a'] = 2
        self.assertEqual(obj['a'], 2)

if __name__ == '__main__':
    unittest.main()
