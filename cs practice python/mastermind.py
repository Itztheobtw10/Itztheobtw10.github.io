from tkinter import * 
import pygame
import random 

root = Tk()

#Logic 
colours = ['Blue', 'Red', 'Green', 'Orange', 'Purple', 'Yellow']


def check_guess(): 
   
   return()

def change_difficulty():
    while True:
        difficulty = input("Please Select A difficulty: Easy or Hard: ").capitalize().strip()

        if difficulty == "Hard":
            code = [random.choice(colours) for i in range(6)]
            print(code)
            break
        elif difficulty == "Easy":
            code = [random.choice(colours) for i in range(4)]
            print(code)
            break
        else:
            print('Invalid Input. Please select either Easy or Hard')
        return()

def ent_name():
    name = entry.get()
    return()
# end of logic 

dif_btn = Button(root,text="Easy", font=('Arial', 14), command=change_difficulty,relief='raised')

# creating the window and its properties 
root.geometry("500x500")
root.title("Theo's Amazing Mastermind Game")

label = Label(root,
                 text="Welcome to Theo's Mastermind Game", 
                 font=('Arial', 30, 'bold'),
                 fg='black',
                 bg='#2e4053',
                 relief='raised',
                 bd = 10,
                 padx=20,
                 pady=20)

label.pack(padx=20, pady=10)
root.config(background="#2e4053")

entry = Entry()
entry.pack()
# intitilising pygame
pygame.mixer.init()

#creating the play function which takes the pygame function mixer.load and .play 
# to access the audio file and play 
def play():
    pygame.mixer.music.load("/Users/itztheobtw/Desktop/mastermind_audio.mp3")
    pygame.mixer.music.play(loops=100)

 # creating the stop function which stops the sound when pressed.
def stop():
    pygame.mixer.music.stop()
    
# creating a button for the fx and setting position in window 
my_btn = Button(root,text="FX", font=('Arial', 14), command=play,relief='raised')
my_btn.place(x=1400,y=30)

# creating a button to stop fx and settting postion 
stop_btn = Button(root,text="NO FX", font=('Arial', 14), command=stop, relief='raised')
stop_btn.place(x=1380,y=60)
root.mainloop()
