from tkinter import *
from gtts import gTTS
import os
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
import pyaudio
import speech_recognition as sr
import time
import playsound
from PIL import ImageTk,Image
root=Tk()
root.title('Speech Notes')
canvasWidth=1920
canvasHeight=1080
c=Canvas(root,width=canvasWidth,height=canvasHeight)
backgroundImage=ImageTk.PhotoImage(file='picmain.jpg')
c.create_image(0,0,image = backgroundImage,anchor = NW)
t=Text(c,width=80,height=30,borderwidth=8,font=('ARIAL',15))
t.place(x=10,y=10)
e=Entry(c,width=30)
e.place(x=190,y=745)
e1=Entry(c,width=30)
e1.place(x=650,y=745)
c.pack()
var=StringVar() 
i=0
j=0
k=0
mytext=""
def sel():
    lang=str(var.get())
    if 'mr-IN'==lang:
        return lang
    if 'en-IN'==lang:
        return lang
    if 'hi-IN'==lang:
        return lang
    if 'fr-FR'==lang:
        return lang
def sel1():
    lang=str(var.get())
    if 'mr-IN'==lang:
        return 'mr'
    if 'en-IN'==lang:
        return 'en'
    if 'hi-IN'==lang:
        return 'hi'
    if 'fr-FR'==lang:
        return 'fr'

def listn1():
    r = sr.Recognizer()
    with sr.Microphone() as s:
        r.adjust_for_ambient_noise(s,duration=5)
        r.dynamic_energy_threshold = True 
        audio = r.listen(s)
        data=""
        try:
            lang1=sel()
            data=r.recognize_google(audio,language=lang1)
            t.insert(END,"\n"+data)
        except sr.UnknownValueError:
            t.insert(END,"\nGoogle Speech Recognition could not understand audio\n")
        except sr.RequestError as e:
            t.insert(END,"\nCould not request results from Google Speech Recognition service; {0}".format(e))
def speech():
    mytext=t.get('1.0',END)
    print(mytext)
    global j
    lang1=sel1()
    tts = gTTS(text=mytext,lang=lang1)
    file4 = str("hi" + str(j) + ".mp3")
    tts.save(file4)
    playsound.playsound(file4,True)
    os.remove(file4)
    j=j+1
def save1():
  fi=""
  fi=e.get()
  file = open(fi+".txt", "w+")
  file.write(t.get('1.0',END))
  file.close()
def rad2():
  name=""
  name=e1.get()
  file = open(name+".txt", "r+")
  info=file.read()
  t.insert(END,"\n"+info)
  file.close()
R1=Radiobutton(c,text='ENGLISH',variable=var,value='en-IN',command=sel)
R1.place(x=20,y=680)
R1.deselect()
R2=Radiobutton(c,text='MARATHI',variable=var,value='mr-IN',command=sel)
R2.place(x=100,y=680)
R3=Radiobutton(c,text='HINDI',variable=var,value='hi-IN',command=sel)
R3.place(x=185,y=680)
R4=Radiobutton(c,text='French',variable=var,val='fr-FR',command=sel)
R4.place(x=250,y=680)

b=Button(c,text="READ",command=speech)
b.place(x=990,y=80,bordermode="inside",height=50, width=100)

b1=Button(c,text="SAVE",command=save1)
b1.place(x=50,y=730,bordermode="outside",height=50, width=100)

b2=Button(c,text="OPEN",command=rad2)
b2.place(x=500,y=730,bordermode="inside",height=50, width=100)

b3=Button(c,text="NOTE",command=listn1)
b3.place(x=990,y=250,bordermode="inside",height=50, width=100)
root.mainloop()
