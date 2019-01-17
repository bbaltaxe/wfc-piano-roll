import matplotlib.pyplot as plt
import pyaudio
import numpy as np

p = pyaudio.PyAudio()

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 1.0   # in seconds, may be float
f = 440.0        # sine frequency, Hz, may be float

def make_note(fs,duration,f):
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
    return samples

def make_chord(ratios,fs,duration,f):
    chord = make_note(fs,duration,0)
    for r in ratios:
        chord = sum([chord,make_note(fs,duration,f*r/ratios[0])])
    return chord
        

# generate samples, note conversion to float32 array
#samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# play. May repeat with different volume values (if done interactively) 
A = make_chord([],fs,duration,440)
#plt.plot(A[10:])
#plt.show()
stream.write(volume*A)
A = make_note(fs,duration,440)
stream.write(volume*A)
A = make_note(fs,duration,440*3)
stream.write(volume*A)
A = make_note(fs,duration,440*5)
stream.write(volume*A)
stream.stop_stream()
stream.close()

p.terminate()
