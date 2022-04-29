# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session


app = Flask(__name__)
#con esta llave firmamos las cookies
app.secret_key = '54SF4GHAFHGAS4'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    session["user"] = "ricardo@gmail.com"
    return render_template('tienda.html')


@app.route('/comprar/<idproducto>',  methods=['GET'])
def comprar_f(idproducto):
    if "user" in session:
        email =  session["user"]
        return "Señor {} Ud ha comprado el articulo de id {}".format(email, idproducto)
    return "Por favor inicie sesión"


@app.route('/cerrarsesion',  methods=['GET'])
def cerrar_sesion():
    if "user" in session:
        session.pop("user")
        return "sesión cerrada"
    return "Por favor inicie sesión"





app.run(debug = False, port=5000)

