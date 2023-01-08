from unittest import TestCase
from task1_les21 import MyOpen

class TestMyOpen(TestCase):

    def test_enter(self):
        with open('some_text.txt', 'r') as f1:
            text1 = f1.read()
        with MyOpen('some_text.txt', 'r') as f2:
            text2 = f2.read()
        self.assertEqual(text1, text2)

    def test_exit(self):
        with MyOpen('some_text.txt', 'r') as f:
            f.read()
        self.assertEqual(f.closed, True)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            with MyOpen('text.txt', 'r') as f:
                f.read()

    def test_attribute_error(self):
        with self.assertRaises(AttributeError):
            with MyOpen('some_text.txt', 'r') as f:
                f.reads()

    def test_counter(self):
        self.assertEqual(MyOpen.counter, 2)