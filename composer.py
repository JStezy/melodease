from note import Note
from interval import Interval
from melody import Melody
from keys import key_list, scales
from random import choice, randint

class Composer:

    def __init__(self, intro=True, smart=True, compositions=[]):
        if intro:
            print("Hello, I am your composer.")
            print("Use Composer.help() to see what I can do.")
            print("To supress this intro in the future, construct me with intro=False")
            self.compositions = compositions
            self.smart = smart

    def generate_melody(self, intro=True):
        melody = Melody()
        if intro:
            print("I will now write a melody according to your constraints.")
            print("By default, I simplify the process with generic questions and implied constraints.")
            print("If you would like more control, call this function with smart=False")
            print("After any prompt, type \"exit\" to cancel this melody.")
            print("To supress this intro, set intro=False")
        exit = False
        if self.smart:
            # determine melody or bassline
            # exit, bassline = self.question("Is this a bassline? (y/n)", ["y","n"])
            # if exit:
            #     return
            # if bassline == "y":
            #     melody.octave_range = (1,5)
            # if bassline == "n":
            #     melody.octave_range = (4,8)
            melody.octave_range = (3,5)
            # determine key
            exit, key = self.question("What key is this in? (ex: A, Am, D#, Ebm etc.)", key_list)
            if exit:
                return
            melody.key = key
            # determine scale
            scale_options = self.get_scale_options(key)
            print("Choose a scale by typing the number:")
            for i, scale in enumerate(scale_options):
                print("{0}. {1}".format(i+1,scale))
            exit, scale = self.question("Scale Choice: ", list(map(str, range(1,len(scale_options)+1,1))))
            if exit:
                return
            melody.scale = scale_options[int(scale)-1]
        melody = self.select_notes(melody)
        self.compositions.append(melody)
        return melody

    # INTERNAL HELPERS

    def question(self, prompt, allowed):
        resp = ""
        allowed.append("exit")
        while not resp in allowed:
            resp = input(prompt)
        exit = resp == "exit"
        return exit, resp

    def get_scale_options(self, key):
        scale_options = []
        major = not "m" in key
        for scale, info in scales.items():
            if major and info['major']:
                scale_options.append(scale)
            if not (major or info['major']):
                scale_options.append(scale)
        return scale_options


    def select_notes(self, melody):
        allowed_notes = []
        tonic = melody.key
        if "m" in melody.key:
            tonic = tonic[0:-1]
        allowed_notes.append(tonic)
        start_note = tonic + '4' # arbitrary octave for computing notes
        current_note = Note(name=start_note)
        scale_steps = scales[melody.scale]['halfsteps']
        for steps in scale_steps:
            interval = Interval(note_1=current_note, halfsteps=steps)
            next_note = interval.get_topnote()
            note_name = next_note.get_name()[0:-1]
            allowed_notes.append(note_name)
            current_note = next_note
        octave = randint(melody.octave_range[0], melody.octave_range[1])
        for x in range(16):
            # pick note and add to melody
            note_name = choice(allowed_notes)
            note_name += str(octave)
            melody.append(Note(name=note_name))
            # pick next octave in range
            bottom = max(melody.octave_range[0], octave - 1)
            top = min(melody.octave_range[1], octave + 1)
            if randint(1,10) < 2:
                octave = choice([bottom, top])
        return melody
