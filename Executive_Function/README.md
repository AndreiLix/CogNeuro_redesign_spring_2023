How to use it:

- download the repo, unzip it, use it as working directory
- go to integration_oddball_and_EEGstream.py and change the paths of rhe images from "image related stuff" to the path of where your images are located

- run integration_oddball_and_EEGstream.py

    - a window will open with the oddball paradigm
    - put your index finger on the Spacebar and look at the screen
    - press the Spacebar key when you see the Blue circle (go cue). Don't do anything when you see the Green circle(no-go cue).
    - the window will close by itself after 3 minutes or so

- 3 files will be saved in the directory

    - EEGdata_HOUR_MINUTE_SECOND.csv
    
    - annotations_HOUR_MINUTE_SECOND.npy
    
        - numpy array shape (n_cues, 2) containing the type of cue displayed and it's location in the EEG samples
        - this annotation: ['go', '1000'] means that at the 1000th sample collected, the "go" cue was displayed; for a sampling frequency of 250Hz, this would mean that 4000 milliseconds after the start of the recording, the "go" cue was displayed;
        
    - time_it_takes_to_display_one_cue.txt







Problems:
- we lose between 2-15 samples for every call of the display function.


Solution:
- Try this out: inside the while loop, if a cue must be displayed we split the processing to 2 cores-> one core takes care of the display function; the other: while the display function is running, add samples from the EEG stream to the dictionary, change i_samples accordingly.
