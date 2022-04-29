
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, redirect, url_for
from ast import Return
import os
import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

BASE_DIR= os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "base1.db")


app = Flask(__name__)
#con esta llave firmamos las cookies
app.secret_key = '54SF4GHAFHGAS4'


@app.route('/')
def index():
   return render_template("index.html", usuario=False)


@app.route('/inicio')
def inicio():
    return render_template("Index.html")


@app.route('/lugares')
def lugares():
     numero1 = request.form.get("numero1")
     return render_template("Lugares.html")


@app.route('/simulacion')
def simulacion():
    return render_template("Simulacion.html")


@app.route('/reservas')
def reservas():
    return render_template("Reservas.html")


@app.route('/registro')
def registro():
    return render_template("Registro.html")

@app.route('/regis', methods=["POST"])
def registro_salido():
    correo = request.form.get("correo")
    contrasena = request.form.get("contrasena")
    nombres = request.form.get("nombres")
    telefono = request.form.get("telefono")
    ciudad = request.form.get("ciudad")
    edad = request.form.get("Edad")
    razon = request.form.get("razon")
    mensaje = request.form.get("mensaje")
   
    
    
    #suma_num = str(numero1) + str(numero2) + str(numero3) + str(numero4) + str(numero5) + str(numero6) + str(numero7) + str(numero8)
    #mensaje = "Su nombre Completo es {}  {} {} {} {} {}  ".format(numero1,numero2,numero3, numero4,numero5,numero6,numero7,numero8)
    
    con_bd = sqlite3.connect('base1.db')
    cursor_db = con_bd.cursor()
    sql = "INSERT INTO Usuario(Correo, Contrasena, Nombres, Telefono, Ciudad, Edad, Razon, Mensaje) VALUES(?, ?, ?, ?, ?, ?)"
    cursor_db.execute(sql, (correo, contrasena, nombres, telefono, ciudad, edad, razon, mensaje,))
    con_bd.commit()
    cursor_db.close()
    
    

    proveedor_correo = 'smtp.gmail.com: 587'
    remitente ='gomeloslos8@gmail.com'
    password ='1004871606'
    servidor = smtplib.SMTP(proveedor_correo)
    servidor.starttls()
    servidor.ehlo()
    servidor.login(remitente, password)
    mensaje = "Bienvenido a nuestra plataforma de turismo, señor(a) " + nombres 
    msg = MIMEMultipart()
    msg.attach(MIMEText(mensaje,'html'))
    msg['From'] = remitente
    msg['To'] = mensaje
    msg['Subject'] = 'Registro Exitoso'
    servidor.sendmail(msg['From'] , msg['To'], msg.as_string())
    
    
    return render_template("Index.html")
    
    
    
@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/logins', methods=["POST"])
def logins_salida():
    correo = request.form.get("correo")
    contrasena = request.form.get("contrasena")
    
    con_bd = sqlite3.connect('base1.db')
    cursor_db = con_bd.cursor()
    sql = "SELECT Correo, Contrasena  FROM  Usuario WHERE Correo=?"
    cursor_db.execute(sql, (correo,))
    fila = cursor_db.fetchone()
    session["user"] = correo
    
    if fila is not None:
        
        if contrasena == fila [1]:
            return render_template('Reservas.html',usuario = fila[1],)
            
        else:
            
            return render_template("login.html") 
    return render_template("Reservas.html")


@app.route('/reservas/<idproducto>',  methods=['GET'])
def comprar_f(idproducto):
    if "user" in session:
        email =  session["user"]
        id_producto=int(idproducto)
        con_bd = sqlite3.connect('base1.db')
        cursor_db = con_bd.cursor()
        sql = "SELECT Producto  FROM  tienda WHERE Idproducto=?"
        cursor_db.execute(sql, (id_producto,))
        nombre= cursor_db.fetchone()
        
       
        proveedor_correo = 'smtp.gmail.com: 587'
        remitente ='gomeloslos8@gmail.com'
        password ='1004871606'
        servidor = smtplib.SMTP(proveedor_correo)
        servidor.starttls()
        servidor.ehlo()
        servidor.login(remitente, password)
        mensaje =  f"<h1>Gracias por Reservar en  nuestra Plataforma de  Turismo Usuario {nombres} a continuacion los datos de su reserva </h1>"
        msg = MIMEMultipart()
        msg.attach(MIMEText(mensaje,'html'))
        msg['From'] = remitente
        msg['To'] = email
        msg['Subject'] = 'Reserva Exitosa'
        servidor.sendmail(msg['From'] , msg['To'], msg.as_string())

        
        
        return    render_template('compraexitosa.html',email=email,nombre=nombre)#"Señor {} Ud ha comprado una reserva id {}".format(email, nombre)
    return render_template('login.html')

@app.route('/cerrarsesion',  methods=['GET'])
def cerrar_sesion():
    if "user" in session:
        session.pop("user")
        return render_template('cerrarsesion.html')
    return  render_template('login.html')


@app.route('/perfil')
def perfil():
    return render_template("perfil.html")


@app.route('/ayuda')
def ayuda():
     return render_template("ayuda.html")

@app.route('/help', methods=["POST"])
def perdi_ayuda():
    nombres = request.form.get("nombres")
    correo = request.form.get("correo")
    telefono = request.form.get("telefono")
    razon = request.form.get("razon")
    mensaje = request.form.get("mensaje")


    db_path = os.path.join(BASE_DIR, "db.db")
    con_bd = sqlite3.connect('base1.db')
    cursor_db = con_bd.cursor()
    
    sql = "INSERT INTO Ayuda(Nombres, Correo, Telefono, Razon, Mensaje ) VALUES(?, ?, ?, ?, ?)"
    cursor_db.execute(sql, (nombres, correo, telefono, razon, mensaje,))
    con_bd.commit()
    cursor_db.close()
 
    con_bd = sqlite3.connect('base1.db')
    
    proveedor_correo = 'smtp.gmail.com: 587'
    remitente ='gomeloslos8@gmail.com'
    password ='1004871606'
    servidor = smtplib.SMTP(proveedor_correo)
    servidor.starttls()
    servidor.ehlo()
    servidor.login(remitente, password)
    mensaje = f"<h1>Hola {nombres} emos visto tu mensaje</h1>"
    msg = MIMEMultipart()
    msg.attach(MIMEText(mensaje,'html'))
    msg['From'] = remitente
    msg['To'] = correo
    msg['Subject'] =
    
    servidor.sendmail(msg['From'] , msg['To'], msg.as_string())

    return render_template("ayuda.html")

@app.route('/salir')
def salir():
    return render_template("/regis")



app.run(debug = True, port=5000)
