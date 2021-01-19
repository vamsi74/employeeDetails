import unittest
from python_rest import SortByName


class MyTestCase(unittest.TestCase):
    def test_outsideKey(self):
        self.assertEqual(SortByName.sortFirst('outsideKey'), 'OOPS! outsideKey is not present in data to sort')

    def test_supervisor(self):
        self.assertEqual(SortByName.sortFirst('supervisor'), 'supervisor is not present for all employees to sort')

    def test_idKey(self):
        self.assertNotEqual(SortByName.sortFirst('id'), 'OOPS! id is not present in data to sort')

    def test_firstname(self):
        self.assertNotEqual(SortByName.sortFirst('firstname'), 'OOPS! firstname is not present in data to sort')

    def test_firstname_all(self):
        self.assertNotEqual(SortByName.sortFirst('firstname'), 'firstname is not present for all employees to sort')

    def test_firstname_sort(self):
        check=SortByName.sortFirst('firstname')
        for i in range(1,len(check['employees']['employee'])-1):
            self.assertLess(check['employees']['employee'][0]['firstname'],check['employees']['employee'][i]['firstname'])

if __name__ == '__main__':
    unittest.main()
