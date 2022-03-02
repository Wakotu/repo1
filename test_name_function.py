from name_function import get_formatted_name
import unittest


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('jains', 'joplin')
        self.assertEqual(formatted_name, 'Jains Joplin')

    def test_first_last_middle(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()
