from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tmsg
import random

#Questions and answers
questions=[
    {   "question":"Which pub in London conceals the entrance to Diagon Alley?",
        "options":["The Three Broomsticks","The Hog's Head","The Leaky Cauldron","The Magical Menagerie"],
        "answer":"The Leaky Cauldron"
    },
    {
        "question":"Who is the Slytherin ghost?",
        "options":["Bloody Baron","Fat Friar","Nearly Headless Nick","Grey Lady"],
        "answer":"Bloody Baron"
    }, 
    {
        "question": "What is the name of the Goblin who helped Harry, Ron, and Hermione break into Gringotts?",
        "options": ["Griphook", "Bogrod", "Travers", "Barty Crouch Sr."],
        "answer": "Griphook"
    },
    {
        "question": "What is the core of Voldemort's wand?",
        "options": ["Phoenix feather", "Dragon heartstring", "Unicorn hair", "Veela hair"],
        "answer": "Phoenix feather"
    },
    {
        "question": "Which spell did Hermione use to wipe her parents' memories of her?",
        "options": ["Obliviate", "Expelliarmus", "Stupefy", "Alohomora"],
        "answer": "Obliviate"
    },
    {
        "question": "What are the names of Bellatrix Lestrange's sisters?",
        "options": ["Narcissa and Andromeda", "Narcissa and Tonks", "Andromeda and Molly", "Molly and Fleur"],
        "answer": "Narcissa and Andromeda"
    },
    {
        "question": "Who was the headmaster of Durmstrang Institute during the Triwizard Tournament?",
        "options": ["Igor Karkaroff", "Victor Krum", "Gellert Grindelwald", "Igor Stravinsky"],
        "answer": "Igor Karkaroff"
    },
    {
        "question": "What is the name of Dumbledore's brother?",
        "options": ["Aberforth", "Alberic", "Albus", "Aberon"],
        "answer": "Aberforth"
    },
    {
        "question": "What was the name of the dragon Harry faced during the Triwizard Tournament?",
        "options": ["Horntail", "Norbert", "Smaug", "Toothless"],
        "answer": "Horntail"
    },
    {
        "question": "What is the name of the ghost that haunts the girls' bathroom at Hogwarts?",
        "options": ["Nearly Headless Nick", "Moaning Myrtle", "The Fat Friar", "The Grey Lady"],
        "answer": "Moaning Myrtle"
    },
    {
        "question": "Who is the head of the Department for the Regulation and Control of Magical Creatures at the Ministry of Magic?",
        "options": ["Kingsley Shacklebolt", "Barty Crouch Sr.", "Dolores Umbridge", "Rufus Scrimgeour"],
        "answer": "Barty Crouch Sr."
    },
    {
        "question": "What is the core of Harry Potter's wand?",
        "options": ["Phoenix feather", "Dragon heartstring", "Unicorn hair", "Veela hair"],
        "answer": "Phoenix feather"
    },
    {
        "question": "Who is the author of 'Fantastic Beasts and Where to Find Them'?",
        "options": ["Gilderoy Lockhart", "Newt Scamander", "Xenophilius Lovegood", "Newton Artemis Fido Scamander"],
        "answer": "Newton Artemis Fido Scamander"
    },
    {
        "question": "What is the name of the house-elf who serves the Black family?",
        "options": ["Dobby", "Kreacher", "Winky", "Hokey"],
        "answer": "Kreacher"
    },
    {
        "question": "Which Quidditch position does Ginny Weasley play for the Gryffindor team?",
        "options": ["Seeker", "Chaser", "Keeper", "Beater"],
        "answer": "Chaser"
    },
    {
        "question": "What spell did Hermione use to free Sirius Black from the tower in 'Harry Potter and the Prisoner of Azkaban'?",
        "options": ["Expecto Patronum", "Expelliarmus", "Alohomora", "Lumos Maxima"],
        "answer": "Expecto Patronum"
    },
    {
        "question": "What is the name of the magical newspaper in the wizarding world?",
        "options": ["The Daily Prophet", "The Quibbler", "The Daily Bugle", "The Marauder's Map"],
        "answer": "The Daily Prophet"
    },
    {
        "question": "What is the Animagus form of Sirius Black?",
        "options": ["Stag", "Wolf", "Dog", "Rat"],
        "answer": "Dog"
    },
    {
        "question": "What is the name of the wizarding bank in the Harry Potter series?",
        "options": ["Gringotts", "Diagon Alley Bank", "Goblin Gold Exchange", "Vaultus Magicus"],
        "answer": "Gringotts"
    },
    {
        "question": "What is the name of Sirius Black's brother who was a Death Eater?",
        "options": ["Regulus", "Kreacher", "Barty Crouch Jr.", "Fenrir Greyback"],
        "answer": "Regulus"
    },
    {
        "question": "Which Horcrux did Harry destroy first?",
        "options": ["Tom Riddle's diary", "Nagini", "The locket", "Rowena Ravenclaw's diadem"],
        "answer": "Tom Riddle's diary"
    },
    {
        "question": "What is the Animagus form of Rita Skeeter?",
        "options": ["Beetle", "Raven", "Spider", "Fly"],
        "answer": "Beetle"
    },
    {
        "question": "Who was the Head of the Department of Magical Law Enforcement at the Ministry of Magic?",
        "options": ["Amelia Bones", "Cornelius Fudge", "Kingsley Shacklebolt", "Pius Thicknesse"],
        "answer": "Amelia Bones"
    }
]

