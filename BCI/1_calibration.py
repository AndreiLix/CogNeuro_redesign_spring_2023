import numpy as np
import pandas as pd
from pylsl import StreamInlet, resolve_stream
from matplotlib import pyplot as plt
import random
import time
from tkinter import *
from PIL import ImageTk, Image



 
N_CUES = 74         # default is 74
BLANK_DUR_ms = 500
CUE_DUR_ms = 1000

# ------------------------------------ makng a list of random cues (50 in total: 37 down, 37 right) -----------------------------

# put cues in a randomized order

list_cues_str= []
 
for i in range(37):                 # default is 37

    list_cues_str.append("down")


for i in range(37):               # default is 37

    list_cues_str.append("right")


random.shuffle( list_cues_str )

#---------------------------------------------------------------------------------------






#---------------------------make a list with the sample indexes at which to display stuff-----------

indexes_cue = []  
indexes_blank = []

for i in range(N_CUES):
    
    indexes_cue.append( i * (BLANK_DUR_ms + CUE_DUR_ms) + BLANK_DUR_ms )
    indexes_blank.append( i * (BLANK_DUR_ms + CUE_DUR_ms) )

indexes_blank.append( N_CUES * (BLANK_DUR_ms + CUE_DUR_ms)  )        # because we want to end with a blank screen for 4 seconds

#----------------------------------------------------------


# we make annotations_array of shape (n_cues, 2) that holds the type of cue and its location in the samples

annotations_aray = np.stack( [ list_cues_str, indexes_cue ], axis = 1)





#----------------------------------- image related stuff -----------------------------------

root = Tk()

    # make sure to use png here
    
im_cross = ImageTk.PhotoImage( Image.open( "/home/andrei/Desktop/BCI_stuff/PIPELINE_space_invaders/photos_calibration/fixation_cross.png" ) )
im_down = ImageTk.PhotoImage( Image.open("/home/andrei/Desktop/BCI_stuff/PIPELINE_space_invaders/photos_calibration/down_arrow.png" ) )
im_right = ImageTk.PhotoImage( Image.open( "/home/andrei/Desktop/BCI_stuff/PIPELINE_space_invaders/photos_calibration/right_arrow.png" ) )

label_cross = Label( image = im_cross )
label_down = Label( image = im_down )
label_right = Label( image = im_right )



my_canvas = Canvas( root, width = 1920, height = 1080 )        # change this based on display resolution
my_canvas.pack(fill = "both", expand = True)


#------------------------------------------------------------------------------------------------













#-------------------------- the juicy part -----------------


# initialize the streaming layer
finished = False
streams = resolve_stream()
inlet = StreamInlet(streams[0])

# initialize the colomns of your data and your dictionary to capture the data.
columns=['Time','FZ', 'C3', 'CZ', 'C4', 'PZ', 'PO7', 'OZ', 'PO8','AccX','AccY','AccZ','Gyro1','Gyro2','Gyro3', 'Battery','Counter','Validation']
data_dict = dict((k, []) for k in columns)



i_sample = 0
i_cue = 0
time_start = time.time()

list_seconds_it_takes_to_run_display_script = []


while True:   # if we collected all the samples we want, we stop

    # get the streamed data. Columns of sample are equal to the columns variable, only the first element being timestamp
    # concatenate timestamp and data in 1 list
    data, timestamp = inlet.pull_sample()
    all_data = [timestamp] + data

    # updating data dictionary with newly transmitted samples   
    i = 0
    for bababowe in list(data_dict.keys()):            # this loop causes delay -> maybe think of a better option
        data_dict[bababowe].append(all_data[i])
        i = i + 1


    # ------------------ doing the display ----------------

    if i_sample in indexes_blank:

        time_start_display_script = time.time()

        my_canvas.create_image( 0, 0, image = im_cross, anchor = "nw" )
        root.update_idletasks()
        root.update() # every second call, a nasty window appears, even if I just run this one

        time_end_display_script = time.time()
        list_seconds_it_takes_to_run_display_script.append( time_end_display_script - time_start_display_script )


    elif i_sample in indexes_cue:


        if list_cues_str[i_cue] == "down":

            time_start_display_script = time.time()

            my_canvas.create_image( 0, 0, image = im_down, anchor = "nw" )
            root.update_idletasks()
            root.update()

            time_end_display_script = time.time()
            list_seconds_it_takes_to_run_display_script.append( time_end_display_script - time_start_display_script )


        if list_cues_str[i_cue] == "right":

            time_start_display_script = time.time()

            my_canvas.create_image( 0, 0, image = im_right, anchor = "nw" )
            root.update_idletasks()
            root.update()

            time_end_display_script = time.time()
            list_seconds_it_takes_to_run_display_script.append( time_end_display_script - time_start_display_script )


        i_cue += 1



    # -------------------------------------------------------

    #   # data is collected at 250 Hz. Let's stop data collection after 10 seconds. Meaning we stop when we collected 250*10 samples.
    #   if len(data_dict['Time']) >= 250*10:
    #      finished = True
        

    if i_sample == N_CUES * (BLANK_DUR_ms + CUE_DUR_ms) + BLANK_DUR_ms:

        break

    i_sample += 1 
    


#------------------ saving stuff ---------------


time_end = time.time()

seconds_it_took_to_collect_data = time_end - time_start
data_df = pd.DataFrame.from_dict(data_dict)
data_df.to_csv("EEGdata_" + str( time.strftime("%H") ) + "h_" + str( time.strftime("%M") ) + "m_" + str( time.strftime("%S") ) + "s" + ".csv", index = False)

np.save( file = "annotations_array_" + str( time.strftime("%H") ) + "h_" + str( time.strftime("%M") ) + "m_" + str( time.strftime("%S") ) + "s" + ".npy", arr = annotations_aray )

time_file = "time_txt_" + str( time.strftime("%H") ) + "h_" + str( time.strftime("%M") ) + "m_" + str( time.strftime("%S") ) + "s" + ".txt"

with open(time_file, 'w') as f:
    f.write('seconds it took to collect data =' + str( seconds_it_took_to_collect_data) + "\n" + "list of time it takes to display one cue:" + str( list_seconds_it_takes_to_run_display_script ) )
#-----------------------------------------------------------
