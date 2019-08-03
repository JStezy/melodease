from note import Note
from interval import Interval
import unittest

## TODO: Functions to test
# *

class TestInterval(unittest.TestCase):
    note_1 = Note(name="A4")
    note_2 = Note(name="B5")
    note_3 = Note(name="C5")
    note_4 = Note(name="E4")
    note_5 = Note(name="A4")
    interval_1 = Interval(note_1, note_5)
    interval_2 = Interval(note_1, note_4)
    interval_3 = Interval(note_1, note_3)
    interval_4 = Interval(note_3, note_5)
    interval_5 = Interval(note_2, note_3)

    def test_str(self):
        self.assertEqual(str(TestInterval.interval_1), 'unison')
        self.assertEqual(str(TestInterval.interval_2), 'perfect 4')
        self.assertEqual(str(TestInterval.interval_3), 'minor 3')
        self.assertEqual(str(TestInterval.interval_4), 'minor 3')
        self.assertEqual(str(TestInterval.interval_5), 'major 7')

    def test_eq(self):
        self.assertTrue(TestInterval.interval_3==TestInterval.interval_4)
        self.assertFalse(TestInterval.interval_2==TestInterval.interval_1) # different

    def test_equals(self):
        self.assertTrue(TestInterval.interval_3.equals(TestInterval.interval_4)) # same

    def test_is_dissonant(self):
        self.assertTrue(TestInterval.interval_5.is_dissonant()) # minor 2
        self.assertFalse(TestInterval.interval_3.is_dissonant()) # minor 3

    def test_dissonance(self):
        self.assertEqual(TestInterval.interval_2.dissonance(), 2)
        self.assertEqual(TestInterval.interval_5.dissonance(), 2)
        self.assertEqual(TestInterval.interval_1.dissonance(), 0)

    def test_get_topnote(self):
        self.assertEqual(TestInterval.interval_2.get_topnote(), Note(name="A4"))



if __name__ == '__main__':
    unittest.main()
