import os
from thinkful.bike.lib.bike_lib import csv_to_dict

__author__ = 'jay'

import unittest


class TestCsvToDict(unittest.TestCase):
    def setUp(self):
        self.path = 'tests/data'
        self.csv = 'test_data/test.csv'

    def test_returns_col_0_keyed_to_dict_of_all_headers_to_values(self):

        expected_res = {'a': {'name': 'a',
                              'rank': 'b',
                              'serial_number': 'c'},
                        '1': {'name': '1',
                              'rank': '2',
                              'serial_number': '3'}
                        }

        res = csv_to_dict(os.path.join(self.path, *self.csv.split('/')))

        self.assertEqual(expected_res, res)

if __name__ == '__main__':
    unittest.main()