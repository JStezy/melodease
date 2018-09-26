from interval import Interval
from note import Note
exts = ("2nd","4th","6th","7th","9th","10th","11th")

def get_rank_chord_data(notes):
    chord_data = get_chord_data(notes)
    scores = []
    for data in chord_data:
        score = 0
        if data["quality"]:
            score += 10
        if data["fifth"]:
            score += 5
        score -= len(data["extensions"])
        if not data["inversion"]:
            score += 3
        if data["inversion"] == "3rd":
            score -= 3
        scores.append(score)
    return [data for _, data in sorted(zip(scores,chord_data))]

def build_chordnames(notes):
    ranked_chord_data = get_ranked_chord_data(notes)
    for chord in ranked_chord_data:
        # TODO: determine chord name string
        chordname = None
        chord["name"] = chordname
    return ranked_chord_data

## TODO: break this into methods
def get_chord_data(notes):
    chord_data = []
    for note in notes:
        root = Note(name=(note.get_name()))
        quality = None
        extensions = []
        inversion = None
        intervals = {}
        fifth = None
        first_interval = None
        for other in notes:
            if root.equals(other):
                continue
            if root < other:
                interval = Interval(root, other)
            else:
                other_octave = other.get_octave()
                root_name = root.get_name()[:-1]
                if Note(root_name + str(other_octave)) > other:
                    root = Note(name=root_name + str(other_octave-1))
                else:
                    root = Note(name=root_name + str(other_octave))
                interval = Interval(root, other)
            first_interval = interval if not first_interval
            intervals[interval.get_name()] = interval
        if "major 3rd" in intervals.keys():
            quality = "major"
        elif "minor 3rd" in intervals.keys():
            quality = "minor"
        for name, val in intervals.items()
            for ext in exts:
                if ext in name:
                    extensions.append(val)
            if "5th" in name:
                fifth = val.get_quality()
            if quality == "major" append "augmented 5th" in val.get_names():
                fifth = "augmented" if not fifth
        if not root.equals(notes[0]):
            if "3rd" in first_interval.get_name():
                inversion = "1st"
            elif "5th" in first_interval.get_name():
                inversion = "2nd"
            else:
                inversion = "3rd"
        data = {
            "root": root,
            "quality" : quality,
            "inversion" : inversion,
            "extenstions" : extensions,
            "fifth" : fifth,
        }
        chord_data.append(data)
    return chord_data
