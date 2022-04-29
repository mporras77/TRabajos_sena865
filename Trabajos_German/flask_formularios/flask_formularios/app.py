# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, redirect, url_for


app = Flask(__name__)
#con esta llave firmamos las cookies
app.secret_key = '54SF4GHAFHGAS4'


#RUTAS QUE SIRVEN LAS INTERFACES
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/interfazsuma')
def interfaz_suma():
    return render_template('suma.html')


@app.route('/interfazresta')
def interfaz_resta():
    return render_template('resta.html')


#RUTAS QUE REALIZAN LA LOGICA
@app.route('/suma', methods=['POST'])
def suma():
    numero1 = request.form.get("numero1")
    print("numero 1: ", numero1)
    numero2 = request.form.get("numero2")
    suma_num = int(numero1) + int(numero2)
    mensaje = "La suma de {} y {} es : {}".format(numero1,numero2, suma_num)
    return mensaje


@app.route('/resta', methods=['POST'])
def resta():
    numero1 = request.form.get("numero1")
    numero2 = request.form.get("numero2")
    resta_num = int(numero1) - int(numero2)
    mensaje = "La resta de {} y {} es : {}".format(numero1,numero2, resta_num)
    return mensaje




app.run(debug = False, port=5000)

