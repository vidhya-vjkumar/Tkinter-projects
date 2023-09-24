from tkinter import *
import tkinter as ttk
import random
from PIL import Image, ImageTk

choices=['Guru joe images\Ah, the age old.png','Guru joe images\\as i see it.png','Guru joe images\eenie.png','Guru joe images\shhhh.png','Guru joe images\\touch the ball.png','Guru joe images\Better not tell you now.png','Guru joe images\Egads No.png','Guru joe images\yes,no,maybe,so.png','Guru joe images\yes.png','Guru joe images\cannot predict now.png']

def answer():
    if entry.get()!="":
        choice=random.choice(choices)
        img=ImageTk.PhotoImage((Image.open(choice).resize((700,500))))
        joe.config(image=img)
        joe.image=img
    else:
        choice=random.choice(choices)
        img=ImageTk.PhotoImage((Image.open("Guru joe images\guru joe.png").resize((700,500))))
        joe.config(image=img)
        joe.image=img
    entry.delete(0, "end")
    

def on_entry_click(event):
    if entry.get() == placeholder:
        entry.delete(0, "end")  # Clear the default placeholder text
        entry.config(fg="white")  # Change the text color to black

def on_focusout(event):
    if entry.get()=="":
        entry.insert(0, placeholder)  # Put back the placeholder text
        entry.config(fg="gray")  # Change the text color to gray


root=Tk()
root.geometry("1000x700")
root.title("Ask Guru Joe")
root.maxsize(1000,700)
root.minsize(1000,700)
root.configure(bg="#C4A484")
root.wm_iconbitmap("Guru joe images\crystal ball.ico")

frm=Frame(root,bg="#C4A484")

img=ImageTk.PhotoImage((Image.open("Guru joe images\guru joe.png").resize((700,500))))
joe=ttk.Label(frm,image=img,justify="center",width=700,height=500)
joe.pack(padx=10,pady=10)

question=StringVar()
entry_frame = ttk.Frame(frm, bg="#7F00FF", bd=1, relief="sunken", borderwidth=2, highlightthickness=0)
entry = ttk.Entry(entry_frame, textvariable=question, bd=0, relief="flat",fg="gray",font="Lucida 16",background="#00072D", width=200,insertbackground="white")
entry.pack(fill="both", expand=True,padx=10,pady=10)

placeholder = "Ask a yes or no question"
entry.insert(0, placeholder)  # Set the initial text to the placeholder
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_focusout)  # When clicked, clear the placeholder
entry.pack(padx=10, pady=10, fill="both", expand=True)
entry_frame.pack(padx=10,pady=10)

ask=ttk.Button(frm,text="Ask",font="Jokerman 24",command=answer,bg="#7F00FF",foreground="yellow")
ask.pack(padx=10,pady=10)

frm.pack()
root.mainloop()