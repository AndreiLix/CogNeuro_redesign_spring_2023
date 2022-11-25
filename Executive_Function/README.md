Problems:
- we lose between 2-15 samples for every call of the display function.
Solution:
Try this out: inside the while loop, if a cue must be displayed we split the processing to 2 cores-> one core takes care of the display function; the other: while the display function is running, add samples from the EEG stream to the dictionary, change i_samples accordingly.
