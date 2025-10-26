import unittest
import times as t

class TestTimes(unittest.TestCase):

    def test_given_input(self):
        
        # arrange
        expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]

        # act
        large = t.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
        short = t.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
        result = t.compute_overlap_time(large, short)

        # assert
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()