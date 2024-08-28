# beetlebug
This project involves audio visualization through the traditional discrete fourier transform of raw audio data.

While not generally necessary, the creation of the transform and the displaying of the visualizer are in seperate files, music.py and play.py respectively.

Finished visualizations are stored in csv files (too large to upload to github), which are then read by play.py. Running music.py with the accompanying mp3 file in the repo will produce a functional 15 fps visualization. Note that play.py is set to use visualizeV8.csv, as many iterations of the transform's format were created during development. Change this to visualize.csv or change the csv file's name to run properly.

Installation of pydub is necessary to run this project, a slightly more complicated process than most modules.
