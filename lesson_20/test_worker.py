import unittest
from worker import Boss, Worker


class BossTestCase(unittest.TestCase):
    def setUp(self):
        self.jeff = Boss(4, 'Jeff', 'Amazon')

    def test_boss_type(self):
        self.assertIsInstance(self.jeff, Boss, 'Not an instance of Boss class.')

    def test_attributes(self):
        # Testing if name was recorded the right way.
        self.assertEqual(self.jeff.name, 'Jeff')
        # Testing if wrong ID type will throw an error.
        self.assertIsInstance(self.jeff.id, int, 'ID is not a number. There must be a mistake.')
        # Testing if wrong Name type will throw an error.
        self.assertIsInstance(self.jeff.name, str, 'Name is not a string. There must be a mistake.')
        # Testing if wrong Company type will throw an error.
        self.assertIsInstance(self.jeff.company, str, 'Company is not a string. There must be a mistake.')

    def test_add_worker(self):
        ivan = Worker(3, 'Ivan', 'Amazon', self.jeff)
        self.jeff.add_worker(ivan)
        # Check if worker was added to Boss Bill workers list.
        self.assertEqual(self.jeff.workers[0], ivan, 'There are still no workers in the list after adding.')


class WorkerTestCase(unittest.TestCase):
    def setUp(self):
        self.jeff = Boss(4, 'Jeff', 'Amazon')
        self.maks = Worker(5, 'Maks', 'Amazon', self.jeff)

    def test_worker_type(self):
        self.assertIsInstance(self.maks, Worker, 'Not an instance of Worker class.')

    def test_attributes(self):
        # Testing if some attribute (ID) was recorded the right way.
        self.assertEqual(self.maks.id, 5)
        # Testing if wrong ID type will throw an error.
        self.assertIsInstance(self.maks.id, int, 'ID is not a number. There must be a mistake.')
        # Testing if wrong Name type will throw an error.
        self.assertIsInstance(self.maks.name, str, 'Name is not a string. There must be a mistake.')
        # Testing if wrong Company type will throw an error.
        self.assertIsInstance(self.maks.company, str, 'Company is not a string. There must be a mistake.')
        # Check if his boss is Jeff
        self.assertEqual(self.maks.boss, 'Jeff', 'Boss was added in wrong way.')

    def test_boss_setter(self):
        # Create a new boss
        self.tim = Boss(4, 'Tim', 'Apple')
        # Set a new boss for a worker
        self.maks.boss = self.tim
        # Testing if wrong Boss will throw an error.
        self.assertEqual(self.maks.boss, 'Tim', 'Boss was added in wrong way.')


if __name__ == "__main__":
    unittest.main()
