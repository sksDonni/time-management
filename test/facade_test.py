import unittest
from facade import DatabaseFacade

class FacadeTest(unittest.TestCase):
    def test_get_all_ids_returns_ids(self):
        facade = DatabaseFacade()
        ids = facade.get_all_ids()
        
        # Will return false if no items in database yet
        self.assertTrue(len(ids) > 0)
        for id in ids:
            self.assertTrue(type(id) == int)