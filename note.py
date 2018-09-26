from notefrequencies import note_dct
import interval
class Note:
    def __init__(self, name=None, freq=None, length=None, velocity=None):
        # Always tries to profile note based on frequency first
        if freq:
            recognized = False
            for note, fq in note_dct.items():
                if abs(freq-fq) < .5:
                    recognized = True
                    freq = fq
                    name = note
            if not recognized:
                freq = None
        # if no frequency or invalid frequency: profiles note by name
        if not freq:
            if name:
                if not name in note_dct.keys():
                    name = self.parse(name) # parses name, defaults to A4 if unparsable
                freq = note_dct[name]
            else: # if no name given, defaults to A4
                name = "A4"
                freq = 440.0
        self._name = name
        self._freq = freq
        self.length = length if length else 1000 # default 1 second
        self.velocity = velocity if velocity else 72 # default speaking voice

    def parse(self, name):
        for note in note_dct.keys():
            if name.upper() in note:
                note_name = note
                break
        if note_name:
            digit = name[-1]
            if digit.isdigit():
                digit = int(digit)
                digit = max(min(digit, 8), 0)
            else:
                digit = 4
            return note_name[:-1] + str(digit)
        else:
            return "A4" # default to A4 = 440hz

    ### get methods ###
    def get_name(self): return self._name
    def get_freq(self): return self._freq
    def get_octave(self): return int(self._name[-1])
    # length and velocity are intended to be public so
    # get methods are only here for uniformity
    def get_length(self): return self.length
    def get_velocity(self): return self.velocity


    ### comparison methods ###
    def __lt__(self, other): return self.freq < other.freq
    def __le__(self, other): return self.freq <= other.freq
    def __eq__(self, other): return self.freq == other.freq
    def __ne__(self, other): return self.freq != other.freq
    def __gt__(self, other): return self.freq > other.freq
    def __ge__(self, other): return self.freq >= other.freq
    ## returns true if notes are equal, regardless of octave
    def equals(self, other):
        return self.name[:-1] == other.name[:-1]

    ### to string method ###
    def __str__(self): return self.name
