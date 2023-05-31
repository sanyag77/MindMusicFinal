# MindMusicFinal
Instructions to Run Code

1. Install Emotiv Brain Control Interface (BCI)
2. Connect Cortex Apps and generate a client ID & Secret to input into the file ‘algorithm processing/eeg/python/sub_data.py’
3. Run file ‘webproject/eeg.py’ to generate data plot
4. Run file ‘algorithm processing/video/videotesting.py’ to generate posture analysis. The code will prompt for an input.
5. Run file ‘algorithm processing/audio/beat-detection.py’ to generate an audio graph. Ensure that the input file is located within the same directory.
6. The website can be seen locally upon viewing file ‘webproject/templates/index.html’ on local machine. However, the backend processes are not fully supported by the website currently
