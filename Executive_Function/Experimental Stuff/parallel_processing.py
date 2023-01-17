#This stuff works! add the display and strean amd you're done!


import threading

import concurrent.futures
from threading import Event
import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pandas as pd
from pylsl import StreamInlet, resolve_stream
from matplotlib import pyplot as plt
import random
import time
from tkinter import *
from PIL import ImageTk, Image


start = time.perf_counter()


def collect_stream(event):

    print("collecting stream...")
         
    finished = False

    streams = resolve_stream()
    inlet = StreamInlet(streams[0])

    # initialize the colomns of your data and your dictionary to capture the data.
    columns=['Time','FZ', 'C3', 'CZ', 'C4', 'PZ', 'PO7', 'OZ', 'PO8','AccX','AccY','AccZ','Gyro1','Gyro2','Gyro3', 'Battery','Counter','Validation']
    data_dict = dict((k, []) for k in columns)


    while True:   # if we collected all the samples we want, we stop

        # get the streamed data. Columns of sample are equal to the columns variable, only the first element being timestamp
        # concatenate timestamp and data in 1 list
        data, timestamp = inlet.pull_sample()
        all_data = [timestamp] + data

        # updating data dictionary with newly transmitted samples   
        i = 0
        for key in list(data_dict.keys()):            # this loop causes delay -> maybe think of a better option
            data_dict[key].append(all_data[i])
            i = i + 1

        
        if event.is_set():

            data_df = pd.DataFrame.from_dict(data_dict)
            data_df.to_csv("EEG_CleanStream_" + str( time.strftime("%H") ) + "h_" + str( time.strftime("%M") ) + "m_" + str( time.strftime("%S") ) + "s" + ".csv", index = False)
            
            return "stream collection ended"
            
















 
N_CUES = 50           # default is 50
BLANK_DUR_ms = 1000
CUE_DUR_ms = 125

# ------------------------------------ makng a list of random cues (50 in total: 35 go, 15 no-go) -----------------------------

# put cues in a randomized order

list_cues_str= []
 
for i in range(35):                 # default is 35

    list_cues_str.append("go")


for i in range(15):               # default is 15

    list_cues_str.append("no-go")


random.shuffle( list_cues_str )

#---------------------------------------------------------------------------------------






#---------------------------make a list with the sample indexes at which to display stuff-----------

indexes_cue = []  #first 1000, then + 1125 # 1000, 1000 + 125 + 1000, 1000 + 125 + 1000 + 
indexes_blank = [] #first 0, then + 1125 # 0, 0 + 1000 + 125, 0 + 1000 + 125...

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
    
im_blank = ImageTk.PhotoImage( Image.open( "C:/Users/user1/Desktop/CogNeuro_redesign_spring_2023-main/photos_calibration/blank_screen_1080x1920.png" ) )
im_blue = ImageTk.PhotoImage( Image.open("C:/Users/user1/Desktop/CogNeuro_redesign_spring_2023-main/photos_calibration/blue_circle_big.png" ) )
im_green = ImageTk.PhotoImage( Image.open( "C:/Users/user1/Desktop/CogNeuro_redesign_spring_2023-main/photos_calibration/green_circle_big.png" ) )

label_blank = Label( image = im_blank )
label_blue = Label( image = im_blue )
label_green = Label( image = im_green )



my_canvas = Canvas( root, width = 1920, height = 1080 )        # change this based on display resolution
my_canvas.pack(fill = "both", expand = True)


#------------------------------------------------------------------------------------------------









event = threading.Event()

with ThreadPoolExecutor() as executor:                        # works

    f1 = executor.submit(collect_stream, event)

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

            my_canvas.create_image( 0, 0, image = im_blank, anchor = "nw" )
            root.update_idletasks()
            root.update() # every second call, a nasty window appears, even if I just run this one

            time_end_display_script = time.time()
            list_seconds_it_takes_to_run_display_script.append( time_end_display_script - time_start_display_script )


        elif i_sample in indexes_cue:


            if list_cues_str[i_cue] == "go":

                time_start_display_script = time.time()

                my_canvas.create_image( 0, 0, image = im_blue, anchor = "nw" )
                root.update_idletasks()
                root.update()

                time_end_display_script = time.time()
                list_seconds_it_takes_to_run_display_script.append( time_end_display_script - time_start_display_script )


            if list_cues_str[i_cue] == "no-go":

                time_start_display_script = time.time()

                my_canvas.create_image( 0, 0, image = im_green, anchor = "nw" )
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
    

    event.set()
    print( "display ended" )

    print(f1.result() )








    time_end = time.time()

    seconds_it_took_to_collect_data = time_end - time_start
    data_df = pd.DataFrame.from_dict(data_dict)
    data_df.to_csv("EEG_MissingSamples_" + str( time.strftime("%H") ) + "h_" + str( time.strftime("%M") ) + "m_" + str( time.strftime("%S") ) + "s" + ".csv", index = False)

    np.save( file = "dirty_annotations_array_" + str( time.strftime("%H") ) + "h_" + str( time.strftime("%M") ) + "m_" + str( time.strftime("%S") ) + "s" + ".npy", arr = annotations_aray )


    # making clean annotations

        # figuring out how many samples were lost in the process, then shifting the annotations by that number of samples

    list_lost_samples = [ int(list_seconds_it_takes_to_run_display_script[i] * 1000 // 4) for i in range(len(list_seconds_it_takes_to_run_display_script)) ]
    
    clean_indexes_cue = indexes_cue

    sum_lost_samples = 0

    for i in range(len(list_lost_samples)):

        sum_lost_samples += list_lost_samples[i]
        clean_indexes_cue[i] += sum_lost_samples

    clean_annotations_aray = np.stack( [ list_cues_str, clean_indexes_cue ], axis = 1)
    np.save( file = "clean_annotations_array_" + str( time.strftime("%H") ) + "h_" + str( time.strftime("%M") ) + "m_" + str( time.strftime("%S") ) + "s" + ".npy", arr = clean_annotations_aray )



    # -----------------------


    
    np.save( file = "dirty_annotations_array_" + str( time.strftime("%H") ) + "h_" + str( time.strftime("%M") ) + "m_" + str( time.strftime("%S") ) + "s" + ".npy", arr = annotations_aray )

    time_file = "time_txt_" + str( time.strftime("%H") ) + "h_" + str( time.strftime("%M") ) + "m_" + str( time.strftime("%S") ) + "s" + ".txt"

    with open(time_file, 'w') as f:
        f.write('seconds it took to collect data =' + str( seconds_it_took_to_collect_data) + "\n" + "list of time it takes to display one cue:" + str( list_seconds_it_takes_to_run_display_script ) )



'''

after we have EEG_clean_signal and EEG_missing_samples and time_txt,

we can move the annotations by a number of samples deteremined by how 
much it took for each cue to be displayed
-> then use EEG_clean_signal as our EED samples for analysis

MAKE SURE EEG_clean and EEG_missing_samples have the same shape, so you know they're collecting the same thing





'''
