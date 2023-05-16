import wave
import struct
import sys
import matplotlib.pyplot as plt
file = sys.argv[1]
print(file)
def pcm_channels(wave_file):
    stream = wave.open(wave_file,"rb")

    num_channels = stream.getnchannels()
    sample_rate = stream.getframerate()
    sample_width = stream.getsampwidth()
    num_frames = stream.getnframes()

    raw_data = stream.readframes( num_frames )
    stream.close()

    total_samples = num_frames * num_channels

    if sample_width == 1:
        fmt = "%iB" % total_samples
    elif sample_width == 2:
        fmt = "%ih" % total_samples
    else:
        raise ValueError("Only supports 8 and 16 bit audio formats.")

    integer_data = struct.unpack(fmt, raw_data)
    del raw_data

    channels = [ [] for time in range(num_channels) ]

    for index, value in enumerate(integer_data):
        bucket = index % num_channels
        channels[bucket].append(value)

    return (sample_rate/10, channels)

sampleN, bitarray = pcm_channels(file)



#references
"""
https://www.it-jim.com/blog/audio-processing-basics-in-python/
https://mziccard.me/2015/05/28/beats-detection-algorithms-1/
"""
#beat detection algorithm begins

def normalize(bitarray):
    bitarray = bitarray[0]
    for i in range (len(bitarray)):
        bitarray[i] = bitarray[i]/32766
    return bitarray

bitarray = normalize(bitarray)

def avgEnergy(bitarray):
    start = -1
    total = 0
    energyList = []
    for i in range(len(bitarray)):
        start+=1
        if (start%sampleN!=0):
            total += bitarray[start]**2
        else:
            energyList.append(total/sampleN)
            total = 0
    return (sum(energyList)/len(energyList), energyList)

def variance(energyArray, avg):
    varianceList =[]
    for i in range(len(energyArray)):
        varianceList.append((avg-energyArray[i])**2)
    return varianceList

avgE, energyList = avgEnergy(bitarray)
varianceList = [-0.0000015 * i + 1.5142857 for i in variance(energyList, avgE)]

def detectBeat(energyList, varianceList, avgE):
    beatTimes = []
    count = 0
    for i in range(len(energyList)):
        if energyList[i] > avgE*varianceList[i]:
            beatTimes.append(0)
            count+=1
        else:
            beatTimes.append(None)
    return (beatTimes, count)
beatTimes, count =detectBeat(energyList, varianceList,avgE)
detectedTempo = count/60
print(detectedTempo)
# visualize the waaave :)
x_axis = [i for i in range(len(energyList))]
plt.plot(energyList)
plt.scatter(x_axis, beatTimes)
plt.show()
