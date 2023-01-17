# adaptation of display_oddball.py with emotional / neutral instead of go / no-go and mask instead of blank

# WORKS FOR NOW, BUT NO KEYBOARD PRESSESS IMPLEMENTED

from tkinter import *
from PIL import ImageTk, Image
import time
import random
import keyboard  # using module keyboard
import datetime 
import os
from PIL import Image
from IPython.display import Image, display
import PIL.Image
import random
#import cv2




N_CUES = 40
MASK_DUR_ms = 100 # HOW LONG DO WE WANT THE MASK TO LAST AFTER EACH EMOTIONAL/NEUTRAL IMAGE?
CUE_DUR_ms = 50 # CUE (IMAGE) LASTS 50ms, after which the noisy mask is displayed.

emotional = ['F01-Disgust-Apex.jpg',
 'F01-Anger-Apex.jpg',
 'M01-Anger-Apex.jpg',
 'F06-Pride-Apex.jpg',
 'F06-Fear-Apex.jpg',
 'F01-Embarrass-Apex.jpg',
 'M02-Embarrass-Apex.jpg',
 'M01-Joy-Apex.jpg',
 'M02-Joy-Apex.jpg',
 'M01-Disgust-Apex.jpg',
 'F06-Sad-Apex.jpg',
 'F01-Contempt-Apex.jpg',
 'F06-Anger-Apex.jpg',
 'M01-Embarrass-Apex.jpg',
 'F01-Sad-Apex.jpg',
 'M02-Contempt-Apex.jpg',
 'M02-Pride-Apex.jpg',
 'F06-Embarrass-Apex.jpg',
 'M02-Disgust-Apex.jpg',
 'F01-Fear-Apex.jpg',
 'M01-Pride-Apex.jpg',
 'M02-Fear-Apex.jpg',
 'F01-Joy-Apex.jpg',
 'F01-Pride-Apex.jpg',
 'F06-Disgust-Apex.jpg',
 'M01-Fear-Apex.jpg',
 'M02-Anger-Apex.jpg',
 'M01-Sad-Apex.jpg',
 'F06-Joy-Apex.jpg',
 'M01-Contempt-Apex.jpg',
 'F06-Contempt-Apex.jpg',
 'M02-Sad-Apex.jpg'] # the images directories should be adjusted according to who's running the script

neutral = ['M02-Neutral.jpg', 'M01-Neutral.jpg', 'F06-Neutral.jpg', 'F01-Neutral.jpg']

mask = "mask.png"

emotional_times = []
neutral_times = []

# ------------------------------------ makng a list of random cues (40 in total: 36 emotional, 4 neutral, 20 masks) -----------------------------

# put cues in a randomized order

list_cues_str = []
 
for i in range(32):                 

    list_cues_str.append("emotional")
    
for i in range(4):                 

    list_cues_str.append("neutral")
      

random.shuffle( list_cues_str )

#---------------------------------------------------------------------------------------

def average(lst):
    return (sum(lst) / len(lst))


#----------------------------------- image related stuff -----------------------------------

root = Tk()

    # make sure to use png here

#im_emotional = ImageTk.PhotoImage(PIL.Image.open(random.choice(emotional)))
#im_neutral = ImageTk.PhotoImage(PIL.Image.open(random.choice(neutral)))
#im_mask = ImageTk.PhotoImage(PIL.Image.open(mask))

#label_emotional = Label( image = im_emotional )
#label_neutral = Label( image = im_neutral )
#label_mask = Label( image = im_mask )



my_canvas = Canvas( root, width = 1920, height = 1080 )        # change this based on display resolution
my_canvas.pack(fill = "both", expand = True)



#----------------------------------------------------------


def show_mask(stimuli):
    while True:
        im_mask = ImageTk.PhotoImage(PIL.Image.open(mask))
        my_canvas.create_image( 0, 0, image = im_mask, anchor = "nw" )
        time.sleep(0.05)
        root.update_idletasks()
        root.update()
        i = datetime.datetime.now()
        if stimuli == "emotional" : # if key 'e' is pressed 
            keyboard.wait("e")
            q = datetime.datetime.now()
            time_t = (i-q).microseconds
            emotional_times.append(time_t)
            break
        elif stimuli == "neutral":
            keyboard.wait("n")
            q = datetime.datetime.now()
            time_t = (i-q).microseconds
            neutral_times.append(time_t)
            break
    


for i in range(len(list_cues_str)): 
    if list_cues_str[i] == "emotional":
        im_emotional = ImageTk.PhotoImage(PIL.Image.open(random.choice(emotional)))
        my_canvas.create_image( 0, 0, image = im_emotional, anchor = "nw" )
        root.update_idletasks()
        root.update()
        show_mask("emotional")
    else:
        if list_cues_str[i] == "neutral":
            im_neutral = ImageTk.PhotoImage(PIL.Image.open(random.choice(neutral)))
            my_canvas.create_image( 0, 0, image = im_neutral, anchor = "nw" )
            root.update_idletasks()
            root.update()
            show_mask("neutral")
    


time.sleep(0.004)  # here we simulate the sampling frequency of the Unicorn (one sample every 4 ms)
    

print(emotional_times)
print("Average time reaction for an emotional face is: ", average(emotional_times))

print(neutral_times)
print("Average time reaction for a neutral face is: ",average(neutral_times))