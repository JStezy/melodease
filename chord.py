import interval
import  chordnames

class Chord:

    def __init__(self, notes):
        arpeggio = sorted(notes)
        core_notes = []
        for note in arpeggio:
            counted = False
            for other in core_notes:
                if note.equals(other):
                    counted = True
                    break
            if not counted:
                core_notes.append(note)
        chord_data = chordnames.build_chordnames(notes)
        self._names = [chord["name"] for chord in chord_data]
        self._name = self._names[0]
        self._quality = chord_data[0]["quality"]
        self._inversion = chord_data[0]["inversion"]
        
