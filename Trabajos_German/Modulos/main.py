from ast import Return
import os
import sqlite3

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


BASE_DIR= os.path.dirname(os.path.abspath(_file_))
db_path = os.path.join(BASE_DIR, "db.db")



def registro():
    
    menu= input("Si desea registrarse marque si \n  Si iniciar seccion  marque no")
    if menu== "si":
        print("Ingrese sus datos")
        correo= str(input("Ingrese su correo"))
        contrasena= str(input("Ingrese su contrasena"))
        nombres= str(input("Ingrese sus Nombres"))
        telefono= int(input("Ingrese su Telefono"))
        cuidad= str(input("Ingrese su Cuidad"))
        edad= int(input("Ingrese su Edad"))

        #print("sus datos personales son",correo,contrasena,nombres,telefono,cuidad,edad,"Por favor confirmar si es correcto")
        verificacion=input("Sus datos son correctos?")
        
        if verificacion == "si":
            
            
            
            
            
    
            con_bd = sqlite3.connect('base1.db')
            #cursor a la db
            cursor_db = con_bd.cursor()
            #consultas
            sql = "INSERT INTO sistema(Correo, Edad, Contrasena, Nombres, Telefono, Ciudad ) VALUES(?, ?, ?, ?, ?, ?)"
            cursor_db.execute(sql, (correo,edad,contrasena, nombres, telefono, cuidad))
            con_bd.commit()
            #cierre del cursor
            cursor_db.close()
            
            
            proveedor_correo = 'smtp.gmail.com: 587'
            remitente ='gomeloslos8@gmail.com'
            password ='1004871606'
            servidor = smtplib.SMTP(proveedor_correo)
            servidor.starttls()
            servidor.ehlo()
            servidor.login(remitente, password)
            mensaje = "<h1>Bievenido a nuestra Plataforma de  Tursismo Sueña</h1>"
            msg = MIMEMultipart()
            msg.attach(MIMEText(mensaje,'html'))
            msg['From'] = remitente
            msg['To'] = correo
            msg['Subject'] = 'Registro Exitoso'
            servidor.sendmail(msg['From'] , msg['To'], msg.as_string())

            iniciologin= input("Su Registro fue Exitoso ¿Desea Iniciar Seccion?")
            if iniciologin == "si":
                return login()
            else:
                return registro()
                
        
        
        return login()
    


#credenciales
            
    
            
            


def login():
    correo=input("Ingrese su Correo")
    contrasena=input("Ingrese su Contrasena")
    
    con_bd = sqlite3.connect('base1.db')
    cursor_db = con_bd.cursor()
    sql = "SELECT Contrasena, Nombres  FROM  sistema WHERE Correo=?"
    cursor_db.execute(sql, (correo,))
    fila = cursor_db.fetchone()
    #print(fila)
    if fila is not None:
        
        if contrasena == fila [0]:
            return Bienvenida(correo)
                
        else:
            print("Correo o Contrasena Incorrecta")



def Bienvenida(email):
    
    print("Bienvenido/a al Sistema")
    
    con_bd = sqlite3.connect('base1.db')
    #cursor a la db
    cursor_db = con_bd.cursor()
    #consultas
    sql = "SELECT Nombres, Edad, Telefono FROM  sistema WHERE Correo=?"
    cursor_db.execute(sql, (email,))
    fila = cursor_db.fetchone()
    if len(fila) > 0:
        if len(fila) > 0:
            print(fila[0])
        if len(fila) > 0:
            print("Su telefono",fila[2])
            
        print("Su edad es",fila[1])
        return
    
            

registro()