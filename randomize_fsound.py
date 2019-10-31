import random

def note_selector():
    note_selector = random.randint(1, 16)
    if note_selector == 1:
        note = "a"
    elif note_selector == 2:
        note = "b"
    elif note_selector == 3:
        note = "c"
    elif note_selector == 4:
        note = "d"
    elif note_selector == 5:
        note = "e"
    elif note_selector == 6:
        note = "f"
    elif note_selector == 7:
        note = "g"
    elif note_selector == 8:
        note = "A"
    elif note_selector == 9:
        note = "C"
    elif note_selector == 10:
        note = "D"
    elif note_selector == 11:
        note = "F"
    elif note_selector == 12:
        note = "G"
    elif note_selector == 13:
        note = "x"
    elif note_selector == 14:
        note = "K"
    elif note_selector == 15:
        note = "S"
    else:
        note = "r"
    return note

def volume_selector():
    volume_selector = random.randint(0, 15)
    if volume_selector == 10:
        volume = "a"
    elif volume_selector == 11:
        volume = "b"
    elif volume_selector == 12:
        volume = "c"
    elif volume_selector == 13:
        volume = "d"
    elif volume_selector == 14:
        volume = "e"
    elif volume_selector == 15:
        volume = "f"
    else:
        volume = str(volume_selector)
    return volume

def length_selector():
    length_selector = random.randint(1, 14)
    if length_selector == 3:
        length = "2"
    elif 4 < length_selector < 7:
        length = "4"
    elif length_selector == 7:
        length = "8"
    elif 8 < length_selector < 11:
        length = "f"
    elif 10 < length_selector < 13:
        length = "g"
    elif 12 < length_selector < 15:
        length = "t"
    else:
        length = str(length_selector)
    return length

def generate_note():
    note = note_selector()
    octave = str(random.randint(1, 7))
    length = length_selector()
    volume = volume_selector()
    if note == "x":
        note_style = note + "-" + length + volume
    elif note == "K" or note == "S" or note == "r":
        note_style = note + "-" + length
    else:
        note_style = note + octave + length + volume
    return note_style

file = open('f_random.fss', 'w')
init_tempo = random.randint(1, 100)
song_length = random.randint(12, 1024)
set_loop = False
file.write("{}\n".format(str(init_tempo)))
file.write("> generated with randomize_fsound.py\n")
while song_length > 0:
    style_selector = random.randint(0, 100)
    if style_selector < 40:
        row_note = generate_note()
        file.write("{}\n".format(row_note))
    elif 39 < style_selector < 50:
        if not set_loop:
            file.write("LS\n")
            set_loop = True
        elif set_loop:
            loops = random.randint(2, 9)
            file.write("L{}\n".format(loops))
            set_loop = False
    elif 49 < style_selector < 60:
        volume = volume_selector()
        file.write("v{}\n".format(volume))
    elif 59 < style_selector < 65:
        new_tempo = random.randint(1, 100)
        file.write("t{}\n".format(new_tempo))
    elif style_selector > 64:
        row_note = generate_note()
        file.write("{}\n".format(row_note))
    else:
        file.write("> this is an error handling message\n")
    song_length = song_length-1
if set_loop:
    loops = random.randint(2, 9)
    file.write("L{}\n".format(loops))
    set_loop = False
file.close()