import tkinter as tk
from tkinter import messagebox as mb
import tkinter.font as f
import random as r


La = ['Rab-Ne-Banadhi-Jodi', 'Gaja', 'Mr-and-Mrs-Ramachari', 'Fida', 'Love-Mocktail']

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
    entry = ""
    
    finalString = ""
    for i in range(len(st)):
        
        if (st[i].lower() == 'a' or st[i].lower() == 'e' or st[i].lower() == 'i' or st[i].lower() == 'o' or st[i].lower() == 'u' or st[i].lower() == '-'):
            finalString = finalString + str(st[i]) + " "
        
        else:
            finalString = finalString + '_' + "  "
            
    finalString = "Guess the movie name : " + finalString         
        
    Label_movie = tk.Label(AB) 
    Label_movie.place(x = 5, y = 10)
    Label_movie.config( text = finalString, width = 61, height = 6, bg = "black", fg = "white", bd = 5, font=("Helvetica", 11))
    Label_movie.pack(side = "top") 
    
    Options = tk. StringVar()
    
    Label_input = tk.Label(AB, text = "Enter the letter : ")
    Label_input.place(x = 10, y = 120)
    Label_input.config(font=("Helvetica", 12))
    
    Entry_option = tk.Entry(AB, textvariable = Options)
    Entry_option.place(x = 127, y = 123)
    Entry_option.config(width = 5)
    
    def check():
        entry = str(Entry_option.get())
    
        if not entry.isalpha():
            mb.showerror("Error", "Not a valid character")
        
        else:
            
            Label_result = tk.Label(AB)
            Label_result.place(x = 120, y = 175)
            Label_result.config(height = 3, width = 30, bg = "white")
            # Label_result.pack()
            
            Label_image = tk.Label(AB)
            Label_image.place(x = 155, y = 245)
            Label_image.config(height = 10, width = 20, bg = "black")
            # Label_image.pack()

    sButton = tk.Button(AB, text = "Check!", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = check)
    sButton.place(x = 170, y = 120)
       
    
    
GUI = tk.Tk()
GUI.geometry("450x350")
GUI.resizable(0, 0)
GUI.title("Play Hangman")

ButtonPlay = tk.Button(GUI, text = "Yayy! Hangman", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = load)
ButtonPlay['font'] = f.Font(family = 'Helvetica' )
ButtonPlay.place(x = 11, y = 10)
ButtonPlay.config(width = 38, height = 3)




GUI.mainloop()