import pyaudio
import numpy as np
from collections import OrderedDict
try:
    import Image 
except ImportError:
    from PIL import Image

im = Image.open("wfc/Images/1_hog_2_166f5a8c-2a02-4b7a-9042-3c72868f4b13.png")
background = (0,0,0)

duration = 2     #length to play each pixel for
volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer

#Here's all the 
od = OrderedDict()
od['A'] = 220.000
od['A#'] = 233.080
od['B'] = 246.94
od['C'] = 261.625
od['C#'] = 277.185 
od['D'] = 293.665
od['D#'] = 311.125
od['E'] = 329.625
od['F'] = 349.23
od['F#'] = 369.995
od['G'] = 391.995
od['G#'] = 415.305
od['a'] = 440.0
od['a#'] = 466.16
od['b'] = 493.88
od['c'] = 523.25
od['c#'] = 554.37
od['d'] = 587.33
od['d#'] = 622.25
od['e'] = 659.25
od['f'] = 698.46
od['f#'] = 739.99
od['g'] = 783.99
od['g#'] = 830.61
odl = list(od.items())

def make_note(fs,duration,f):
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
    return samples

def make_chord(ratios,fs,duration,f):
    chord = make_note(fs,duration,0)
    for r in ratios:
        chord = sum([chord,make_note(fs,duration,f*r/ratios[0])])
    return chord

def make_chrom_chord(notes,fs,duration): 
    chord = make_note(fs,duration,0)
    for n in notes:
        chord = sum([chord,make_note(fs,duration,odl[n][1])])
    return chord

def make_scale_chord(notes,fs,duration):
    #make scale 
    keys = ['A','B','C#','D','E','F#','G#','a','b','c#','d','e','f#','g#']
    Amaj = OrderedDict((k,od[k]) for k in keys if k in od)
    Amajl = list(Amaj.items())

    chord = make_note(fs,duration,0)
    for n in notes: 
        chord = sum([chord,make_note(fs,duration,Amajl[n][1])])
    return chord

def stop():
    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == "__main__":

    p = pyaudio.PyAudio()
    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)
    pixels = list(im.getdata())
    width, height = im.size

    pix = im.load()
    roll = np.zeros((width,height))

    for i in range(width):
        for j in range(height):
            #create a matrix to iterate on
            if pix[i,j] != background:
                roll[i][j] = 1
        print("\n")
    
    #sound it out!
    for i in range(width):
        chord = []
        for j in range(height):
            if roll[i][j]:
                chord.append(j+1)
        print(chord)
        #harmonics
        #A = make_chord(chord,fs,duration,440)
        #from chromatic
        A = make_chrom_chord(chord,fs,duration)
        #from Amaj scale
        #A = make_scale_chord(chord,fs,duration)

        stream.write(volume*A)


    stop()    


