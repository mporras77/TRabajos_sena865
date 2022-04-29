# -*- coding: utf-8 -*-
from flask import Flask,render_template


app = Flask(__name__)  


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/inicio')
def inicio():
    return render_template("index.html")


@app.route('/lugares')
def lugares():
    return render_template("lugares.html")


@app.route('/simulacion')
def simulacion():
    return render_template("simulacion.html")


@app.route('/reservas')
def reservas():
    return render_template("reservas.html")


@app.route('/registro')
def registro():
    return render_template("registro.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/perfil')
def perfil():
    return render_template("perfil.html")


@app.route('/ayuda')
def ayuda():
    return render_template("ayuda.html")


@app.route('/salir')
def salir():
    return render_template("salir.html")

@app.route('/carrito')
def carrito():
    return render_template("carrito.html")











app.run(debug = True, port=5000)
