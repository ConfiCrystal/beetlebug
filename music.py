import pydub
from pydub import AudioSegment
import matplotlib.pyplot as plt
import numpy as np
import math
import cmath
import csv

def aquireAudio():
    # Change filename to change input audio
    # Preprocess fourier transform here (maybe unneccessary), view in play
    filename = "beetlebug.mp3"
    song = AudioSegment.from_mp3(filename)
    return song

def graph(data, title):
    xValues = range(len(data))
    plt.title(title)
    plt.plot(xValues, data)
    plt.show()

def dft(data):
    for i in range(len(data)):
        data[i] = complex(data[i], 0)
    return dftInner(data)

def dftInner(data):
    N = len(data)
    if N <= 1:
        return data
    
    even = data[0::2]
    odd = data[1::2]

    even = dftInner(even)
    odd = dftInner(odd)

    for i in range(N // 2):
        rotate = cmath.exp(-2 * math.pi * i * complex(0, 1) / N) * odd[i]
        data[i] = even[i] + rotate
        data[i + N // 2] = even[i] - rotate

    return data

def simplify(data):
    K = []
    skip = len(data) // 1000
    for i in range(0, len(data), skip):
        K.append(data[i])
    for i in range(len(K)):
        K[i] = K[i].real

    return K

song = aquireAudio()
data = song.get_array_of_samples().tolist()

sampleFactor = 20
sample = song.frame_rate // sampleFactor
buffer = [0 for i in range(sample)]
data = data + buffer

#graph(data, "Raw Audio")
stereo = 2
frameRate = 15
sampleSkip = stereo * song.frame_rate // frameRate
out = []
for frame in range(0, len(data) - sample, sampleSkip):
    section = data[frame : frame + sample : stereo]
    visualize = dft(section)
    visualize = simplify(visualize)
    out.append({'dft' : visualize})

with open('visualize.csv', 'w', newline='') as csvfile:
    fieldnames = ['dft']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(out)

print("Finished")

