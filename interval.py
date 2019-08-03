from intervalnames import interval_list
from note import Note
from math import log2, pow

class Interval:

    def __init__(self, note_1, note_2=None, halfsteps=None):
        if note_2:
            halfsteps = None
            self._halfsteps = self.compute_halfsteps(note_1, note_2)
        if halfsteps:
            self._halfsteps = halfsteps
            note_2 = self.compute_note_2(note_1, halfsteps)
        else:
            note_2 = Note(name=note_1.get_name())
        steps = self._halfsteps
        num_octaves = 0
        while steps > 12:
            steps -= 12
            num_octaves += 1

        self._data = interval_list[steps]
        # data fields include:
        # halfsteps, int, flat, quality, dissonant, dissonance
        self._octaves = num_octaves
        self._topnote = max(note_1, note_2)
        # switch order in case they are equal so that
        # each note points to a separate Note instance
        self._bottomnote = min(note_2, note_1)
        self._notes = (self._topnote, self._bottomnote)

    ### get methods to access attributes ###

    # returns the number of half steps between note_1 and note_2
    def compute_halfsteps(self, note_1, note_2):
        multiplier = note_1.get_freq()/note_2.get_freq()
        if multiplier < 1:
            multiplier = 1/multiplier
        halfsteps = round(log2(multiplier)*12)
        return halfsteps

    def compute_note_2(self, note_1, halfsteps):
        multiplier = pow(2,(halfsteps/12))
        freq_2 = note_1.get_freq()*multiplier
        note_2 = Note(freq=freq_2)
        return note_2

    # GET METHODS
    def get_halfsteps(self): return self._halfsteps
    # returns the number of additional octaves of separation
    # between the notes unaccounted for by the interval name
    def get_octaves(self): return self._octaves
    # returns the top note
    def get_topnote(self): return self._topnote
    # returns the bottom note
    def get_bottomnote(self): return self._bottomnote
    # returns quality of the interval
    def get_quality(self): return self._data['quality']
    # returns interval numeral
    def get_int(self): return self._data['int']
    # returns whether interval is flat
    def is_flat(self): return self._data['flat']
    # returns whether interval is dissonant
    def is_dissonant(self): return self._data['dissonant']
    # returns dissonance level (0,1,2 or 3)
    def dissonance(self): return self._data['dissonance']
    # returns quality
    def quality(self): return self._data['quality']


    ########################################

    # to string uses the first name in names
    def __str__(self):
        number = self.get_int()
        if 2 <= number <= 7:
            return "{0} {1}".format(self.quality(), number)
        else:
            return self.quality()

    # compares by distance between notes
    def __lt__(self, other): return self._halfsteps < other._halfsteps
    def __le__(self, other): return self._halfsteps <= other._halfsteps
    def __eq__(self, other): return self._halfsteps == other._halfsteps
    def __ne__(self, other): return self._halfsteps != other._halfsteps
    def __gt__(self, other): return self._halfsteps > other._halfsteps
    def __ge__(self, other): return self._halfsteps >= other._halfsteps

    # Checks if the notes in self and other are the same.
    # This is a more rigorous comparison than the __eq__
    # method which only ensures that the intervals are equal.
    def equals(self, other): return self._notes == other._notes