global answers,crct_ans,ques_ans,q_no,q,option_buttons,op
op=[]                       #consists of options of all questions
option_buttons=[]           #consists of options of one question at a time
q_no=[]                     #consists of the question numbers
q=[]                        #consists of the question label
answers=[None]*4            #the answer the user chooses
crct_ans=[None]*4           #list of label to display the correct answers
ques_ans=[]                 #list of correct answers for the questions

#Function to initially display questions and options
def make_ques():
    for i in range(4):
        answers[i]=StringVar()
    for j in range(4):
        q1 = ttk.Label(frm, text="", font="Helvetica 12 bold", wraplength=600,background="#8B0000",foreground="#FFD700")
        q1.pack(fill=X,pady=10)
        q.append(q1)
        option_buttons = []
        for k in range(4):
            option_button = ttk.Radiobutton(frm, text="", variable=answers[j], value=0, style="Custom.TRadiobutton")
            option_buttons.append(option_button)
            option_button.pack(fill=X)
        crct_ans[j]=Label(frm,text="",font=("Helvetica", 10),background="#C4A484")
        crct_ans[j].pack()
        crct_ans.append(crct_ans[j])

        show_ques(q1,option_buttons)
    
#Function to display different questions
def show_ques(q1,option_buttons):
    current_ques=random.randint(0,22)
    while current_ques in q_no:
        current_ques=random.randint(0,18)
    q_no.append(current_ques)
    q1.config(text=questions[current_ques]["question"])
    ques_ans.append(questions[current_ques]["answer"])
    for i in range(4):
        option_buttons[i].config(text=questions[current_ques]["options"][i],value=questions[current_ques]["options"][i])
    op.append(option_buttons)
    
#Function to check correct answers
def check_answer():
    score=0
    for i in range(4):
        if answers[i].get()==ques_ans[i]:
            score+=1
            crct_ans[i].config(text=(f"Correct answer: {ques_ans[i]}!"),foreground="green",font="Lucida 10")
        else :
            crct_ans[i].config(text=(f"Correct answer: {ques_ans[i]}!"),foreground="red",font="Lucida 8")
            #crct_ans.pack()
        
    choice=tmsg.askyesno("Game Over!",(f"Your score is {score}/4! Want to play again?"),icon="question")
    if choice==True:
        play_again()
    else:
        exit()

#Function that deals with play again     
def play_again():
    q_no=[]
    ques_ans.clear()
    global option_buttons
    for i in range(4):
        answers[i].set("")
        crct_ans[i].config(text="")

    for i in range(4):
        show_ques(q[i],op[i])  

#GUI
root=Tk()
root.geometry("700x800")
root.title("Harry Potter Quiz")
root.configure(bg="#FFFDD0")
root.wm_iconbitmap("CodSoft_Task5\hp.ico")

main_frm=tk.Frame(root)
main_frm.pack(fill=BOTH,expand=1)

canvas=tk.Canvas(main_frm)
canvas.pack(fill="both",expand=1)

scrollbar=ttk.Scrollbar(canvas,orient="vertical",command=canvas.yview)
scrollbar.pack(side=RIGHT,fill=BOTH)
canvas.configure(yscrollcommand=scrollbar.set,scrollregion=canvas.bbox("all"))
canvas.bind('<Configure>')

frm=Frame(canvas,bg="#C4A484",padx=5,pady=5)
canvas.create_window((0,0),window=frm,anchor="nw")

title=tk.Label(frm, text="Harry Potter Quiz", font=("Lobster",26),justify="center",foreground="#FFD700",bg="#8B0000")
title.pack(fill=BOTH)

make_ques()

submit_button = ttk.Button(frm, text="Submit", command=check_answer, style="Custom.TButton")
submit_button.pack(pady=10)

custom_style = ttk.Style()
custom_style.configure("Custom.TRadiobutton", font=("Lucida", 12), foreground="#8B0000",background="#DECDB9")
custom_style.configure("Custom.TButton", foreground="black", background="yellow", font=("Lucida", 12))

frm.pack(fill=BOTH)
root.mainloop()