# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 13:38:40 2022

@author: Raymundo Soto
"""

from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def run():
    def acceder_bd():
        user = entry_1.get()
        passcode = entry_2.get()
                
        try:
            if user == '':
                messagebox.showinfo(message="No suministro nombre de usuario", title="Advertencia")
                entry_1.delete(0,END)
                entry_2.delete(0,END)
            if passcode == '':
                messagebox.showinfo(message="No suministro contraseña de usuario", title="Advertencia")
                entry_1.delete(0,END)
                entry_2.delete(0,END)
                 
            name_db = 'users_data.db'
            conn= sql.connect(name_db)
            cursor = conn.cursor()
            instruccion = f"SELECT * FROM datos_usuario WHERE usuario = '{user}'"  # WHERE FILTRA DATOS
            cursor.execute(instruccion)             
            datos = cursor.fetchall()             
            conn.commit()
            conn.close()
            
    
            if passcode == datos[0][1]:
                messagebox.showinfo(message="La contraseña es correcta, accesso otorgado",
                                    title="Bienvenido")
                entry_1.delete(0,END)
                entry_2.delete(0,END)
                ventana_secundaria()
                   
            else:
                respuesta = messagebox.showinfo(message="La contraseña es incorrecta, intente de nuevo",
                                       title="Acceso denegado")
                       
        except:
            
            messagebox.showinfo(message="No existen datos de usuario",
                                title="Error")
            entry_1.delete(0,END)
            entry_2.delete(0,END)
            
    def ventana_secundaria():
        ventana_2 = Toplevel(ventana_login)
        ventana_2.geometry('600x300')
        ventana_2.title('Ventana secundaria')
        label_ven_2 = Label(ventana_2, text='Acceso a la ventana 2')
        label_ven_2.config(fg="blue",    
             bg="white",   
             font=("Verdana",24)) 
        label_ven_2.pack()

      
            
    def salir():
        ventana_login.destroy()
    
    ventana_login = Tk()
    ventana_login.geometry('600x400')
    ventana_login.title('Ventana de acceso')
    
    frame_1 = Frame(ventana_login, bg='gray')
    frame_1.config(bg="gray") 
    frame_1.config(width="300", height="100")
    frame_1.place(x=50, y=50)
    frame_1.config(relief="groove")   
    frame_1.config(cursor="spider")     
    
    label_1 = Label(frame_1, text='Usuario')
    label_1.place(x=30, y=40)
    entry_1 = Entry(frame_1, width=20)
    entry_1.place(x=100,y=40)
    
    frame_2 = Frame(ventana_login, bg='gray')
    frame_2.config(bg="gray") 
    frame_2.config(width="300", height="100")
    frame_2.place(x=50, y=200)
    frame_2.config(relief="ridge")   #cambiar el tipo de borde
    frame_2.config(cursor="pirate")    #cambiar el tipo de cursor 
    
    label_2 = Label(frame_2, text='Contraseña')
    label_2.place(x=30, y=40)
    entry_2 = Entry(frame_2, width=20, show='*')
    entry_2.place(x=120,y=40)
    
    button = Button(ventana_login, text = 'Acceder', width = 15, command = acceder_bd)
    button.place(x=400, y=150)
    
    boton_salir = Button(ventana_login, text = 'Salir', width = 20, command=salir)
    boton_salir.place(x=400, y=350)
    
    
    
    
    
    
    ventana_login.mainloop()


if __name__ == '__main__':
    
    run()

