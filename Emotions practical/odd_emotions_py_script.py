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
import csv

# Create the CSV file

row = ["Stimulus type", 'Reaction time']
# open the file in the write mode
with open('csv_file', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)
    # write a row to the csv file
    writer.writerow(row)



emotional_fifty = ['M10-Disgust-Apex.jpg',
 'F02-Pride-Apex.jpg',
 'F04-Surprise-Apex.jpg',
 'F06-Fear-Apex.jpg',
 'F03-Embarrass-Apex.jpg',
 'M09-Joy-Apex.jpg',
 'M12-Sad-Apex.jpg',
 'M01-Pride-Apex.jpg',
 'M07-Anger-Apex.jpg']

neutral_fifty = ['M12-Neutral.jpg',
 'F03-Neutral.jpg',
 'M10-Neutral.jpg',
 'F04-Neutral.jpg',
 'F02-Neutral.jpg',
 'M01-Neutral.jpg',
 'M09-Neutral.jpg',
 'F06-Neutral.jpg',
 'M07-Neutral.jpg']


emotional_twohun = ['M10-Disgust-Apex.jpg',
 'F02-Pride-Apex.jpg',
 'F04-Surprise-Apex.jpg',
 'F06-Fear-Apex.jpg',
 'F03-Embarrass-Apex.jpg',
 'M09-Joy-Apex.jpg',
 'M12-Sad-Apex.jpg',
 'M01-Pride-Apex.jpg',
 'M07-Anger-Apex.jpg']

neutral_twohun = ['M12-Neutral.jpg',
 'F03-Neutral.jpg',
 'M10-Neutral.jpg',
 'F04-Neutral.jpg',
 'F02-Neutral.jpg',
 'M01-Neutral.jpg',
 'M09-Neutral.jpg',
 'F06-Neutral.jpg',
 'M07-Neutral.jpg']

mask = "mask.png"

emotional_times_fifty = []
neutral_times_fifty = []

emotional_times_twohun = []
neutral_times_twohun = []



check_repetition = ["start"]

# makng a list of random cues (36 in total: 9 emotional 50ms, 9 neutral 50ms, 9 emotional 200ms, neutral 200ms, 
#1 mask between each)

# Put cues in a randomized order

list_cues_str = []
 
for i in range(9):                 

    list_cues_str.append("emotional_50")
    
for i in range(9):                 

    list_cues_str.append("neutral_50")
    
for i in range(9):                 

    list_cues_str.append("emotional_200")
    
for i in range(9):                 

    list_cues_str.append("neutral_200")
      

random.shuffle( list_cues_str )

#---------------------------------------------------------------------------------------

def average(lst):
    return (sum(lst) / len(lst))


#----------------------------------- image related stuff -----------------------------------

root = Tk()

root.geometry("1000x1000")
my_canvas = Canvas( root, width = 1000, height = 1000 )
my_canvas.pack(fill = "both", expand = True)

#------------------time related stuff----------------------------------------

date_format_str = '%Y-%m-%d %H:%M:%S.%f'

#----------------------------------------------------------


def show_mask(stimuli, time_sleep, i):
    while True:
        im_mask = ImageTk.PhotoImage(PIL.Image.open(mask))
        my_canvas.create_image( 500, 300, image = im_mask, anchor = CENTER  )
        time.sleep(time_sleep)
        root.update_idletasks()
        root.update()
        if time_sleep == 0.05:
            if stimuli == "emotional" : 
                keyboard.wait("e")
                q = datetime.datetime.now()
                start = datetime.datetime.strptime(str(i), date_format_str)
                end = datetime.datetime.strptime(str(q), date_format_str)
                diff = end - start
                # Get the interval in milliseconds
                diff_in_milli_secs = diff.total_seconds() * 1000
                emotional_times_fifty.append(diff_in_milli_secs)
                row = ["Emotional 50 ms", diff_in_milli_secs]
                with open('csv_file', 'a') as f:
                    # create the csv writer
                    writer = csv.writer(f)
                    # write the row to the csv file
                    writer.writerow(row)
                break
            elif stimuli == "neutral":
                keyboard.wait("n")
                q = datetime.datetime.now()
                start = datetime.datetime.strptime(str(i), date_format_str)
                end = datetime.datetime.strptime(str(q), date_format_str)
                diff = end - start
                # Get the interval in milliseconds
                diff_in_milli_secs = diff.total_seconds() * 1000
                neutral_times_fifty.append(diff_in_milli_secs)
                row = ["Neutral 50 ms", diff_in_milli_secs]
                with open('csv_file', 'a') as f:
                    # create the csv writer
                    writer = csv.writer(f)
                    # write the row to the csv file
                    writer.writerow(row)
                break
        else:
            if stimuli == "emotional" : 
                keyboard.wait("e")
                q = datetime.datetime.now()
                start = datetime.datetime.strptime(str(i), date_format_str)
                end = datetime.datetime.strptime(str(q), date_format_str)
                diff = end - start
                # Get the interval in milliseconds
                diff_in_milli_secs = diff.total_seconds() * 1000
                emotional_times_twohun.append(diff_in_milli_secs)
                row = ["Emotional 200 ms", diff_in_milli_secs]
                with open('csv_file', 'a') as f:
                    # create the csv writer
                    writer = csv.writer(f)
                    # write the row to the csv file
                    writer.writerow(row)
                break
            elif stimuli == "neutral":
                keyboard.wait("n")
                q = datetime.datetime.now()
                start = datetime.datetime.strptime(str(i), date_format_str)
                end = datetime.datetime.strptime(str(q), date_format_str)
                diff = end - start
                # Get the interval in milliseconds
                diff_in_milli_secs = diff.total_seconds() * 1000
                neutral_times_twohun.append(diff_in_milli_secs)
                row = ["Neutral 200 ms", diff_in_milli_secs]
                with open('csv_file', 'a') as f:
                    # create the csv writer
                    writer = csv.writer(f)
                    # write the row to the csv file
                    writer.writerow(row)
                break
            
            

