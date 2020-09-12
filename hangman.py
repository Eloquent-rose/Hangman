import tkinter as tk
from tkinter import *  
from tkinter import messagebox as mb
import tkinter.font as f
import random as r
from PIL import ImageTk, Image
import winsound

La = ['Rab-Ne-Banadhi-Jodi', 'Gaja', 'Mr-and-Mrs-Ramachari', 'Fida', 'Love-Mocktail']
count = 0
attempts = 9

def load():
    
    ButtonAdd = tk.Button(GUI, text = "Add Movie", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = add)
    ButtonAdd['font'] = f.Font(family = 'Helvetica' )
    ButtonAdd.place(x = 11, y = 100)
    ButtonAdd.config(width = 20, height = 2)
    
    ButtonGame = tk.Button(GUI, text = "Start Game", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = StartPlay)
    ButtonGame['font'] = f.Font(family = 'Helvetica' )
    ButtonGame.place(x = 210, y = 100)
    ButtonGame.config(width = 20, height = 2)
    
    EndButton = tk.Button(GUI, text = "Quit", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = q)
    EndButton.place(x = 100, y = 200)
    EndButton['font'] = f.Font(family = 'Helvetica' )
    EndButton.config(width = 20, height = 2)
    
        
def add(n = 0):
    
    if n == 0:
               
        GUI.withdraw()
        
        Add = tk.Tk()
        Add.geometry("400x100")
        Add.title("Movie Name")
        Add.resizable(0, 0)
        
        L = tk.Label(Add, text = "Add Movie Name : ")
        L.place(x = 10, y = 30)
        
        Name = tk.StringVar()
        
        entry1 = tk.Entry(Add, textvariable = Name)
        entry1.place(x = 120, y = 30)
            
        
        def close():
            Add.withdraw()
            StartPlay()
            
        def delete():
            confirm(entry1.get())
            entry1.delete(0, len(str(entry1.get())))
            
        
        AdButton = tk.Button(Add, text = "Confirm", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = delete)
        AdButton.place(x = 260, y = 30)           
                 
        StartGame = tk.Button(Add, text = "Start Game", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = close)
        StartGame.place(x = 320, y = 30)
        
        Add.mainloop()
        

        
        
def confirm(a):
    
    flag = 0
    n1 = str(a)
    n1 = n1.replace(" ", "-")
    
    for i in La:
        if i.lower() == n1.lower():
            flag = 1
            break
        
    if flag == 0:
        La.append(n1)
        s = "Added successfully"
        mb.showinfo("Hello", s)
        
    else:
        s = "Name already exists"
        mb.showerror("Error", s)   
       
def q():
    mb.showinfo("Quit", "Thank you! See you real soon!")
    quit()
    
    
def StartPlay():
    
    GUI.withdraw()
    
    AB = tk.Tk()
    AB.geometry("450x450")
    AB.title("Let's Start!🎉")
    
    x = r.randint(0, (len(La)-1))
    st = La[x]
    Letters = ['a', 'e', 'i', 'o', 'u', '-']
    entry = ""
    
    finalString = ""
    for i in range(len(st)):
        
        if st[i].lower() in Letters:
            finalString = finalString + str(st[i]) + " "
        
        else:
            finalString = finalString + '_' + "  "
            
    finalString = "Guess the movie name : " + finalString         
        
    Label_movie = tk.Label(AB) 
    Label_movie.place(x = 11, y = 10)
    Label_movie.config( text = finalString, width = 50, height = 5, bg = "black", fg = "white", bd = 5, font=("Helvetica", 11))
    Label_movie.pack(side = "top") 
    
    Options = tk. StringVar()
    
    Label_input = tk.Label(AB, text = "Enter the letter : ")
    Label_input.place(x = 100, y = 120)
    Label_input.config(font=("Helvetica", 12))
    
    Entry_option = tk.Entry(AB, textvariable = Options)
    Entry_option.place(x = 220, y = 123)
    Entry_option.config(width = 5)
    
    text = "Hello! Okay then let's start!"
    text1 = "more chances!"
    
    Label_result = tk.Label(AB)
    Label_result.place(x = 70, y = 175)
    Label_result.config(height = 2, width = 30, bg = "white", bd = 10)
    
    canvas_image = Label(AB, width = 3, height = 1, bg = "white", bd = 10)   
    canvas_image.place(x = 90, y = 250)
    
    canvas_attempts = Label(AB, width = 18, height = 2, bg = "white")
    canvas_attempts.place(x = 180, y = 260)
    canvas_attempts.config(text = text1, font=("Helvetica", 12))
    
    res = str(attempts - count)
    Label_result.config(text = text, font=("Helvetica", 12))
    canvas_image.config(text = res, font=("Helvetica", 25))   

0
    def check():
        
        global count 
        global attempts
        
        entry = str(Entry_option.get())
    
        if not entry.isalpha():
            
            mb.showerror("Error", "Not a valid character")
            Entry_option.delete(0, len(entry))
            
        elif len(entry) > 1:
            
            mb.showerror("Error", "Too many arguments")
            Entry_option.delete(0, len(entry))
        
        else:
            
            finalString = ""
            Entry_option.delete(0, len(entry))
            
            if entry.lower() in st.lower():
                if not entry.lower() in Letters:
                    Letters.append(entry.lower())
                    text = "Hurray!! Try picking another letter."
                    winsound.Beep(10000, 1000) 
                else:
                    text = "Letter already attempted!."
                    winsound.Beep(5000, 1000)
                    
            else:
                text = "Oops! No match, guess another letter."
                count = count + 1
                winsound.Beep(1000, 100) 
                
            print(Letters)
            
            for i in range (len(st)):
                
                if st[i].lower() in Letters:
                    finalString = finalString + str(st[i]) + " "
        
                else:
                    finalString = finalString + '_' + "  "
            
            finalString = "Guess the movie name : " + finalString 
            
            res = str(attempts - count)
            Label_result.config(text = text)
            Label_movie.config(text =  finalString)
            canvas_image.config(text = res, font=("Helvetica", 25)) 
            
            if res == 0:
                text = "Game over!"
                Label_result.config(text = text)
                     

    sButton = tk.Button(AB, text = "Check!", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = check)
    sButton.place(x = 270, y = 120)   
    
    
GUI = tk.Tk()
GUI.geometry("450x350")
GUI.resizable(0, 0)
GUI.title("Play Hangman")

ButtonPlay = tk.Button(GUI, text = "Yayy! Hangman", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = load)
ButtonPlay['font'] = f.Font(family = 'Helvetica' )
ButtonPlay.place(x = 11, y = 10)
ButtonPlay.config(width = 38, height = 3)

GUI.mainloop()