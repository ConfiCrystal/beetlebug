from pydub import AudioSegment
from pydub.playback import play
import csv
import threading
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import math

csv.field_size_limit(1000000000)

data = []
# Use the preproessed csv file here to view it
with open('visualizeV8.csv', mode ='r') as file:    
     csvFile = csv.DictReader(file)
     for line in csvFile:
          temp = line['dft']
          # remove brackets
          temp = temp[1:len(temp)-1]
          # extract list
          temp = temp.split(",")
          # convert to float
          for i in range(len(temp)):
              temp[i] = float(temp[i])
          data.append(temp)

length = len(data[0])
fig, ax = plt.subplots()
magnitude = 1200000
ax.set_ylim([-magnitude, magnitude])
x = range(length)
line, = ax.plot(x, data[0])

# Use the appropriate mp3 file here to play simultaneously
sound = AudioSegment.from_mp3("beetlebug.mp3")
music_thread = threading.Thread(target=play, args=(sound,))

def init():
     pass
def animate(i):
     global start
     if i == 0:
          start = time.perf_counter()
          music_thread.start()
     i = math.ceil((time.perf_counter() - start) * 15)
     line.set_ydata(data[i])
     return line,

animation = FuncAnimation(fig, animate, init_func=init, frames=len(data), interval=1000/15, repeat=False)
plt.show()  
