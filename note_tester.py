from note import Note
import unittest

class TestNote(unittest.TestCase):
    note_1 = Note(name="A5")
    note_2 = Note()
    note_3 = Note(freq=82.4)
    note_4 = Note()

    def test_str(self):
        self.assertEqual(str(TestNote.note_1), 'A5')

    def test_eq(self):
        print("the note is: " + str(TestNote.note_4))
        self.assertTrue(TestNote.note_2==TestNote.note_4)
        self.assertFalse(TestNote.note_1==TestNote.note_3) # different notes
        self.assertFalse(TestNote.note_2==TestNote.note_1) # different octaves

    def test_equals(self):
        self.assertTrue(TestNote.note_1.equals(other=TestNote.note_2)) # different octaves
        self.assertFalse(TestNote.note_1.equals(other=TestNote.note_3)) # different notes

    def test_set_length(self):
        TestNote.note_3.set_length(7)
        self.assertEqual(TestNote.note_3.length, 7)
        # check that set_length raises value errors
        with self.assertRaises(ValueError):
            TestNote.note_3.set_length("apple")

if __name__ == '__main__':
    unittest.main()
