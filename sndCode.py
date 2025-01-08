
"""

code to read sound files from drive and put some kind of reverb
on them, then listen to processed output

"""
# import every function from pyo package
from pyo import *

# server object starting that handles every sound related input-output task
s = Server().boot()
s.start()

# path of sound files on drive
path = 'C:/WAV_2.wav'
# path = 'D:/handel.wav'

# player object that actually reads and plays(if put .out() at the end of that)
# sound data from specified path and with sampling rate of server object
sf = SfPlayer(path)

# reverberation over sound file with shrouder method
b = Freeverb(sf,size=0.5,damp=0.5,bal=0.7,mul=0.5)

# reverberation over sound file with FDN method
c = WGVerb(sf,feedback=0.5,cutoff=5000,bal=0.7,mul=0.5).out()

# reverberation over sound file with convolution method, filter by which signal
# convolved is defined with SndTable object of input signal
d = Convolve(sf, SndTable(path),size=512,mul=1)

# spatial rendering with HRTF method
# azimuth and elevation degrees defined first
azi = Phasor(0.2, mul=360)
ele = Sine(0.1).range(-40, 90)
# HRTF method over sound file with gain=1 (mul) which can be low or high 
mv = HRTF(b, azi, ele, mul=0.5)

# Binaural spatial rendering over sound file
# azimuth and elevation spans defined first
# spn = Sine(0.3).range(0, 1)
spn = 0.3
# binaural rendering
bi = Binaural(sf, azi, ele, spn, spn, mul=0.5).out()
