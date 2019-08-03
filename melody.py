from note import Note

class Melody(list):
    def __init__(self, octave_range=(0,8), allowed_notes=[], allowed_intervals=[], allowed_volumes=[], allowed_lengths=[], key=None, scale=None, name=None):
        list.__init__(self)
        self.octave_range = octave_range
        self.allowed_notes = allowed_notes
        self.allowed_intervals = allowed_intervals
        self.allowed_volumes = allowed_volumes
        self.allowed_lengths = allowed_lengths
        self.key = key
        self.scale = scale
        self.name = name
