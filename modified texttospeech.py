'''importing modules'''
from gtts import gTTS
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import os
import streamlit as st

def main():
    master = tk.Tk(className='Text to Speech Converter') #main window
    master.geometry("500x500")
    mainFrame =  Frame(master)
    mainFrame.pack()

    #text box creation with label
    myText_str = tk.StringVar() #string variable to get the contents of entry box
    Label(mainFrame, text='Enter your text').grid(row=0) #label for text box
    myText = Entry(mainFrame,textvariable=myText_str,bd=1,bg='white')
    myText.grid(row=0,column=10)

    #text to speech conversion function
    def text_to_speech():
        language = 'en'
        TextEntered = myText_str.get()
        if len(TextEntered)==0:
            messagebox.showerror("Error","you need to enter some text to get audio output")
        else:
            messagebox.showinfo("message",f"your input is {TextEntered}")
            obj = gTTS(text=TextEntered,slow=True)
            obj.save("audio.mp3")
            os.system("audio.mp3")


    #adding Button
    buttonFrame = Frame(master)
    buttonFrame.pack()
    convert_button = tk.Button(buttonFrame, text='Convert',fg='black',activebackground='white',activeforeground='pink',width=20,bg='white',
                               borderwidth=0,command=text_to_speech)
    convert_button.grid(row=20,column=1)
    convert_button.pack()


    master.mainloop()

if __name__ == "__main__":
    """
    # This a Text to Speech Conversion Program
    
    * The main functionality of this project is to convert the given text in a text box into a speech.
    """
    t = st.button("Start")
    if t:
        main()