import unittest
import interface_time_management


class TimeManagementTest(unittest.TestCase):
    # This method currently sits on the TimeManagement class, but it could eventually
    # be re-factored to a helper/validator class.
    def test_validates_id_works_as_expected(self):
        ids = [1, 2, 3, 4]

        invalid1 = "one"
        invalid2 = "o32o"
        self.assertFalse(interface_time_management.task_id_is_valid(invalid1, ids))
        self.assertFalse(interface_time_management.task_id_is_valid(invalid2, ids))

        valid1 = "1"
        valid2 = "2"
        self.assertTrue(interface_time_management.task_id_is_valid(valid1, ids))
        self.assertTrue(interface_time_management.task_id_is_valid(valid2, ids))
