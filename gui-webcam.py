
from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
import imutils

def iniciar ():
    global cap
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    visualizar()

def visualizar():
    global cap
    if cap is not None:
        ret, frame = cap.read()
    if ret == True:
        frame = imutils.resize(frame, width=640)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        im = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=im)
        lblVideo.configure(image=img)
        lblVideo.image = img
        lblVideo.after(10, visualizar)
    else:
        lblVideo.image = ""
        cap.release()

def finalizar():
    global cap
    cap.release()

cap = None
root = Tk()
root.title('WEBCAM STREAMING by YAIR')
root.resizable(0,0)

btnIniciar = Button(root, text="INICIAR", width=45, command=iniciar)
btnIniciar.grid(row=0, column=0, padx=5, pady=5)

btnFinalizar = Button(root, text="FINALIZAR", width=45, command=finalizar)
btnFinalizar.grid(row=0, column=1, padx=5, pady=5)

lblVideo = Label(root)
lblVideo.grid(column=0, row=1, columnspan=2)

root.mainloop(

)
