#! /usr/bin/env python

import time, tkFont, Tkinter

botones=Tkinter.Tk()
root=Tkinter.Toplevel()
root.wm_title("contador")
botones.wm_title("botones")
Tkinter.mainloop(1)
bigfont=tkFont.Font(root=root, font=None, name=None, family='Mono', size=250, weight='bold')
empieza=time.time()
cuentaempezada=0
parar=0

def empezar():
  global cuentaempezada
  global empieza, parar
  cuentaempezada=1
  empieza=time.time()
  print "empezar"
  parar=0

def parar():
  global parar
  parar=1
  print "parar"

startbutton=Tkinter.Button(botones, height=10, width=30, background="#00BB00", command=empezar)
stopbutton=Tkinter.Button(botones, height=10, width=30, background="#BB0000", command=parar)
startbutton.pack()
stopbutton.pack()

while 1:
  try:
    contador.pack_forget()
  except NameError:
    pass
  if not parar:
    ahora=time.time()
    segundos=int(ahora-empieza)%60
    minutos=int(ahora-empieza)/60
  if cuentaempezada:
    contador=Tkinter.Label(root, text="%02i:%02i"%(minutos, segundos), font=bigfont)
  else:
    contador=Tkinter.Label(root, text="00:00", font=bigfont)
  empezar=Tkinter.Button()
  contador.pack()

  root.update()
  time.sleep(0.001)
