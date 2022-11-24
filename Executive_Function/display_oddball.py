from tkinter import *
from PIL import ImageTk, Image
import time
import random




N_CUES = 50
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






#----------------------------------- image related stuff -----------------------------------

root = Tk()

    # make sure to use png here

im_blank = ImageTk.PhotoImage( Image.open( "/home/andrei/Desktop/BCI_stuff/PIPELINE_space_invaders/photos_calibration/blank_screen_1080x1920.png" ) )
im_blue = ImageTk.PhotoImage( Image.open("/home/andrei/Desktop/BCI_stuff/PIPELINE_space_invaders/photos_calibration/blue_circle_big.png" ) )
im_green = ImageTk.PhotoImage( Image.open( "/home/andrei/Desktop/BCI_stuff/PIPELINE_space_invaders/photos_calibration/green_circle_big.png" ) )

label_blank = Label( image = im_blank )
label_blue = Label( image = im_blue )
label_green = Label( image = im_green )



my_canvas = Canvas( root, width = 1920, height = 1080 )        # change this based on display resolution
my_canvas.pack(fill = "both", expand = True)


#------------------------------------------------------------------------------------------------







#---------------------------make a list with the sample indexes at which to display stuff-----------

indexes_cue = []  #first 1000, then + 1125 # 1000, 1000 + 125 + 1000, 1000 + 125 + 1000 + 
indexes_blank = [] #first 0, then + 1125 # 0, 0 + 1000 + 125, 0 + 1000 + 125...

for i in range(N_CUES):
    
    indexes_cue.append( i * (BLANK_DUR_ms + CUE_DUR_ms) + BLANK_DUR_ms )
    indexes_blank.append( i * (BLANK_DUR_ms + CUE_DUR_ms) )

indexes_blank.append( N_CUES * (BLANK_DUR_ms + CUE_DUR_ms) + CUE_DUR_ms )        # because we want to end with a blank screen for 4 seconds

#----------------------------------------------------------


i_sample = 0
i_cue = 0

while True: 


    if i_sample in indexes_blank:

        my_canvas.create_image( 0, 0, image = im_blank, anchor = "nw" )
        root.update_idletasks()
        root.update() # every second call, a nasty window appears, even if I just run this one


    elif i_sample in indexes_cue:

        if list_cues_str[i_cue] == "go":

            my_canvas.create_image( 0, 0, image = im_blue, anchor = "nw" )
            root.update_idletasks()
            root.update()

        if list_cues_str[i_cue] == "no-go":

            my_canvas.create_image( 0, 0, image = im_green, anchor = "nw" )
            root.update_idletasks()
            root.update()



        i_cue += 1
        

    if i_sample == N_CUES * (BLANK_DUR_ms + CUE_DUR_ms) + BLANK_DUR_ms:

        break


    i_sample += 1


    time.sleep(0.004)  # here we simulate the sampling frequency of the Unicorn (one sample every 4 ms)







# while True:       # this stuff works   # dummy example


#     if i_sample == 0:

#         my_canvas.create_image( 0, 0, image = im_blank, anchor = "nw" )
#         root.update_idletasks()
#         root.update() # every second call, a nasty window appears, even if I just run this one


#     elif i_sample == 999:

#         my_canvas.create_image( 0, 0, image = im_green, anchor = "nw" )
#         root.update_idletasks()
#         root.update() # every second call, a nasty window appears, even if I just run this one


#     if i_sample == 1250:
#         break

#     i_sample += 1

#     time.sleep(0.004)  # here we simulate the sampling frequency of the Unicorn (one sample every 4 ms)