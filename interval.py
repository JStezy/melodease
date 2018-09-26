from intervalnames import interval_list

class Interval:

    def __init__(self, note_1, note_2):
        self._halfsteps = self.get_halfsteps(note_1, note_2)
        steps = self._halfsteps
        num_octaves = 0
        while steps > len(interval_list):
            steps -= 12
            num_octaves += 1
        self._names = interval_list[steps]
        self._octaves = num_octaves
        self._topnote = max(note_1, note_2)
        # switch order in case they are equal so that
        # each note points to a separate Note instance
        self._bottomnote = min(note_2, note_1)
        self._quality = self._names[0].split[0]
        self._notes = (self._topnote, self._bottomnote)

    ### get methods to access attributes ###

    # returns the number of half steps between note_1 and note_2
    def get_halfsteps(self, note_1, note_2):
        multiplier = note_1.freq/note_2.freq
        multiplier = 1/multiplier if multiplier < 1
        halfsteps = round(log2(multiplier)*12)
        return halfsteps

    # returns interval names as a tuple of names
    def get_names(self): return self._names

    # returns the number of additional octaves of separation
    # between the notes unaccounted for by the interval name
    def get_octaves(self): return self._octaves

    # returns the top note
    def get_topnote(self): return self._topnote

    # returns the bottom note
    def get_bottomnote(self): return self._bottomnote

    # returns quality of the interval
    def get_quality(self): return self._quality

    ########################################

    # to string uses the first name in names
    def __str__(self):
        return self._names[0]

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
