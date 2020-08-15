import unittest
import datetime
import kronos

string_format_time = "%Y-%m-%d %H:%M:%S"
date_time_str = "2020-07-19 18:14:21"


class KronosTest(unittest.TestCase):
    def test_get_day_of_week(self):
        date_time = datetime.datetime.strptime(date_time_str, string_format_time)
        self.assertEqual("Sunday", kronos.get_day_of_week(date_time))

    def test_is_yesterday(self):
        date_time = kronos.get_date_time_from_string("2020-07-20 18:14:21")
        self.assertTrue(kronos.is_yesterday(date_time_str, today=date_time))
        date_time = kronos.get_date_time_from_string("2020-07-19 18:14:21")
        self.assertFalse(kronos.is_yesterday(date_time_str, today=date_time))
