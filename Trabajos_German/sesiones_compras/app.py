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


@app.route('/comprar',  methods=['GET'])
def comprar(idproducto):
    return "Por favor inicie sesión"



app.run(debug = False, port=5000)

