from notefrequencies import note_dct
import numpy as np

class Note:
    def __init__(self, name=None, freq=None, length=None, volume=None):
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
                print("unrecognized freq")
        # if no frequency or invalid frequency: profiles note by name
        if not freq:
            if name:
                if not name in note_dct.keys():
                    name = "A4"
                freq = note_dct[name]
            else:
                name = "A4"
                freq = note_dct[name]

        self._name = name
        self._freq = freq
        self.length = length if length else 1.0 # default 1 second
        self.volume = volume if volume else .5 # default speaking voice

    # TODO: Make a note parser with regex
    # def parse(self, name):
    #     for note in note_dct.keys():
    #
    #     if note_name:
    #         digit = name[-1]
    #         if digit.isdigit():
    #             digit = int(digit)
    #             digit = max(min(digit, 8), 0)
    #         else:
    #             digit = 4
    #         return note_name[:-1] + str(digit)
    #     else:
    #         return "A4" # default to A4 = 440hz

    ### get methods ###
    def get_name(self): return self._name
    def get_freq(self): return self._freq
    def get_octave(self): return int(self._name[-1])
    # length and volume are intended to be public so
    # get methods are only here for uniformity
    def get_length(self): return self.length
    def get_volume(self): return self.volume

    def samples(self, fs=44100):
        length = self.length   # in seconds, may be float
        freq = self._freq         # sine frequency, Hz, may be float
        samples = (np.sin(2*np.pi*np.arange(fs*length)*freq/fs)).astype(np.float32)
        return samples

    # Set methods to easily change length and volume
    def set_length(self, length):
        length = abs(float(length))
        self.length = length

    def set_volume(self, volume):
        try:
            volume = abs(float(volume))
            self.volume = volume
        except ValueError:
            print("parameter volume must be 0.0 to 1.0")

    ### comparison methods ###
    # TODO: make these return false if wrong type comparison
    def __lt__(self, other): return self._freq < other._freq
    def __le__(self, other): return self._freq <= other._freq
    def __eq__(self, other): return self._freq == other._freq
    def __ne__(self, other): return self._freq != other._freq
    def __gt__(self, other): return self._freq > other._freq
    def __ge__(self, other): return self._freq >= other._freq
    ## returns true if notes are equal, regardless of octave
    def equals(self, other):
        try:
            return self._name[:-1] == other.get_name()[:-1]
        except AttributeError:
            print("parameter other must be class: Note")

    ### to string method ###
    def __str__(self): return self._name
