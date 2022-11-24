import tkinter
import customtkinter
import tkinter as tk
import tkinter.filedialog as fd
import os
from tkinter.ttk import Progressbar
import time
from tkinter import *
import glob
from PIL import ImageTk, Image
from PIL import *
from matplotlib.ft2font import HORIZONTAL
from newspaper import Article
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


# CREATE WINDOW
customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("500x400")     
app.title(" Text Summarization")
app.iconbitmap('icon.ico')


#SUMMARIZATION
def summarize(text, per):

    url = str(entry.get())
    article = Article(url)
    article.download()
    article.parse()
    nlp = spacy.load('en_core_web_sm')
    doc= nlp(text)
    tokens=[token.text for token in doc]
    word_frequencies={}
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    max_frequency=max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=word_frequencies[word]/max_frequency
    sentence_tokens= [sent for sent in doc.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():                            
                    sentence_scores[sent]=word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent]+=word_frequencies[word.text.lower()]
    select_length=int(len(sentence_tokens)*per)
    summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)
    final_summary=[word.text for word in summary]
    summary=''.join(final_summary)

    top2= Toplevel(app)
    top2.geometry("700x500")
    top2.title("Summary")
    Label(top2, text= summary, font=('Arial 9'), wraplength=600, justify="center").place(x=50,y=10)
    scrollbar = Scrollbar(top2)
    scrollbar.pack(side = RIGHT, fill = Y )
   

    #print (summary)

def run():
    url = str(entry.get())
    article = Article(url)
    article.download()
    article.parse()
    summarize(article.text, 0.20)

# TOOLBAR
def Help1():
    #Code to be written
    top= Toplevel(app)
    top.geometry("1200x210")
    top.title("Help")
    Label(top, text= "How to use:", font=('Mistral 18 bold')).place(x=50,y=10)
    Label(top,text= "Step 1: Select if the detection will be over an image or a video.", font=('Arial')).place(x=150,y=70)
    Label(top,text= "Step 2: Click the 'Upload' button to choose the file to detect. The file must be in a local storage.", font=('Arial')).place(x=150,y=110)
    Label(top,text= "Step 3: Wait 10 seconds for the detection to process. The results will be displayed automatically in a new window.", font=('Arial')).place(x=150,y=150)
    pass

frame = Frame(app)
frame.pack()
mainmenu = Menu(frame)
mainmenu.add_command(label = "Help", command= Help1)
mainmenu.add_command(label = "Exit", command= app.destroy)
app.config(menu = mainmenu)


# TITLE "DRUG DETECTION"
logo = Image.open("logo.png")
#Resize the Image using resize method
resized_image= logo.resize((400,250), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
l = Label(app, image = new_image)
l.config(bg="#1A1A1A")
l.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER) 
l.pack()

# SOFTWARE DESCRIPTION TEXT
l2 = Label(app, text = "Text Summarization and Keyword extraction")
l2.config(fg="black", bg="white", font =("helvetica", 12), wraplength=650, justify="center")
l2.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER) 
l2.pack()


#INPUT TEXT
entry = customtkinter.CTkEntry(master=app, placeholder_text="Enter URL here")
#entry.config(bg='grey')
entry.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
entry.pack(pady=12, padx=10)


# UPLOAD BUTTON
button1 = customtkinter.CTkButton(master=app, text="Summerize", command=run)
button1.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
 
#summarize(article.text, 0.20)
app.mainloop()