def countdown(count):
    # change text in label        
    label['text'] = count
    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)
    else:
        label.destroy()
        for i in range(36): # 36 stimuli 
            if list_cues_str[i] == "emotional_50":
                while True:
                    image_emo_50 = random.choice(emotional_fifty)
                    if image_emo_50 in check_repetition[-1]:
                        image_emo_50 = random.choice(emotional_fifty)
                    else:
                        check_repetition.append(image_emo_50)
                        break    
                emotional_fifty.remove(image_emo_50)
                im_emotional = ImageTk.PhotoImage(PIL.Image.open(image_emo_50))
                my_canvas.create_image( 500, 300, image = im_emotional, anchor = CENTER )
                i = datetime.datetime.now()
                root.update_idletasks()
                root.update()
                show_mask("emotional", 0.05, i)
            elif list_cues_str[i] == "neutral_50":
                while True:
                    image_neu_50 = random.choice(neutral_fifty)
                    if image_neu_50 in check_repetition[-1]:
                        image_neu_50 = random.choice(neutral_fifty)
                    else:
                        check_repetition.append(image_neu_50)
                        break 
                neutral_fifty.remove(image_neu_50)
                im_neutral = ImageTk.PhotoImage(PIL.Image.open(image_neu_50))
                my_canvas.create_image(500, 300, image = im_neutral, anchor = CENTER )
                i = datetime.datetime.now()
                root.update_idletasks()
                root.update()
                show_mask("neutral", 0.05, i)
            elif list_cues_str[i] == "emotional_200":
                while True:
                    image_emo_200 = random.choice(emotional_twohun)
                    if image_emo_200 in check_repetition[-1]:
                        image_emo_200 = random.choice(emotional_twohun)
                    else:
                        check_repetition.append(image_emo_200)
                        break
                emotional_twohun.remove(image_emo_200)
                im_neutral = ImageTk.PhotoImage(PIL.Image.open(image_emo_200))
                my_canvas.create_image(500, 300, image = im_neutral, anchor = CENTER )
                i = datetime.datetime.now()
                root.update_idletasks()
                root.update()
                show_mask("emotional", 0.2, i)
            else:
                if list_cues_str[i] == "neutral_200":
                    while True:
                        image_neu_200 = random.choice(neutral_twohun)
                        if image_neu_200 in check_repetition[-1]:
                            image_neu_200 = random.choice(neutral_twohun)
                        else:
                            check_repetition.append(image_neu_200)
                            break
                    neutral_twohun.remove(image_neu_200)
                    im_neutral = ImageTk.PhotoImage(PIL.Image.open(image_neu_200) )
                    my_canvas.create_image(500, 300, image = im_neutral, anchor = CENTER )
                    i = datetime.datetime.now()
                    root.update_idletasks()
                    root.update()
                    show_mask("neutral", 0.2, i)

        print("End of experiment, you may close this terminal window.")
        time.sleep(0.004) 

        #print(emotional_times_50)
        print("Average time reaction for an emotional face with 50 ms exposure is (in ms): ", average(emotional_times_fifty))

        #print(neutral_times_50)
        print("Average time reaction for a neutral face with 50 ms exposure is (in ms): ",average(neutral_times_fifty))
        
        #print(emotional_times_200)
        print("Average time reaction for an emotional face with 200 ms exposure is (in ms): ", average(emotional_times_twohun))

        #print(neutral_times_200)
        print("Average time reaction for a neutral face with 200 ms exposure is (in ms): ",average(neutral_times_twohun))



label = Label(root, font = ("Arial", 50))
label.place(relx=0.5, rely=0.5, anchor = CENTER)

# call countdown first time    
countdown(5)

root.mainloop()