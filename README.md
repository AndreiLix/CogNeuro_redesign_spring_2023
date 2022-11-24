# CogNeuro_redesign_spring_2023
The repo containing the stuff we need for the Executive Function and BCI practical sessions.





Folders:

**Executive Function**
  - the odd-ball experimental setting (displays images for an odd-ball task while recording the EEG stream)
  - **outputs:**
      - .csv file containing the EEG stream during the odd-ball paradigm
      - numpy array of shape ( n_cues, 2 ) containing the type of cue and the location of its occurance in samples ([ ["go", 1000], ["no-go", 2125], ... ]  
**BCI**
  - platy Atari games with Motor Imagery
