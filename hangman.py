# ------------------------------------------------------------------------ Importing packages ----------------------------------------------------------------------------
import tkinter as tk  
from tkinter import messagebox as mb
import tkinter.font as f
import random as r
import winsound
import shelve as sh

op = sh.open('Movies.bd')                                       # Movie list file
La = op['MOVIE-LIST']                                           # Pointer stroing movie list

AB = 0                                                          # Game play GUI
EndGame = False 

count = 0
attempts = 7
# ------------------------------------------------------------------------- Window alignment function --------------------------------------------------------------------

def alignment(root):
    
    # root.iconbitmap('Images/ic.ico')
    
    winWidth = root.winfo_reqwidth()
    winHeight = root.winfo_reqheight()

    posRight = int(root.winfo_screenwidth()/2 - winWidth)
    posLeft = int(root.winfo_screenheight()/2 - winHeight)

    root.geometry( "+{}+{}" .format(posRight, posLeft))     
    
# ------------------------------------------------------------------------ Loading of first window -------------------------------------------------------------------

def load():
    
    # ---------------------------------------------------------------- Buttons --------------------------------------------------------------------
    
    ButtonAdd = tk.Button(GUI, text = "Add Movie", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = add)
    ButtonAdd['font'] = f.Font(family = 'Helvetica' )
    ButtonAdd.place(x = 11, y = 100)
    ButtonAdd.config(width = 20, height = 2)                    # Add Movie Button
    
    ButtonGame = tk.Button(GUI, text = "Start Game", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : StartPlay(0))
    ButtonGame['font'] = f.Font(family = 'Helvetica' )
    ButtonGame.place(x = 210, y = 100)
    ButtonGame.config(width = 20, height = 2)                   # Start Game Button
    
    EndButton = tk.Button(GUI, text = "Quit", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = q)
    EndButton.place(x = 100, y = 200)
    EndButton['font'] = f.Font(family = 'Helvetica' )
    EndButton.config(width = 20, height = 2)                    # Quit Button
    
# ---------------------------------------------------------------------------- Add Movie Dialog Box ----------------------------------------------------------------------
      
def add():
    
    global GUI
    GUI.withdraw()

    GUI = tk.Tk()
    GUI.geometry("400x100")
    GUI.title("Movie Name")
    GUI.resizable(0, 0)
    alignment(GUI)
    
    L = tk.Label(GUI, text = "Add Movie Name : ")               
    L.place(x = 10, y = 30)                                     # Add Movie Label

    Name = tk.StringVar()                                       # Input

    entry1 = tk.Entry(GUI, textvariable = Name)                 
    entry1.place(x = 120, y = 30)                               # Entry Label

    # ------------------------------------------------ Confirm movie and empty entry label -------------------------------------------------------
    
    def delete():
        confirm(entry1.get())
        entry1.delete(0, len(str(entry1.get())))


    AdButton = tk.Button(GUI, text = "Confirm", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = delete)
    AdButton.place(x = 260, y = 30)                             # Add Movie Button      

    StartGame = tk.Button(GUI, text = "Start Game", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : StartPlay(0))
    StartGame.place(x = 320, y = 30)                            # Start Game Button

    GUI.mainloop()
        
# ------------------------------------------------------------------------ Adding Movie to List -------------------------------------------------------------------------

def confirm(a):
    
    global op
    
    flag = 0                                                     # Movie present in list flag
    n1 = str(a)                                                  # Entered movie by user
    n1 = n1.replace(" ", "--")
    
    # ------------------------------------------------ if movie present in list -----------------------------------------------------
    
    for i in La:
        if i.lower() == n1.lower():
            flag = 1
            break
    # ---------------------------------------------------------------------------------------------------------------- If not exists
    if flag == 0:
        La.append(n1)                                             # Temperory list (Stores all movies)
        
        # ---------------------------------- Add Movie permenantly -------------------------------------
        
        ans = mb.askquestion("Notification", "Do you want to add this movie permenantly to your list!?")
        if ans == 'yes':
            
            tempLa = [i for i in op['MOVIE-LIST']]                # Permanent list   
            tempLa.append(n1)
            op['MOVIE-LIST'] = tempLa
            del(tempLa)                                           # Empty permanent list
            
            op.close()
            op = sh.open('Movies.bd')   
        
        s = "Added successfully"
    
    # --------------------------------------------------------------------------------------------------------------------- If exists
    else:
        s = "Name already exists"
        
    mb.showinfo("Notification", s)   
   
