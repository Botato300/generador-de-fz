from tkinter import *
import subprocess

ventana = Tk()
ventana.title("FenixZone Roleplay Bypass Advanced")
ventana.iconbitmap("resources/logo.ico")
ventana.geometry("500x200")
ventana.resizable(0, 0)

imagenfondo = PhotoImage(file = "resources/fondo.gif")
fondo = Label(ventana, image = imagenfondo)
fondo.place(x = -5, y = -5)

fcolor = "#121212"

servidor = StringVar(ventana)
servidor.set("Seleccione uno...")
servidores = ["[S1] FenixZone RP", "[S2] FenixZone RP", "[S4] FenixZone RP", "[S5] FenixZone RP"]
opcion = OptionMenu(ventana, servidor, *servidores)

def ejecutar():
	subprocess.Popen(["creditcard-generator.exe"])

t1 = Label(ventana, font = "Helvetica 12 bold", text = "Nombre y Apellido:", bg = fcolor, fg = "white")
t1.place(x = 10, y = 10, width = 160, height = 30)
et1 = Entry(ventana, font = "Verdana 11")
et1.place(x = 190, y = 15, width = 180, height = 20)

t2 = Label(ventana, font = "Helvetica 12 bold", text = "Servidor:", bg = fcolor, fg = "white")
t2.place(x = -25, y = 50, width = 150, height = 20)
et2 = Label(ventana, bg = "#00CB00", textvariable = servidor)
et2.place(x = 100, y = 50)

opcion.config(width = 10)
opcion.place(x = 210, y = 46, width = 150, height = 25)

t3 = Label(ventana, font = "Verdana 10 bold", text = "El servidor [S3] y el servidor [BR] no están disponibles.", bg = "red")
t3.place(x = 15, y = 80, width = 400, height = 15)

t4 = Label(ventana, font = "Helvetica 11 bold", text = "Bypassear:" , bg = fcolor, fg = "white")
t4.place(x = 11, y = 110)
et4 = Button(ventana, text = "Click aquí", command = ejecutar)
et4.place(x = 130, y = 111, height = 25)

t5 = Label(ventana, font = "Helvetica 8 bold", text = "Software desarrollado por Votati", bg = fcolor, fg ="white")
t5.place(x = 10, y = 180)

ventana.mainloop()
