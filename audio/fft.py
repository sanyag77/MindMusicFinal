import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile # get the api
import numpy as np
fs, data = wavfile.read('imperial_march.wav') # load the data
#a = data.T[0] # this is a two channel soundtrack, I get the first track -- FOR TWO CHANNEL TRACKS
#data=[(ele/2**16.)*2-1 for ele in data] # this is 8-bit track, b is now normalized on [-1,1)
audiofft = fft(data) # calculate fourier transform (complex numbers list)
d = int(len(audiofft)/2)  # you only need half of the fft list (real signal symmetry)

#DECLARE GLOBALS
global sub_bass_max, bass_max, low_midrange_max, midrange_max, upper_midrange_max, presence_max, brilliance_max
global sub_bass_beat, bass_beat, low_midrange_beat, midrange_beat, upper_midrange_beat, presence_beat, brilliance_beat
sub_bass_max = 10
bass_max = 10
low_midrange_max = 10
midrange_max = 10
upper_midrange_max = 10
presence_max = 10
brilliance_max = 10
sub_bass_beat = False
bass_beat = False
low_midrange_beat = False
midrange_beat = False
upper_midrange_beat = False
presence_beat = False
brilliance_beat = False


#DISPLAY INPUT SIGNAL AND FOURIER TRANSFORM SPECTRUM
plt.plot(data)
plt.show()
plt.plot(abs(audiofft[:(d-1)]),'r') 
plt.show()

def beat_detect(data,fft):
    freqs = fs*np.arange(len(data)/2)/len(data)
    print(max(fft))
    # Frequency Ranges for each important audio group
    sub_bass_indices = [idx for idx,val in enumerate(freqs) if val >= 20 and val <= 60]
    bass_indices = [idx for idx,val in enumerate(freqs) if val >= 60 and val <= 250]
    low_midrange_indices = [idx for idx,val in enumerate(freqs) if val >= 250 and val <= 500]
    midrange_indices = [idx for idx,val in enumerate(freqs) if val >= 500 and val <= 2000]
    upper_midrange_indices = [idx for idx,val in enumerate(freqs) if val >= 2000 and val <= 4000]
    presence_indices = [idx for idx,val in enumerate(freqs) if val >= 4000 and val <= 6000]
    brilliance_indices = [idx for idx,val in enumerate(freqs) if val >= 6000 and val <= 20000]
   
    plotmidrange = [0]*len(freqs)
    for i in enumerate(freqs):
        idx,val = i
        if val>=4000 and val<=6000:
            plotmidrange[idx] = 1
    plt.plot(plotmidrange)
    plt.show()


    sub_bass = np.max(fft[sub_bass_indices])
    bass = np.max(fft[bass_indices])
    low_midrange = np.max(fft[low_midrange_indices])
    midrange = np.max(fft[midrange_indices])
    upper_midrange = np.max(fft[upper_midrange_indices])
    presence = np.max(fft[presence_indices])
    brilliance = np.max(fft[brilliance_indices])

    global sub_bass_max, bass_max, low_midrange_max, midrange_max, upper_midrange_max, presence_max, brilliance_max
    global sub_bass_beat, bass_beat, low_midrange_beat, midrange_beat, upper_midrange_beat, presence_beat, brilliance_beat
    sub_bass_max = max(sub_bass_max, sub_bass)
    print("Max:", sub_bass_max)
    print("Bass:", sub_bass)

    #bass_max = max(bass_max, bass)
    low_midrange_max = max(low_midrange_max, low_midrange)
    midrange_max = max(midrange_max, midrange)
    upper_midrange_max = max(upper_midrange_max, upper_midrange)
    presence_max = max(presence_max, presence)
    brilliance_max = max(brilliance_max, brilliance)

    if sub_bass >= sub_bass_max*.9 and not sub_bass_beat:
        sub_bass_beat = True
        print("Sub Bass Beat")
    elif sub_bass < sub_bass_max*.3:
        sub_bass_beat = False

    if bass >= bass_max*.9 and not bass_beat:
        bass_beat = True
        print("Bass Beat")
    elif bass < bass_max*.3:
        bass_beat = False

    if low_midrange >= low_midrange_max*.9 and not low_midrange_beat:
        low_midrange_beat = True
        print("Low Midrange Beat")
    elif low_midrange < low_midrange_max*.3:
        low_midrange_beat = False

    if midrange >= midrange_max*.9 and not midrange_beat:
        midrange_beat = True
        print("Midrange Beat")
    elif midrange >= midrange_max*.3:
        midrange_beat = False

    if upper_midrange >= upper_midrange_max*.9 and not upper_midrange_beat:
        upper_midrange_beat = True
        print("Upper Midrange Beat")
    elif upper_midrange < upper_midrange_max*.3:
        upper_midrange_beat = False

    if brilliance >= brilliance_max*.9 and not brilliance_beat:
        brilliance_beat = True
        print("Brilliance Beat")
    elif brilliance < brilliance_max*.3:
        brilliance_beat = False

    if presence >= presence_max*.9 and not presence_beat:
        presence_beat = True
        print("Presence Beat")
    elif presence < presence_max*.3:
        presence_beat = False


    primary_freq = freqs[np.argmax(fft)]
    # print("Primary Frequency: ", primary_freq)
beat_detect(data,audiofft)
