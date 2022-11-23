from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
from time import sleep
from threading import Thread

import sounddevice as sd 
import soundfile as sf 




###### Cores usadas #######
cor1 = "#3d3d3d"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul

fundo = cor2

janela = Tk()
janela.title("Alarme Digital") 
janela.geometry('425x175')
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=fundo)

# DIVIDIR A TELA EM 2 FRAMES
frame_logo = Frame(janela, width=400, height=10, bg=fundo)
frame_logo.grid(row=0,column=0,pady=1, padx=0)


frame_corpo = Frame(janela, width=400, height=290, bg=fundo)
frame_corpo.grid(row=1,column=0,pady=1, padx=0)


# CONFIG O FRAME LOGO

l_linha = Label(frame_logo, width=400, height=1, bg=fundo, anchor =NW, font=('Ivy 2 '))
l_linha.place(x=1,y=0)



# CONFIG CORPO

imagem = Image.open('icon.png')
imagem = imagem.resize((100,100))
imagem = ImageTk.PhotoImage(imagem)

l_imagem = Label(frame_corpo, height=100,image=imagem,padx=10, compound=LEFT, bg=fundo, fg=fundo, anchor =NW, font=('Ivy 18 bold'))
l_imagem.place(x=10,y=10)

l_nome = Label(frame_corpo, text='Alarme Digital', height=1, bg=fundo, fg=cor1, anchor =NE)
l_nome.place(x=105,y=10)

# CREATE BOXES
l_h = Label(frame_corpo, text='Horas', height=1, bg=fundo, fg=cor1, anchor =NE)
l_h.place(x=130,y=40)

c_hora = Combobox(frame_corpo, width=2, font=('Ivy 16 '))
c_hora['value'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24")
c_hora.current(0)
c_hora.place(x=130,y=60)


l_min = Label(frame_corpo, text='Min.', height=1, bg=fundo, fg=cor1, anchor =NE)
l_min.place(x=180,y=40)

c_min = Combobox(frame_corpo, width=2, font=('Ivy 16 '))
c_min['value'] = ("00","01","02","03","04","05","06","07","08","09","10",\
    "11","12","13","14","15","16","17","18","19","20"
    ,"21","22","23","24","25","26","27","28","29","30",\
    "31","32","33","34","35","36","37","38","39","40",\
    "41","42","43","44","45","46","47","48","49","50",
    "51","52","53","54","55","56","57","58","59"
    
    )
c_min.current(0)
c_min.place(x=180,y=60)

l_s = Label(frame_corpo, text='Seg.', height=1, bg=fundo, fg=cor1, anchor =NE)
l_s.place(x=225,y=40)

c_seg = Combobox(frame_corpo, width=2, font=('Ivy 16 '))
c_seg['value'] = ("00","01","02","03","04","05","06","07","08","09","10",\
    "11","12","13","14","15","16","17","18","19","20"
    ,"21","22","23","24","25","26","27","28","29","30",\
    "31","32","33","34","35","36","37","38","39","40",\
    "41","42","43","44","45","46","47","48","49","50",
    "51","52","53","54","55","56","57","58","59"
    
    )
c_seg.current(0)
c_seg.place(x=230,y=60)

l_s = Label(frame_corpo, text='Periodo', height=1, bg=fundo, fg=cor1, anchor =NW)
l_s.place(x=280,y=40)

c_per = Combobox(frame_corpo, width=2, font=('Ivy 15 '))
c_per['value'] = ("AM","PM")
c_per.current(0)
c_per.place(x=280,y=60)




def ativar_alarme():
    if selecionado.get():
        print('Ativar:', selecionado.get())
        alarme()

selecionado = IntVar()

radio = Radiobutton(frame_corpo,command=ativar_alarme, text='Ativar', font=('Ivy 10'), fg=cor4,bg=fundo,value=1, variable=selecionado)
radio.place(x=125,y=95)



def tocar_alarme():
        array, smp_rt = sf.read('music.mp3', dtype = 'float64')   
        sd.play(array, smp_rt) 
        status = sd.wait()   
        sd.stop()


def alarme():       
    while True:
            control = selecionado.get()
            h_alarme = c_hora.get()
            m_alarme = c_min.get()
            s_alarme = c_seg.get()
            p_alarme = c_per.get()
            hora_atual = datetime.now()

            hora = hora_atual.strftime("%H")
            minutos = hora_atual.strftime("%M")
            segundos = hora_atual.strftime("%S")
            periodo = hora_atual.strftime("%p")
            if control == 1:
                if p_alarme == periodo:
                    if h_alarme == hora:
                        if m_alarme == minutos:
                            if s_alarme == segundos:
                                print("Chegou a hora!!!")
                                tocar_alarme()
    
            
    
janela.mainloop()
