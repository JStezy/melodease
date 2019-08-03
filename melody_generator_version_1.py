from note import Note
from interval import Interval
from random import choice
import pyaudio
from composer import Composer
from notefrequencies import note_dct

import numpy as np

p = pyaudio.PyAudio()
fs = 44100       # sampling rate, Hz, must be integer

# 
songwriter = Composer()
melody = songwriter.generate_melody()
# tempo = 2 # beats/second
# melody = []
# random_note_names = []
# middle_notes = [k for k in note_dct.keys() if 3 <= int(k[-1]) <= 5]
# for x in range(50):
#     random_note_names.append(choice(middle_notes))
#
# start_note = Note()
# # current_note = Note(name=random_note_names[0])
# length = 1 # 16th note
# for note_name in random_note_names:
#     next_note = Note(name=note_name)
#     test_interval = Interval(start_note, next_note)
#     dis = test_interval.dissonance()
#     if dis<3:
#         next_note.set_length(length)
#         melody.append(next_note)
#         # current_note = next_note
#         length = 1
#     else:
#         length += 1





# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# play. May repeat with different volume values (if done interactively)
for note in melody:
    print(note)
    stream.write(note.get_volume()*note.samples(fs))

stream.stop_stream()
stream.close()

p.terminate()
