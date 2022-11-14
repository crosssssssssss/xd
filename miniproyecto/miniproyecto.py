from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
from tkinter import Tk, Label
import speech_recognition as sr

raiz=Tk()
raiz.title("Emulacion en lengua de señas")
raiz.geometry("1280x720")
imagenF = PhotoImage(file="Fondo.png")
FondoF = Label(image = imagenF)
FondoF.place(x=0, y=0, relwidth=1, relheight=1)
vp=Frame(raiz)
vp.grid(column=0, row=0, padx=(30,30), pady=(5,5))
miFrame=Frame()
miFrame.config(bg="white", width="1164", height="520", bd=6, relief="groove")
miFrame.place(x=100, y=20)
microimg=PhotoImage(file="fotomicro.png")
microimg.subsample(100)
bandera = False

#Palabras:
gato=["gato"]
perro=["perro"]
def visualizar2():
    global cap
    global palabraDos
    global cap2
    global cap3
    global cap4
    global cap5
    if cap is not None:      
        ret, frame = cap2.read()
        if ret == True:
            frame = imutils.resize(frame, width=950, height=510)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, visualizar)

        else:
            lblVideo.image = ""
            cap2.release()
            miFrame=Frame()
            miFrame.config(bg="white", width="1164", height="520", bd=6, relief="groove")
            miFrame.place(x=100, y=20)
    else:
        print("Error1")

def visualizar():
    global cap
    if cap is not None:
        ret, frame = cap.read()
        if ret == True:
            frame = imutils.resize(frame, width=950, height=510)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, visualizarA)

        else:
            lblVideo.image = ""
            cap.release()

cap = None

def codigoB():
    global cap
    global visualizar
    global bandera
    if cap is not None:
        lblVideo.image = ""
        cap.release()
        cap = None
    with sr.Microphone() as source:
        print('Speak Anything : ')
        r = sr.Recognizer()
        audio = r.listen(source)  
        try:
            text = r.recognize_google(audio, language='es-ES')     
            text=text.lower()
            text= text.replace(" ", "")
            text= text.replace("á", "a")
            text= text.replace("é", "e")
            text= text.replace("í", "i")
            text= text.replace("ó", "o")
            text= text.replace("ú", "u")
            text= text.replace("?", "")
            text= text.replace("¿", "")
            text= text.replace("!", "")
            text= text.replace("¡", "")
            text= text.replace(",", "")
            text= text.replace(".", "")
            print('You said: {}'.format(text))
            if bandera == False:   
                for item in range(len(gato)):                                            #Gato 1
                    if (gato[item] == (text)):
                        bandera = False;           
                        lblVideo.image = ""
                        cap = None
                        video=('gato.mp4')
                        cap = cv2.VideoCapture(video)
                        visualizar()

                    else:    
                        for item in range(len(perro)):                                          #Perros? 2
                            if (perro[item] == (text)):
                                bandera = False;           
                                lblVideo.image = ""
                                cap = None
                                video=('perro.mp4')
                                cap = cv2.VideoCapture(video)
                                print("xd")
                                visualizar()

                            else:      
                                print("")


        finally:
            print("No se escucho nada")

botonM=Button(raiz, width=100, height=100, image=microimg, command=codigoB)
botonM.config(cursor="hand2")
botonM.place(x=624, y=570)
lblVideo = Label(raiz)
lblVideo.place(x=105, y=24)

raiz.mainloop()





















