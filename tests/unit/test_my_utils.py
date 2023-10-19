import sys
sys.path.insert(0, '../../src')  # noqa
import my_utils
import unittest
import random
import math
import statistics


class TestMyUtils(unittest.TestCase):

    def setUp(self):

        random.seed(42)
        self.array = [random.randint(0, 100) for _ in range(100)]
        self.path_to_data = '../test_data/'
        
    def test_get_column_from_name_Equality(self):

        file_name = self.path_to_data + 'Agro_co2_emission_test.csv'
        idx_actual = my_utils.get_column_from_name(file_name=file_name,
                                           column_name='Savanna fires')
        self.assertEqual(idx_actual, 2)
    def test_get_columns_checkEquality(self):

        afghan_fires_list_pred = [0, 0, 0, 0]
        file_name = self.path_to_data + 'Agro_co2_emission_test.csv'
        fires_actual = my_utils.get_column(file_name=file_name,
                                           query_value='Afghanistan')
        self.assertEqual(fires_actual, afghan_fires_list_pred)

    def test_get_columns_notequal(self):

        afghan_fires_list_pred = [1, 1, 1, 1]
        file_name = self.path_to_data + 'Agro_co2_emission_test.csv'
        fires_actual = my_utils.get_column(file_name=file_name,
                                           query_value='Afghanistan')
        self.assertNotEqual(fires_actual, afghan_fires_list_pred)

    def test_mean_equal(self):

        mean_pred = my_utils.get_mean(self.array)
        self.assertEqual(statistics.mean(self.array), mean_pred)

    def test_mean_nonequal(self):

        mean_pred = my_utils.get_mean(self.array)
        self.assertNotEqual(-1, mean_pred)

    def test_median_equal(self):

        med_pred = my_utils.get_median(self.array)
        self.assertEqual(statistics.median(self.array), med_pred)

    def test_median_nonequal(self):

        med_pred = my_utils.get_median(self.array)
        self.assertNotEqual(-1, med_pred)

    def test_stdev_equal(self):

        stdev_pred = my_utils.get_standard_deviation(self.array)
        self.assertTrue(statistics.stdev(self.array)-stdev_pred < 0.001)

    def test_stdev_notequal(self):

        stdev_pred = my_utils.get_standard_deviation(self.array)
        self.assertNotEqual(-1, stdev_pred)


if __name__ == '__main__':
    unittest.main()
