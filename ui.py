THEME_COLOR = "#375362"
import time
from tkinter import *
from quiz_brain import *

class UserInterface:
    def __init__(self,quiz):
        self.quiz=quiz
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=350,height=400)
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.canvas=Canvas(width=300,height=250)
        #canvas.config(padx=20,pady=20)
        self.canvas.grid(column=0,row=1,columnspan=2,padx=10,pady=50)
        trueimg=PhotoImage(file="./images/true.png")
        falseimg = PhotoImage(file="./images/false.png")
        self.truebut=Button(image=trueimg,highlightthickness=0,command=lambda : self.check("true"))
        self.truebut.grid(column=0,row=2)
        self.falsebut = Button(image=falseimg,highlightthickness=0,command=lambda : self.check("false"))
        self.falsebut.grid(column=1, row=2)
        self.ques=self.canvas.create_text(150,125,text="Nothing",font=("Arial",20,"italic"),width=280)
        self.score=Label(text=f"Score:{self.quiz.score}",bg=THEME_COLOR,fg="white")
        self.score.grid(column=1,row=0)
        self.getnextq()
        self.window.mainloop()
    def changec(self):
        self.canvas.config(bg="white")
        self.getnextq()
    def getnextq(self):
        x=self.quiz.next_question()
        self.canvas.itemconfig(self.ques,text=x)
        #self.canvas.config(bg="white")
    def check(self,ans):
        is_correct=self.quiz.check_answer(ans)
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.changec)