# --------------------------------------------------------------------------- Quit function ------------------------------------------------------------------------------
     
def q():
    if(mb.askquestion("Notification", "Do you want to leave us soo soon!?") == "yes"):
        
        mb.showinfo("Quit", "Thank you! See you real soon!")
        quit()
    
# ------------------------------------------------------------------------------ Game Play -------------------------------------------------------------------------
  
def StartPlay(n):
    
    global AB
    global EndGame
    
    global count
    global attempts

    # ------------ Close Previous windows -----------
    if n == 0:
        GUI.withdraw()
    if n == 1:
        count = 0                                                       # Number of wrong attempts
        attempts = 7 
        AB.withdraw()
    
    AB = tk.Tk()
    AB.geometry("520x375")
    AB.title("Let's Start!🎉")
    AB.resizable(0, 0)
    alignment(AB)
    
    # ----------- Generating random number -----------
    a = 0
    x = 0
    while a == x:
        x = r.randint(0, (len(La)-1))
    
    st = La[x]                                                  # Movie name in the x position of the list                               
    Letters = ['a', 'e', 'i', 'o', 'u']
    entry = ""                                                  # The character entered by the user
    
    finalString = ""                                            # Variable storing the movie name in the format to be displayed
    
    # ----------- Formatting the movie name -----------
    for i in range(len(st)):
        
        if st[i].lower() in Letters:                            # If character encountered present in letters list
            finalString = finalString + str(st[i]) + " "
            
        elif st[i] == '-':                                      # If the character encountered is a space
            finalString = finalString + "    "
        
        else:                                                   # If the character encountered not present
            finalString = finalString + '_' + "  "
            
    finalString = "Guess the movie name : \n" + finalString     # Final formatted string to be displayed    
    
        
    Label_movie = tk.Label(AB) 
    Label_movie.place(x = 11, y = 10)
    Label_movie.config( text = finalString, width = 55, height = 5, bg = "black", fg = "white", bd = 5, font=("Helvetica", 12))
    Label_movie.pack(side = "top")                              # Display for the formatted movie name
    
    Options = tk. StringVar()                                   # Entry of the character by the user
    
    Label_input = tk.Label(AB, text = "Enter the letter : ")
    Label_input.place(x = 140, y = 120)
    Label_input.config(font=("Helvetica", 12))                  # 'Enter the letter' display
    
    Entry_option = tk.Entry(AB, textvariable = Options)
    Entry_option.place(x = 260, y = 123)
    Entry_option.config(width = 5)                              # Entry of the character by the user
    
    text = "Hello! Okay then let's start!"
    text1 = "more chances!"
    
    Label_result = tk.Label(AB)
    Label_result.place(x = 100, y = 150)
    Label_result.config(height = 2, width = 30, bd = 10)         # Display if the answer is correct or not
    
    canvas_image = tk.Label(AB, width = 1, height = 1, bd = 10)   
    canvas_image.place(x = 170, y = 192)                         # Display of the 'number of attempts'
    
    canvas_attempts = tk.Label(AB, width = 12, height = 2)
    canvas_attempts.place(x = 203, y = 202)
    canvas_attempts.config(text = text1, font=("Helvetica", 12)) # Display of attempts left
    
    Game_over = tk.Label(AB)
    Game_over.place(x = 107, y = 250)                            # Display 'game over'
    
    New_movie_bt = tk.Button(AB, text = "Try new Movie", activebackground = "grey", activeforeground = "black", bg = "black", fg = "white", command = lambda : StartPlay(1))
    New_movie_bt.place(x = 15, y = 300)
    New_movie_bt['font'] = f.Font(family = 'Helvetica' )
    New_movie_bt.config(width = 22, height = 2)                  # New Movie Button
    
    quit_bt = tk.Button(AB, text = "End Game", activebackground = "grey", activeforeground = "black", bg = "black", fg = "white", command = q)
    quit_bt.place(x = 255, y = 300)
    quit_bt['font'] = f.Font(family = 'Helvetica' )
    quit_bt.config(width = 22, height = 2)                        # Quit Button
    
    # ---------------- Change of text in both Number of attempts and if the input is correct or not ----------------
    Label_result.config(text = text, font=("Helvetica", 12))
    canvas_image.config(text = attempts, font=("Helvetica", 25))   

    # ------------------------------------------------------- Check of the input character --------------------------------------------------------------------
    
    def check():
        
        global count 
        global attempts
        global EndGame
        
        f = False
        
        entry = str(Entry_option.get())                           # Input character

        # ------------ Check if the only character entered is an alphabet or not ------------
        if not entry.isalpha():                                   # If the entered character is not an alphabet
            
            mb.showerror("Error", "Not a valid character")
            Entry_option.delete(0, len(entry))
            
        elif len(entry) > 1:                                      # If 2 or more characters are entered by the user
            
            mb.showerror("Error", "Too many arguments")
            Entry_option.delete(0, len(entry))
        
        else:                                                     # if the character entered as no exceptional errors    
            
            finalString = ""
            Entry_option.delete(0, len(entry))               
            
        # ------------------------------------------------------------------------------------------- If the input character is present in the movie name 
        if entry.lower() in st.lower():
            
            if not entry.lower() in Letters:                  # The letter entered is not present is in letters list
                Letters.append(entry.lower())
                text = "Hurray!! Try picking another letter."
                winsound.Beep(10000, 250)
                
            else:
                text = "Letter already attempted!."            # The letter entered is present is in letters list
                
                for i in range(2):
                    winsound.Beep(5000, 250)   
        
        # ------------------------------------------------------------------------------------------- If the input character is not present in the movie name 
        else:
            if not entry.lower() in Letters:                  # The letter entered is not present is in letters list
                Letters.append(entry.lower())
                text = "Oops! No match, guess another letter."
                count = count + 1
                
                for i in range(3):
                    winsound.Beep(1000, 500)
                    
            else:                                              # The letter entered is present is in letters list
                text = "Letter already attempted!."            
                
                for i in range(2):
                    winsound.Beep(5000, 250)   
            
        # ------------ Editing movie name after user entry ------------                              
        for i in range (len(st)):
            
            if st[i].lower() in Letters:                        # if the character is present in Letters list
                finalString = finalString + str(st[i]) + " "
                
            elif st[i] == '-':                                  # if the character is a word divider
                finalString = finalString + "    "
    
            else:                                               # if the character is not yet revealed
                finalString = finalString + '_' + "  "
                
        # ------------------------ Scan movie name ------------------------
        for i in range(len(finalString)):
            if finalString[i] == '_':
                f = True
                break
        
        if f == True:                                           # Yet the movie name should be completed
            finalString = "Guess the movie name : \n" + finalString 
        
        else:                                                   # The movie name is completed
            finalString = "Yayy!! Done"
        
        
        res = attempts - count                                  # Remaining attempts left
        
        # ------------------------------------------------------------------------------------------- Attempted even after the game is over
        if res < 0:                                            
            if EndGame == True:
                mb.showerror("Error", "Chances over! Try a new game.")
        
        # -------------------------------------------------------------------------------------------  if the game over 
        elif res == 0:                                            
            t1 = "Game over! Try again. "
            text = "Sorry! No match"
            EndGame = True
            Label_result.config(text = text)
            canvas_image.config(text = res, font=("Helvetica", 25)) 
            Game_over.config(text = t1, font=("Helvetica", 20))
        
        # ------------------------------------------------------------------------------------------- Still attempts are left                         
        else:                                                   
            Label_result.config(text = text)
            Label_movie.config(text =  finalString)
            canvas_image.config(text = res, font=("Helvetica", 25))                       

    sButton = tk.Button(AB, text = "Check!", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = check)
    sButton.place(x = 310, y = 120)                                  # Check button for user input
    
    a = x                                                            # previous movie name index
    
# ------------------------------------------------------------------------ The entry window design -------------------------------------------------------------------

GUI = tk.Tk()
GUI.geometry("450x275")
GUI.resizable(0, 0)
GUI.title("Play Hangman")
alignment(GUI)

ButtonPlay = tk.Button(GUI, text = "Yayy! Hangman", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = load)
ButtonPlay['font'] = f.Font(family = 'Helvetica' )
ButtonPlay.place(x = 11, y = 10)
ButtonPlay.config(width = 38, height = 3)                             # Play button

GUI.mainloop()

