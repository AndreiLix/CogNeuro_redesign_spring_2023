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




emotional = ['M10-Disgust-Apex.jpg',
 'F02-Pride-Apex.jpg',
 'F07-Disgust-Apex.jpg',
 'F04-Surprise-Apex.jpg',
 'F06-Fear-Apex.jpg',
 'F03-Embarrass-Apex.jpg',
 'M09-Joy-Apex.jpg',
 'M02-Surprise-Apex.jpg',
 'M12-Sad-Apex.jpg',
 'F09-Sad-Apex.jpg',
 'F08-Embarrass-Apex.jpg',
 'M01-Pride-Apex.jpg',
 'M06-Pride-Apex.jpg',
 'F01-Joy-Apex.jpg',
 'F05-Joy-Apex.jpg',
 'M07-Anger-Apex.jpg',
 'F10-Fear-Apex.jpg',
 'M04-Contempt-Apex.jpg'] # the images directories should be adjusted according to who's running the script

neutral = ['M12-Neutral.jpg',
 'M04-Neutral.jpg',
 'F03-Neutral.jpg',
 'M02-Neutral.jpg',
 'F09-Neutral.jpg',
 'F10-Neutral.jpg',
 'M10-Neutral.jpg',
 'F04-Neutral.jpg',
 'M06-Neutral.jpg',
 'F02-Neutral.jpg',
 'F07-Neutral.jpg',
 'M01-Neutral.jpg',
 'M09-Neutral.jpg',
 'F05-Neutral.jpg',
 'F06-Neutral.jpg',
 'F01-Neutral.jpg',
 'F08-Neutral.jpg',
 'M07-Neutral.jpg']

mask = "mask.png"

emotional_times_fifty = []
neutral_times_fifty = []

emotional_times_twohun = []
neutral_times_twohun = []

random_length = []

for i in range(18):
    random_length.append(0.05)
for i in range(18):
    random_length.append(0.2)

random.shuffle(random_length)
# ------------------------------------ makng a list of random cues (36 in total: 32 emotional, 4 neutral, 18 masks) -----------------------------

# put cues in a randomized order

list_cues_str = []
 
for i in range(18):                 

    list_cues_str.append("emotional")
    
for i in range(18):                 

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
        my_canvas.create_image( 1920/2, 1080/2, image = im_mask, anchor = CENTER  )
        time_sleep = random.choice(random_length)
        time.sleep(time_sleep)
        root.update_idletasks()
        root.update()
        i = datetime.datetime.now()
        if time_sleep == 0.05:
            if stimuli == "emotional" : # if key 'e' is pressed 
                keyboard.wait("e")
                q = datetime.datetime.now()
                time_t = (i-q).microseconds
                emotional_times_fifty.append(time_t)
                break
            elif stimuli == "neutral":
                keyboard.wait("n")
                q = datetime.datetime.now()
                time_t = (i-q).microseconds
                neutral_times_fifty.append(time_t)
                break
        else:
            if stimuli == "emotional" : # if key 'e' is pressed 
                keyboard.wait("e")
                q = datetime.datetime.now()
                time_t = (i-q).microseconds
                emotional_times_twohun.append(time_t)
                break
            elif stimuli == "neutral":
                keyboard.wait("n")
                q = datetime.datetime.now()
                time_t = (i-q).microseconds
                neutral_times_twohun.append(time_t)
                break
            
            

def countdown(count):
    # change text in label        
    label['text'] = count
    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)
    else:
        label.destroy()
        for i in range(len(list_cues_str)): 
            if list_cues_str[i] == "emotional":
                im_emotional = ImageTk.PhotoImage(PIL.Image.open(random.choice(emotional)))
                my_canvas.create_image( 1920/2, 1080/2, image = im_emotional, anchor = CENTER )
                root.update_idletasks()
                root.update()
                show_mask("emotional")
            else:
                if list_cues_str[i] == "neutral":
                    im_neutral = ImageTk.PhotoImage(PIL.Image.open(random.choice(neutral)) )
                    my_canvas.create_image(1920/2, 1080/2, image = im_neutral, anchor = CENTER )
                    root.update_idletasks()
                    root.update()
                    show_mask("neutral")
    

        time.sleep(0.004)  # here we simulate the sampling frequency of the Unicorn (one sample every 4 ms)

        #print(emotional_times)
        print("Average time reaction for an emotional face with 50 ms exposure is: ", average(emotional_times_fifty))

        #print(neutral_times)
        print("Average time reaction for a neutral face with 50 ms exposure is: ",average(neutral_times_fifty))
        
        #print(emotional_times)
        print("Average time reaction for an emotional face with 200 ms exposure is: ", average(emotional_times_twohun))

        #print(neutral_times)
        print("Average time reaction for a neutral face with 200 ms exposure is: ",average(neutral_times_twohun))



label = Label(root, font = ("Arial", 50))
label.place(relx=0.5, rely=0.5, anchor = CENTER)

# call countdown first time    
countdown(5)
# root.after(0, countdown, 5)

root.mainloop()